package com.reimbursement.backend.controller;

import com.reimbursement.backend.entity.Claim;
import com.reimbursement.backend.service.ClaimService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

// handles claim APIs
@RestController
@RequestMapping("/claims")
public class ClaimController {

    @Autowired
    private ClaimService claimService;

    /**
     * submit a claim
     */
    @PostMapping("/{employeeId}")
    public Claim submitClaim(@RequestBody Claim claim,
                             @PathVariable Long employeeId) {

        return claimService.submitClaim(claim, employeeId);
    }

    /**
     * get all claims
     */
    @GetMapping
    public List<Claim> getAllClaims() {
        return claimService.getAllClaims();
    }

    /**
     * approve claim
     */
    @PutMapping("/approve/{claimId}")
    public Claim approveClaim(@PathVariable Long claimId) {
        return claimService.approveClaim(claimId);
    }

    /**
     * reject claim
     */
    @PutMapping("/reject/{claimId}")
    public Claim rejectClaim(@PathVariable Long claimId) {
        return claimService.rejectClaim(claimId);
    }
}