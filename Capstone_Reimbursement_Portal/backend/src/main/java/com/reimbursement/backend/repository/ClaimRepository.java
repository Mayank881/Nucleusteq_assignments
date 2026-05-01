package com.reimbursement.backend.repository;

import com.reimbursement.backend.entity.Claim;
import org.springframework.data.jpa.repository.JpaRepository;

// handles claim DB operationsn like saving, fetching, updating claims
public interface ClaimRepository extends JpaRepository<Claim, Long> {

}