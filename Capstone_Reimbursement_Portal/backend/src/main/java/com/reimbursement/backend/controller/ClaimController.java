package com.reimbursement.backend.controller;

import com.reimbursement.backend.dto.ClaimRequestDTO;
import com.reimbursement.backend.dto.ClaimResponseDTO;
import com.reimbursement.backend.service.ClaimService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * handles claim APIs
 */
@CrossOrigin(origins = {
    "http://localhost:5500",
    "http://127.0.0.1:5500"
})
@RestController
@RequestMapping("/claims")
public class ClaimController {

    @Autowired
    private ClaimService claimService;

    /**
     * submit a claim
     */
    @PostMapping("/{employeeId}")
    public ClaimResponseDTO submitClaim(@RequestBody ClaimRequestDTO requestDTO,
            @PathVariable Long employeeId) {

        return claimService.submitClaim(requestDTO, employeeId);
    }

    /**
     * get all claims
     */
    @GetMapping
    public List<ClaimResponseDTO> getAllClaims() {
        return claimService.getAllClaims();
    }

    /**
     * approve claim
     */
    @PutMapping("/approve/{claimId}")
    public ClaimResponseDTO approveClaim(@PathVariable Long claimId) {
        return claimService.approveClaim(claimId);
    }

    /**
     * reject claim
     */
    @PutMapping("/reject/{claimId}")
    public ClaimResponseDTO rejectClaim(@PathVariable Long claimId) {
        return claimService.rejectClaim(claimId);
    }
}