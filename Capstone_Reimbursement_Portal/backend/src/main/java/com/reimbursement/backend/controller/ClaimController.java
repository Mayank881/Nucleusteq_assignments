
package com.reimbursement.backend.controller;

import com.reimbursement.backend.dto.ApiResponse;
import com.reimbursement.backend.dto.ClaimRequestDTO;
import com.reimbursement.backend.dto.ClaimResponseDTO;
import com.reimbursement.backend.service.ClaimService;
import com.reimbursement.backend.constants.Messages;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;

import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;

import java.util.List;

/**
 * handles claim APIs
 */
@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/claims")
public class ClaimController {

    @Autowired
    private ClaimService claimService;

    /**
     * submit a claim
     */
    @PostMapping("/{employeeId}")
    public ResponseEntity<ApiResponse<ClaimResponseDTO>> submitClaim(
            @RequestBody ClaimRequestDTO requestDTO,
            @PathVariable Long employeeId) {

        ClaimResponseDTO claim = claimService.submitClaim(requestDTO, employeeId);

        return ResponseEntity.status(HttpStatus.CREATED)
                .body(new ApiResponse<>(true, Messages.CLAIM_SUBMITTED, claim));
    }

    /**
     * get all claims
     */
    @GetMapping
    public ResponseEntity<ApiResponse<List<ClaimResponseDTO>>> getAllClaims() {

        List<ClaimResponseDTO> claims = claimService.getAllClaims();

        return ResponseEntity.ok(
                new ApiResponse<>(true, Messages.CLAIMS_FETCHED, claims)
        );
    }

    /**
     * approve claim
     */
    @PutMapping("/{id}/approve")
    public ResponseEntity<ApiResponse<ClaimResponseDTO>> approveClaim(
            @PathVariable Long id,
            @RequestParam Long reviewerId) {

        ClaimResponseDTO claim = claimService.approveClaim(id, reviewerId);

        return ResponseEntity.ok(
                new ApiResponse<>(true, Messages.CLAIM_APPROVED, claim)
        );
    }

    /**
     * reject claim
     */
    @PutMapping("/{id}/reject")
    public ResponseEntity<ApiResponse<ClaimResponseDTO>> rejectClaim(
            @PathVariable Long id,
            @RequestParam Long reviewerId) {

        ClaimResponseDTO claim = claimService.rejectClaim(id, reviewerId);

        return ResponseEntity.ok(
                new ApiResponse<>(true, Messages.CLAIM_REJECTED, claim)
        );
    }
}
