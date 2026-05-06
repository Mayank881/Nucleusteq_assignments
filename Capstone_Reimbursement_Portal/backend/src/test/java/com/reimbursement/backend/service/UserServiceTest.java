package com.reimbursement.backend.service;

import com.reimbursement.backend.entity.User;
import com.reimbursement.backend.enums.Role;
import com.reimbursement.backend.repository.ClaimRepository;
import com.reimbursement.backend.repository.UserRepository;
import com.reimbursement.backend.dto.UserRequestDTO;

import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageImpl;
import org.springframework.data.domain.PageRequest;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.anyLong;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.Mockito.*;

class UserServiceTest {

    @Mock
    private PasswordEncoder passwordEncoder;

    @Mock
    private UserRepository userRepository;

    @Mock
    private ClaimRepository claimRepository;

    @InjectMocks
    private UserService userService;

    public UserServiceTest() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    void getAllUsers_success() {

        User u = new User();
        u.setId(1L);

        Page<User> page = new PageImpl<>(List.of(u));

        when(userRepository.findAll(any(PageRequest.class))).thenReturn(page);

        var res = userService.getAllUsers(0, 5);

        assertNotNull(res);
        assertTrue(res.containsKey("content"));
    }

    @Test
    void createUser_success() {

        UserRequestDTO dto = new UserRequestDTO();
        dto.setName("test");
        dto.setEmail("test@company.com");
        dto.setPassword("1234");
        dto.setRole(Role.EMPLOYEE);

        User savedUser = new User();
        savedUser.setId(1L);

        when(passwordEncoder.encode(anyString())).thenReturn("encoded123");
        when(userRepository.save(any())).thenReturn(savedUser);

        var res = userService.createUser(dto);

        assertNotNull(res);
        assertNotNull(res);
    }

    @Test
    void createUser_emailExists() {

        UserRequestDTO dto = new UserRequestDTO();
        dto.setEmail("test@company.com");
        dto.setPassword("1234");
        dto.setRole(Role.EMPLOYEE);

        when(userRepository.existsByEmail(dto.getEmail())).thenReturn(true);

        assertThrows(RuntimeException.class, () -> {
            userService.createUser(dto);
        });
    }

    @Test
    void getAllUsers_empty() {

        Page<User> page = new PageImpl<>(List.of());

        when(userRepository.findAll(any(PageRequest.class))).thenReturn(page);

        var res = userService.getAllUsers(0, 5);

        assertTrue(((List<?>) res.get("content")).isEmpty());
    }

    @Test
    void assignManager_success() {

        User user = new User();
        user.setId(1L);
        user.setRole(Role.EMPLOYEE);

        User manager = new User();
        manager.setId(2L);
        manager.setRole(Role.MANAGER);

        when(userRepository.findById(1L)).thenReturn(Optional.of(user));
        when(userRepository.findById(2L)).thenReturn(Optional.of(manager));

        when(claimRepository.findByEmployeeId(anyLong())).thenReturn(List.of());

        userService.assignManager(1L, 2L);

        assertEquals(manager, user.getManager());
    }

    @Test
    void createUser_nullPassword() {

        UserRequestDTO dto = new UserRequestDTO();
        dto.setEmail("test@company.com");
        dto.setPassword(null);

        when(userRepository.existsByEmail(any())).thenReturn(false);

        assertThrows(Exception.class, () -> {
            userService.createUser(dto);
        });
    }
}