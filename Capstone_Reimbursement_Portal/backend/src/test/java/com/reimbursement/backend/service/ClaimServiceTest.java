package com.reimbursement.backend.service;

import com.reimbursement.backend.dto.ClaimRequestDTO;
import com.reimbursement.backend.entity.Claim;
import com.reimbursement.backend.entity.User;
import com.reimbursement.backend.enums.ClaimStatus;
import com.reimbursement.backend.enums.Role;
import com.reimbursement.backend.exception.ResourceNotFoundException;
import com.reimbursement.backend.exception.BadRequestException;
import com.reimbursement.backend.repository.ClaimRepository;
import com.reimbursement.backend.repository.UserRepository;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import java.time.LocalDate;
import java.util.Optional;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;


class ClaimServiceTest {

    @Mock
    private ClaimRepository claimRepository;

    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private ClaimService claimService;

    private User employee;
    private User manager;

    @BeforeEach
    void setup() {
        MockitoAnnotations.openMocks(this);

        manager = new User();
        manager.setId(2L);
        manager.setRole(Role.MANAGER);

        employee = new User();
        employee.setId(1L);
        employee.setRole(Role.EMPLOYEE);
        employee.setManager(manager);
    }

    // ================= TEST 1 =================
    @Test
    void submitClaim_success() {

        ClaimRequestDTO dto = new ClaimRequestDTO();
        dto.setAmount(500.0);
        dto.setDate(LocalDate.now());
        dto.setDescription("Travel");

        when(userRepository.findById(1L)).thenReturn(Optional.of(employee));
        when(claimRepository.save(any(Claim.class))).thenAnswer(i -> i.getArgument(0));

        var response = claimService.submitClaim(dto, 1L);

        assertNotNull(response);
        assertEquals("Travel", response.getDescription());
        assertEquals(ClaimStatus.SUBMITTED, response.getStatus());

        verify(claimRepository, times(1)).save(any(Claim.class));
    }

    // ================= TEST 2 =================
@Test
void submitClaim_employeeNotFound() {

    ClaimRequestDTO dto = new ClaimRequestDTO();
    dto.setAmount(500.0);
    dto.setDate(LocalDate.now());
    dto.setDescription("Travel");

    when(userRepository.findById(1L)).thenReturn(Optional.empty());

    assertThrows(RuntimeException.class, () -> {
        claimService.submitClaim(dto, 1L);
    });
}


// ================= TEST 3 =================
@Test
void approveClaim_success() {

    Claim claim = new Claim();
    claim.setId(1L);
    claim.setStatus(ClaimStatus.SUBMITTED);


    claim.setEmployee(employee);
    claim.setReviewer(manager);

    when(claimRepository.findById(1L)).thenReturn(Optional.of(claim));
    when(claimRepository.save(any(Claim.class))).thenReturn(claim);

    var result = claimService.approveClaim(1L, 2L, "ok");

    assertEquals(ClaimStatus.APPROVED, result.getStatus());
}


// ================= TEST 4 =================
@Test
void approveClaim_wrongReviewer() {

    Claim claim = new Claim();
    claim.setId(1L);
    claim.setStatus(ClaimStatus.SUBMITTED);
    claim.setReviewer(manager);

    when(claimRepository.findById(1L)).thenReturn(Optional.of(claim));

    assertThrows(RuntimeException.class, () -> {
        claimService.approveClaim(1L, 999L, "ok");
    });
}


// ================= TEST 5 =================
@Test
void approveClaim_alreadyProcessed() {

    Claim claim = new Claim();
    claim.setId(1L);
    claim.setStatus(ClaimStatus.APPROVED);
    claim.setReviewer(manager);

    when(claimRepository.findById(1L)).thenReturn(Optional.of(claim));

    assertThrows(RuntimeException.class, () -> {
        claimService.approveClaim(1L, 2L, "ok");
    });
}


// ================= TEST 6 =================
@Test
void rejectClaim_success() {

    Claim claim = new Claim();
    claim.setId(1L);
    claim.setStatus(ClaimStatus.SUBMITTED);
    claim.setReviewer(manager);

    claim.setEmployee(employee);
    claim.setReviewer(manager);

    when(claimRepository.findById(1L)).thenReturn(Optional.of(claim));
    when(claimRepository.save(any(Claim.class))).thenReturn(claim);

    var result = claimService.rejectClaim(1L, 2L, "reject");

    assertEquals(ClaimStatus.REJECTED, result.getStatus());
}


// ================= TEST 7 =================
@Test
void getAllClaims_success() {

    Claim claim = new Claim();
    claim.setId(1L);

    claim.setEmployee(employee);
    claim.setReviewer(manager);

    when(claimRepository.findAll()).thenReturn(List.of(claim));

    var result = claimService.getAllClaims();

    assertEquals(1, result.size());
}


// ================= TEST 8 =================
@Test
void getClaimsByReviewer_success() {

    Claim claim = new Claim();
    claim.setId(1L);

    claim.setEmployee(employee);
    claim.setReviewer(manager);

    when(claimRepository.findByReviewerId(2L)).thenReturn(List.of(claim));

    var result = claimService.getClaimsByReviewer(2L);

    assertEquals(1, result.size());
}

@Test
void submitClaim_adminFallback() {
    ClaimRequestDTO dto = new ClaimRequestDTO();
    dto.setAmount(100.0);
    dto.setDate(LocalDate.now());
    dto.setDescription("Food");

    User employeeNoManager = new User();
    employeeNoManager.setId(1L);
    employeeNoManager.setManager(null);

    User admin = new User();
    admin.setId(99L);
    admin.setRole(Role.ADMIN);

    when(userRepository.findById(1L)).thenReturn(Optional.of(employeeNoManager));
    when(userRepository.findAll()).thenReturn(List.of(admin));
    when(claimRepository.save(any(Claim.class))).thenAnswer(i -> i.getArgument(0));

    var res = claimService.submitClaim(dto, 1L);

    assertNotNull(res);
    verify(claimRepository).save(any());
}

@Test
void approveClaim_notFound() {
    when(claimRepository.findById(1L)).thenReturn(Optional.empty());

    assertThrows(ResourceNotFoundException.class, () ->
        claimService.approveClaim(1L, 2L, "ok")
    );
}

@Test
void rejectClaim_alreadyProcessed() {
    Claim claim = new Claim();
    claim.setId(1L);
    claim.setStatus(ClaimStatus.APPROVED);
    claim.setReviewer(manager);
    claim.setEmployee(employee);

    when(claimRepository.findById(1L)).thenReturn(Optional.of(claim));

    assertThrows(BadRequestException.class, () ->
        claimService.rejectClaim(1L, 2L, "no")
    );
}

@Test
void submitClaim_adminNotFound() {

    ClaimRequestDTO dto = new ClaimRequestDTO();
    dto.setAmount(100.0);
    dto.setDate(LocalDate.now());
    dto.setDescription("Food");

    User emp = new User();
    emp.setId(1L);
    emp.setManager(null);

    when(userRepository.findById(1L)).thenReturn(Optional.of(emp));
    when(userRepository.findAll()).thenReturn(List.of()); // ❌ no admin

    assertThrows(ResourceNotFoundException.class, () -> {
        claimService.submitClaim(dto, 1L);
    });
}

@Test
void rejectClaim_wrongReviewer() {

    Claim claim = new Claim();
    claim.setId(1L);
    claim.setStatus(ClaimStatus.SUBMITTED);
    claim.setEmployee(employee);
    claim.setReviewer(manager);

    when(claimRepository.findById(1L)).thenReturn(Optional.of(claim));

    assertThrows(BadRequestException.class, () -> {
        claimService.rejectClaim(1L, 999L, "no");
    });
}

@Test
void getAllClaims_empty() {

    when(claimRepository.findAll()).thenReturn(List.of());

    var res = claimService.getAllClaims();

    assertEquals(0, res.size());
}

@Test
void approveClaim_nullComment() {

    Claim claim = new Claim();
    claim.setId(1L);
    claim.setStatus(ClaimStatus.SUBMITTED);
    claim.setEmployee(employee);
    claim.setReviewer(manager);

    when(claimRepository.findById(1L)).thenReturn(Optional.of(claim));
    when(claimRepository.save(any())).thenReturn(claim);

    var res = claimService.approveClaim(1L, 2L, null);

    assertNotNull(res);
}
}