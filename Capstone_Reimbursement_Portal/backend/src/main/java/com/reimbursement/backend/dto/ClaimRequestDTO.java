package com.reimbursement.backend.dto;

import java.time.LocalDate;

/**
 * DTO for claim input
 */
public class ClaimRequestDTO {

    private Double amount;
    private LocalDate date;
    private String description;

    public Double getAmount() {
        return amount;
    }

    public void setAmount(Double amount) {
        this.amount = amount;
    }

    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
}