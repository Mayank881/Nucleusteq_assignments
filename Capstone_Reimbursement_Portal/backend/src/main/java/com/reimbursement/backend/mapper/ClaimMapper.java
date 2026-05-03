package com.reimbursement.backend.mapper;

import com.reimbursement.backend.dto.ClaimRequestDTO;
import com.reimbursement.backend.dto.ClaimResponseDTO;
import com.reimbursement.backend.entity.Claim;

/**
 * handles mapping between Claim and DTOs
 */
public class ClaimMapper {

    public static Claim toEntity(ClaimRequestDTO dto) {

        Claim claim = new Claim();
        claim.setAmount(dto.getAmount());
        claim.setDate(dto.getDate());
        claim.setDescription(dto.getDescription());

        return claim;
    }

    public static ClaimResponseDTO toDTO(Claim claim) {

        ClaimResponseDTO dto = new ClaimResponseDTO();
        dto.setId(claim.getId());
        dto.setAmount(claim.getAmount());
        dto.setDate(claim.getDate());
        dto.setDescription(claim.getDescription());
        dto.setStatus(claim.getStatus());
        dto.setEmployeeId(claim.getEmployee().getId());
        dto.setReviewerId(claim.getReviewer().getId());
        dto.setReviewerComment(claim.getReviewerComment());

        return dto;
    }
}