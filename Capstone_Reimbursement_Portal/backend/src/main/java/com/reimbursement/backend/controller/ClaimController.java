package com.reimbursement.backend.controller;

import com.reimbursement.backend.dto.ApiResponse;
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
    public ApiResponse<ClaimResponseDTO> submitClaim(@RequestBody ClaimRequestDTO requestDTO,
            @PathVariable Long employeeId) {

        ClaimResponseDTO claim = claimService.submitClaim(requestDTO, employeeId);

        return new ApiResponse<>(true, "Claim submitted successfully", claim);
    }

    /**
     * get all claims
     */
    @GetMapping
    public ApiResponse<List<ClaimResponseDTO>> getAllClaims() {

        List<ClaimResponseDTO> claims = claimService.getAllClaims();

        return new ApiResponse<>(true, "Claims fetched successfully", claims);
    }

    /**
     * approve claim
     */
    @PutMapping("/{id}/approve")
    public ApiResponse<ClaimResponseDTO> approveClaim(@PathVariable Long id,
            @RequestParam Long reviewerId) {

        ClaimResponseDTO claim = claimService.approveClaim(id, reviewerId);

        return new ApiResponse<>(true, "Claim approved successfully", claim);
    }

    /**
     * reject claim
     */
    @PutMapping("/{id}/reject")
    public ApiResponse<ClaimResponseDTO> rejectClaim(@PathVariable Long id,
            @RequestParam Long reviewerId) {

        ClaimResponseDTO claim = claimService.rejectClaim(id, reviewerId);

        return new ApiResponse<>(true, "Claim rejected successfully", claim);
    }
}