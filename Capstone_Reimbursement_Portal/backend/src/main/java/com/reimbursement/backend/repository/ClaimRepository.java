package com.reimbursement.backend.repository;

import com.reimbursement.backend.entity.User;
import com.reimbursement.backend.entity.Claim;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ClaimRepository extends JpaRepository<Claim, Long> {

    void deleteByEmployee(User user);
    void deleteByReviewer(User user);
    List<Claim> findByReviewerId(Long reviewerId);
}