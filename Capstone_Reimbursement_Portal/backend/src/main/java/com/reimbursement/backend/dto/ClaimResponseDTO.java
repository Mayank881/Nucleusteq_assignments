package com.reimbursement.backend.dto;

import com.reimbursement.backend.enums.ClaimStatus;

/**
 * DTO for claim response
 */
public class ClaimResponseDTO {

    private Long id;
    private Double amount;
    private String description;
    private ClaimStatus status;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Double getAmount() {
        return amount;
    }

    public void setAmount(Double amount) {
        this.amount = amount;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public ClaimStatus getStatus() {
        return status;
    }

    public void setStatus(ClaimStatus status) {
        this.status = status;
    }
}