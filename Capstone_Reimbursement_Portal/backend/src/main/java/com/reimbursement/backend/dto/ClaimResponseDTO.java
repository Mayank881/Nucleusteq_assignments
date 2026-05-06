package com.reimbursement.backend.dto;

import com.reimbursement.backend.enums.ClaimStatus;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDate;

/**
 * DTO for claim response
 */
@Getter
@Setter
public class ClaimResponseDTO {

    private Long id;
    private Double amount;
    private String description;
    private ClaimStatus status;
    private LocalDate date;
    private Long employeeId;
    private Long reviewerId;
    private String reviewerComment;

}

