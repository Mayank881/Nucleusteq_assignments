
package com.reimbursement.backend.controller;

import com.reimbursement.backend.dto.ApiResponse;
import com.reimbursement.backend.dto.ClaimActionDTO;
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
         * get claims - all or by reviewer
         */
        @GetMapping
        public ResponseEntity<ApiResponse<List<ClaimResponseDTO>>> getClaims(
                        @RequestParam(required = false) Long reviewerId) {

                List<ClaimResponseDTO> claims;

                if (reviewerId != null) {
                        claims = claimService.getClaimsByReviewer(reviewerId);
                } else {
                        claims = claimService.getAllClaims();
                }

                return ResponseEntity.ok(
                                new ApiResponse<>(true, Messages.CLAIMS_FETCHED, claims));
        }

        /**
         * approve claim
         */
        @PutMapping("/{id}/approve")
        public ResponseEntity<ApiResponse<ClaimResponseDTO>> approveClaim(
                        @PathVariable Long id,
                        @RequestParam Long reviewerId,
                        @RequestBody ClaimActionDTO request) {

                ClaimResponseDTO response = claimService.approveClaim(id, reviewerId, request.getComment());

                return ResponseEntity.ok(
                                new ApiResponse<>(true, "Claim approved successfully", response));
        }

        /**
         * reject claim
         */
        @PutMapping("/{id}/reject")
        public ResponseEntity<ApiResponse<ClaimResponseDTO>> rejectClaim(
                        @PathVariable Long id,
                        @RequestParam Long reviewerId,
                        @RequestBody ClaimActionDTO request) {

                ClaimResponseDTO response = claimService.rejectClaim(id, reviewerId, request.getComment());

                return ResponseEntity.ok(
                                new ApiResponse<>(true, "Claim rejected successfully", response));
        }
}
