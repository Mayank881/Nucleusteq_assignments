package com.reimbursement.backend.service;

import com.reimbursement.backend.dto.ClaimRequestDTO;
import com.reimbursement.backend.dto.ClaimResponseDTO;
import com.reimbursement.backend.entity.Claim;
import com.reimbursement.backend.entity.User;
import com.reimbursement.backend.enums.ClaimStatus;
import com.reimbursement.backend.exception.ResourceNotFoundException;
import com.reimbursement.backend.repository.ClaimRepository;
import com.reimbursement.backend.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

// handles claim logic
@Service
public class ClaimService {

    @Autowired
    private ClaimRepository claimRepository;

    @Autowired
    private UserRepository userRepository;

    /**
     * submit a claim
     */
    public ClaimResponseDTO submitClaim(ClaimRequestDTO requestDTO, Long employeeId) {

        User employee = userRepository.findById(employeeId)
                .orElseThrow(() -> new ResourceNotFoundException("Employee not found"));

        Claim claim = new Claim();
        claim.setAmount(requestDTO.getAmount());
        claim.setDate(requestDTO.getDate());
        claim.setDescription(requestDTO.getDescription());
        claim.setStatus(ClaimStatus.SUBMITTED);
        claim.setEmployee(employee);

        // assign reviewer
        if (employee.getManager() != null) {
            claim.setReviewer(employee.getManager());
        } else {
            User admin = userRepository.findAll()
                    .stream()
                    .filter(u -> u.getRole().name().equals("ADMIN"))
                    .findFirst()
                    .orElseThrow(() -> new ResourceNotFoundException("Admin not found"));

            claim.setReviewer(admin);
        }

        Claim savedClaim = claimRepository.save(claim);

        ClaimResponseDTO dto = new ClaimResponseDTO();
        dto.setId(savedClaim.getId());
        dto.setAmount(savedClaim.getAmount());
        dto.setDescription(savedClaim.getDescription());
        dto.setStatus(savedClaim.getStatus());

        return dto;
    }

    /**
     * get all claims
     */
    public List<ClaimResponseDTO> getAllClaims() {

        List<Claim> claims = claimRepository.findAll();
        List<ClaimResponseDTO> list = new java.util.ArrayList<>();

        for (Claim c : claims) {
            ClaimResponseDTO dto = new ClaimResponseDTO();
            dto.setId(c.getId());
            dto.setAmount(c.getAmount());
            dto.setDescription(c.getDescription());
            dto.setStatus(c.getStatus());

            list.add(dto);
        }

        return list;
    }

    /**
     * approve claim
     */
    public ClaimResponseDTO approveClaim(Long claimId) {

        Claim claim = claimRepository.findById(claimId)
                .orElseThrow(() -> new ResourceNotFoundException("Claim not found"));

        claim.setStatus(ClaimStatus.APPROVED);

        Claim saved = claimRepository.save(claim);

        ClaimResponseDTO dto = new ClaimResponseDTO();
        dto.setId(saved.getId());
        dto.setAmount(saved.getAmount());
        dto.setDescription(saved.getDescription());
        dto.setStatus(saved.getStatus());

        return dto;
    }

    /**
     * reject claim
     */
    public ClaimResponseDTO rejectClaim(Long claimId) {

        Claim claim = claimRepository.findById(claimId)
                .orElseThrow(() -> new ResourceNotFoundException("Claim not found"));

        claim.setStatus(ClaimStatus.REJECTED);

        Claim saved = claimRepository.save(claim);

        ClaimResponseDTO dto = new ClaimResponseDTO();
        dto.setId(saved.getId());
        dto.setAmount(saved.getAmount());
        dto.setDescription(saved.getDescription());
        dto.setStatus(saved.getStatus());

        return dto;
    }
}