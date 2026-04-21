package com.reimbursement.backend.repository;

import com.reimbursement.backend.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;

// handles user DB operations 
public interface UserRepository extends JpaRepository<User, Long> {

}
git add .
git commit -m "Day 2: Completed repository layer for User and Claim"
git push