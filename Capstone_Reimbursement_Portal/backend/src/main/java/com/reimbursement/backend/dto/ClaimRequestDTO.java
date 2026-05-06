package com.reimbursement.backend.dto;

import java.time.LocalDate;
import lombok.Getter;
import lombok.Setter;

/**
 * DTO for claim input
 */
@Getter
@Setter
public class ClaimRequestDTO {

    private Double amount;
    private LocalDate date;
    private String description;

}