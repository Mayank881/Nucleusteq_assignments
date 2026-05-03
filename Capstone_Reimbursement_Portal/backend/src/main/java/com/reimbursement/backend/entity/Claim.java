package com.reimbursement.backend.entity;

import com.reimbursement.backend.enums.ClaimStatus;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDate;

// this class is for claim table
@Entity
@Table(name = "claims")

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor

public class Claim {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // claim amount that employee is asking for reimbursement
    @Column(nullable = false)
    private Double amount;

    @Column(nullable = false)
    private LocalDate date;

    // desc of claim like travel or hotel expenses
    @Column(nullable = false)
    private String description;

    // status of claim
    @Enumerated(EnumType.STRING)
    private ClaimStatus status;

    // employee who created claim
    @ManyToOne
    @JoinColumn(name = "employee_id")
    private User employee;

    // manager/admin who will review
    @ManyToOne
    @JoinColumn(name = "reviewer_id")
    private User reviewer;

    @Column(length = 500)
    private String reviewerComment;

}