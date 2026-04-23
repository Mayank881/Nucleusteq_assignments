package com.reimbursement.backend.service;

import com.reimbursement.backend.entity.Claim;
import com.reimbursement.backend.entity.User;
import com.reimbursement.backend.enums.ClaimStatus;
import com.reimbursement.backend.repository.ClaimRepository;
import com.reimbursement.backend.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

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
    public Claim submitClaim(Claim claim, Long employeeId) {

        User employee = userRepository.findById(employeeId).orElse(null);

        if (employee != null) {

            // set employee
            claim.setEmployee(employee);

            // default status
            claim.setStatus(ClaimStatus.SUBMITTED);

            // assign reviewer
            if (employee.getManager() != null) {
                claim.setReviewer(employee.getManager());
            } else {
                // assign admin if no manager
                User admin = userRepository.findAll()
                        .stream()
                        .filter(u -> u.getRole().name().equals("ADMIN"))
                        .findFirst()
                        .orElse(null);

                claim.setReviewer(admin);
            }

            return claimRepository.save(claim);
        }

        return null;
    }

    /**
     * get all claims
     */
    public List<Claim> getAllClaims() {
        return claimRepository.findAll();
    }

    /**
     * approve claim
     */
    public Claim approveClaim(Long claimId) {

        Claim claim = claimRepository.findById(claimId).orElse(null);

        if (claim != null) {
            claim.setStatus(ClaimStatus.APPROVED);
            return claimRepository.save(claim);
        }

        return null;
    }

    /**
     * reject claim
     */
    public Claim rejectClaim(Long claimId) {

        Claim claim = claimRepository.findById(claimId).orElse(null);

        if (claim != null) {
            claim.setStatus(ClaimStatus.REJECTED);
            return claimRepository.save(claim);
        }

        return null;
    }
}