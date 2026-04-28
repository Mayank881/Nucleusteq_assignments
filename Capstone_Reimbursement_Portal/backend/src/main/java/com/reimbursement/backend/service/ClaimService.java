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

// handles claim logic
@Service
public class ClaimService {

    @Autowired
    private ClaimRepository claimRepository;

    @Autowired
    private UserRepository userRepository;

    /**
     * submit a claim
     */
    public ClaimResponseDTO submitClaim(ClaimRequestDTO requestDTO, Long employeeId) {

        User employee = userRepository.findById(employeeId)
                .orElseThrow(() -> new ResourceNotFoundException(Messages.EMPLOYEE_NOT_FOUND));

        Claim claim = ClaimMapper.toEntity(requestDTO);

        claim.setStatus(ClaimStatus.SUBMITTED);
        claim.setEmployee(employee);

        // assign reviewer
        if (employee.getManager() != null) {
            claim.setReviewer(employee.getManager());
        } else {
            User admin = userRepository.findAll()
                    .stream()
                    .filter(u -> u.getRole().name().equals("ADMIN"))
                    .findFirst()
                    .orElseThrow(() -> new ResourceNotFoundException(Messages.USER_NOT_FOUND));

            claim.setReviewer(admin);
        }

        Claim savedClaim = claimRepository.save(claim);

        return ClaimMapper.toDTO(savedClaim);
    }

    /**
     * get all claims
     */
    public List<ClaimResponseDTO> getAllClaims() {

        List<Claim> claims = claimRepository.findAll();
        List<ClaimResponseDTO> list = new ArrayList<>();

        for (Claim c : claims) {
            list.add(ClaimMapper.toDTO(c));
        }

        return list;
    }

    /**
     * approve claim
     */
    public ClaimResponseDTO approveClaim(Long claimId, Long reviewerId) {

        Claim claim = claimRepository.findById(claimId)
                .orElseThrow(() -> new ResourceNotFoundException(Messages.CLAIM_NOT_FOUND));

        // check correct reviewer
        if (!claim.getReviewer().getId().equals(reviewerId)) {
            throw new BadRequestException(Messages.UNAUTHORIZED_REVIEWER);
        }

        // prevent re-processing
        if (claim.getStatus() != ClaimStatus.SUBMITTED) {
            throw new BadRequestException(Messages.CLAIM_ALREADY_PROCESSED);
        }

        claim.setStatus(ClaimStatus.APPROVED);

        Claim saved = claimRepository.save(claim);

        return ClaimMapper.toDTO(saved);
    }

    /**
     * reject claim
     */
    public ClaimResponseDTO rejectClaim(Long claimId, Long reviewerId) {

        Claim claim = claimRepository.findById(claimId)
                .orElseThrow(() -> new ResourceNotFoundException(Messages.CLAIM_NOT_FOUND));

        // check correct reviewer
        if (!claim.getReviewer().getId().equals(reviewerId)) {
            throw new BadRequestException(Messages.UNAUTHORIZED_REVIEWER);
        }

        // prevent re-processing
        if (claim.getStatus() != ClaimStatus.SUBMITTED) {
            throw new BadRequestException(Messages.CLAIM_ALREADY_PROCESSED);
        }

        claim.setStatus(ClaimStatus.REJECTED);

        Claim saved = claimRepository.save(claim);

        return ClaimMapper.toDTO(saved);
    }
}

