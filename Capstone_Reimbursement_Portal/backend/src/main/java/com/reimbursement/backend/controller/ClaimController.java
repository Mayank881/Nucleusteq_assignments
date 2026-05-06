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

// LOGGING IMPORTS
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * handles claim APIs
 */
@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/claims")
public class ClaimController {

        private static final Logger logger = LoggerFactory.getLogger(ClaimController.class);

        @Autowired
        private ClaimService claimService;

        /**
         * submit a claim
         */
        @PostMapping("/{employeeId}")
        public ResponseEntity<ApiResponse<ClaimResponseDTO>> submitClaim(
                        @RequestBody ClaimRequestDTO requestDTO,
                        @PathVariable Long employeeId) {

                logger.info("API HIT: Submit Claim | employeeId={}", employeeId);

                try {
                        ClaimResponseDTO claim = claimService.submitClaim(requestDTO, employeeId);

                        logger.info("SUCCESS: Claim submitted | claimId={} | employeeId={}",
                                        claim.getId(), employeeId);

                        return ResponseEntity.status(HttpStatus.CREATED)
                                        .body(new ApiResponse<>(true, Messages.CLAIM_SUBMITTED, claim));

                } catch (Exception e) {
                        logger.error("ERROR: Claim submission failed | employeeId={}", employeeId, e);
                        throw e;
                }
        }

        /**
         * get claims - all or by reviewer
         */
        @GetMapping
        public ResponseEntity<ApiResponse<List<ClaimResponseDTO>>> getClaims(
                        @RequestParam(required = false) Long reviewerId) {

                logger.info("API HIT: Get Claims | reviewerId={}", reviewerId);

                try {
                        List<ClaimResponseDTO> claims;

                        if (reviewerId != null) {
                                logger.info("Fetching claims for reviewerId={}", reviewerId);
                                claims = claimService.getClaimsByReviewer(reviewerId);
                        } else {
                                logger.info("Fetching all claims");
                                claims = claimService.getAllClaims();
                        }

                        logger.info("SUCCESS: Claims fetched | count={}", claims.size());

                        return ResponseEntity.ok(
                                        new ApiResponse<>(true, Messages.CLAIMS_FETCHED, claims));

                } catch (Exception e) {
                        logger.error("ERROR: Failed to fetch claims", e);
                        throw e;
                }
        }

        /**
         * approve claim
         */
        @PutMapping("/{id}/approve")
        public ResponseEntity<ApiResponse<ClaimResponseDTO>> approveClaim(
                        @PathVariable Long id,
                        @RequestParam Long reviewerId,
                        @RequestBody ClaimActionDTO request) {

                logger.info("API HIT: Approve Claim | claimId={} | reviewerId={}", id, reviewerId);

                try {
                        ClaimResponseDTO response = claimService.approveClaim(id, reviewerId,
                                        request.getComment());

                        logger.info("SUCCESS: Claim approved | claimId={} | reviewerId={}",
                                        id, reviewerId);

                        return ResponseEntity.ok(
                                        new ApiResponse<>(true, Messages.CLAIM_APPROVED, response));

                } catch (Exception e) {
                        logger.error("ERROR: Claim approval failed | claimId={} | reviewerId={}",
                                        id, reviewerId, e);
                        throw e;
                }
        }

        /**
         * reject claim
         */
        @PutMapping("/{id}/reject")
        public ResponseEntity<ApiResponse<ClaimResponseDTO>> rejectClaim(
                        @PathVariable Long id,
                        @RequestParam Long reviewerId,
                        @RequestBody ClaimActionDTO request) {

                logger.info("API HIT: Reject Claim | claimId={} | reviewerId={}", id, reviewerId);

                try {
                        ClaimResponseDTO response = claimService.rejectClaim(id, reviewerId,
                                        request.getComment());

                        logger.info("SUCCESS: Claim rejected | claimId={} | reviewerId={}",
                                        id, reviewerId);

                        return ResponseEntity.ok(
                                        new ApiResponse<>(true, Messages.CLAIM_REJECTED, response));

                } catch (Exception e) {
                        logger.error("ERROR: Claim rejection failed | claimId={} | reviewerId={}",
                                        id, reviewerId, e);
                        throw e;
                }
        }
}