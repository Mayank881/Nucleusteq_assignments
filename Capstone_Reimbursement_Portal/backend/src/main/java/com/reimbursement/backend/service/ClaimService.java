package com.reimbursement.backend.service;

import com.reimbursement.backend.dto.ClaimRequestDTO;
import com.reimbursement.backend.dto.ClaimResponseDTO;
import com.reimbursement.backend.entity.Claim;
import com.reimbursement.backend.entity.User;
import com.reimbursement.backend.enums.ClaimStatus;
import com.reimbursement.backend.exception.ResourceNotFoundException;
import com.reimbursement.backend.exception.BadRequestException;
import com.reimbursement.backend.mapper.ClaimMapper;
import com.reimbursement.backend.repository.ClaimRepository;
import com.reimbursement.backend.repository.UserRepository;
import com.reimbursement.backend.constants.Messages;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

// handles claim logic
@Service
public class ClaimService {

    private static final Logger logger = LoggerFactory.getLogger(ClaimService.class);

    @Autowired
    private ClaimRepository claimRepository;

    @Autowired
    private UserRepository userRepository;

    /**
     * submit a claim
     */
    public ClaimResponseDTO submitClaim(ClaimRequestDTO requestDTO, Long employeeId) {

        logger.info("START: Submit claim | employeeId={}", employeeId);

        User employee = userRepository.findById(employeeId)
                .orElseThrow(() -> {
                    logger.error("Employee not found | employeeId={}", employeeId);
                    return new ResourceNotFoundException(Messages.EMPLOYEE_NOT_FOUND);
                });

        Claim claim = ClaimMapper.toEntity(requestDTO);
        logger.info("Claim mapped from DTO");

        claim.setStatus(ClaimStatus.SUBMITTED);
        claim.setEmployee(employee);

        // assign reviewer
        if (employee.getManager() != null) {
            claim.setReviewer(employee.getManager());
            logger.info("Reviewer assigned (manager) | reviewerId={}", employee.getManager().getId());
        } else {
            User admin = userRepository.findAll()
                    .stream()
                    .filter(u -> u.getRole().name().equals("ADMIN"))
                    .findFirst()
                    .orElseThrow(() -> {
                        logger.error("Admin not found for fallback reviewer");
                        return new ResourceNotFoundException(Messages.USER_NOT_FOUND);
                    });

            claim.setReviewer(admin);
            logger.info("Reviewer assigned (admin fallback) | reviewerId={}", admin.getId());
        }

        Claim savedClaim = claimRepository.save(claim);

        logger.info("SUCCESS: Claim created | claimId={} | employeeId={}",
                savedClaim.getId(), employeeId);

        //  AUDIT LOG
        logger.info("AUDIT: User {} created claim {}", employeeId, savedClaim.getId());

        return ClaimMapper.toDTO(savedClaim);
    }

    /**
     * get all claims
     */
    public List<ClaimResponseDTO> getAllClaims() {

        logger.info("Fetching all claims");

        List<Claim> claims = claimRepository.findAll();
        List<ClaimResponseDTO> list = new ArrayList<>();

        for (Claim c : claims) {
            list.add(ClaimMapper.toDTO(c));
        }

        logger.info("SUCCESS: Total claims fetched | count={}", list.size());

        return list;
    }

    /**
     * approve claim
     */
    public ClaimResponseDTO approveClaim(Long claimId, Long reviewerId, String comment) {

        logger.info("START: Approve claim | claimId={} | reviewerId={}", claimId, reviewerId);

        Claim claim = claimRepository.findById(claimId)
                .orElseThrow(() -> {
                    logger.error("Claim not found | claimId={}", claimId);
                    return new ResourceNotFoundException(Messages.CLAIM_NOT_FOUND);
                });

        if (!claim.getReviewer().getId().equals(reviewerId)) {
            logger.warn("Unauthorized reviewer attempt | claimId={} | reviewerId={}", claimId, reviewerId);
            throw new BadRequestException(Messages.UNAUTHORIZED_REVIEWER);
        }

        if (claim.getStatus() != ClaimStatus.SUBMITTED) {
            logger.warn("Claim already processed | claimId={} | status={}", claimId, claim.getStatus());
            throw new BadRequestException(Messages.CLAIM_ALREADY_PROCESSED);
        }

        claim.setStatus(ClaimStatus.APPROVED);
        claim.setReviewerComment(comment);

        Claim saved = claimRepository.save(claim);

        logger.info("SUCCESS: Claim approved | claimId={} | reviewerId={}", claimId, reviewerId);

        //  AUDIT LOG
        logger.info("AUDIT: Reviewer {} approved claim {}", reviewerId, claimId);

        return ClaimMapper.toDTO(saved);
    }

    /**
     * reject claim
     */
    public ClaimResponseDTO rejectClaim(Long claimId, Long reviewerId, String comment) {

        logger.info("START: Reject claim | claimId={} | reviewerId={}", claimId, reviewerId);

        Claim claim = claimRepository.findById(claimId)
                .orElseThrow(() -> {
                    logger.error("Claim not found | claimId={}", claimId);
                    return new ResourceNotFoundException(Messages.CLAIM_NOT_FOUND);
                });

        if (!claim.getReviewer().getId().equals(reviewerId)) {
            logger.warn("Unauthorized reviewer attempt | claimId={} | reviewerId={}", claimId, reviewerId);
            throw new BadRequestException(Messages.UNAUTHORIZED_REVIEWER);
        }

        if (claim.getStatus() != ClaimStatus.SUBMITTED) {
            logger.warn("Claim already processed | claimId={} | status={}", claimId, claim.getStatus());
            throw new BadRequestException(Messages.CLAIM_ALREADY_PROCESSED);
        }

        claim.setStatus(ClaimStatus.REJECTED);
        claim.setReviewerComment(comment);

        Claim saved = claimRepository.save(claim);

        logger.info("SUCCESS: Claim rejected | claimId={} | reviewerId={}", claimId, reviewerId);

        // AUDIT LOG
        logger.info("AUDIT: Reviewer {} rejected claim {}", reviewerId, claimId);

        return ClaimMapper.toDTO(saved);
    }

    /**
     * get claims by reviewer
     */
    public List<ClaimResponseDTO> getClaimsByReviewer(Long reviewerId) {

        logger.info("Fetching claims for reviewerId={}", reviewerId);

        List<Claim> claims = claimRepository.findByReviewerId(reviewerId);
        List<ClaimResponseDTO> list = new ArrayList<>();

        for (Claim c : claims) {
            list.add(ClaimMapper.toDTO(c));
        }

        logger.info("SUCCESS: Claims fetched for reviewer | reviewerId={} | count={}",
                reviewerId, list.size());

        return list;
    }
}