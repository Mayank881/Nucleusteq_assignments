package com.reimbursement.backend.constants;

/**
 * holds all application messages
 */
public class Messages {

    // user
    public static final String USER_NOT_FOUND = "User not found";
    public static final String EMPLOYEE_NOT_FOUND = "Employee not found";
    public static final String MANAGER_NOT_FOUND = "Manager not found";
    public static final String EMAIL_EXISTS = "Email already exists";
    public static final String INVALID_EMAIL_DOMAIN = "Invalid email domain";

    // claim
    public static final String CLAIM_NOT_FOUND = "Claim not found";
    public static final String CLAIM_ALREADY_PROCESSED = "Claim already processed";
    public static final String UNAUTHORIZED_REVIEWER = "Only assigned reviewer can perform this action";

    // success
    public static final String USER_CREATED = "User created successfully";
    public static final String USERS_FETCHED = "Users fetched successfully";
    public static final String MANAGER_ASSIGNED = "Manager assigned successfully";
    public static final String EMPLOYEE_ASSIGNED = "Employee assigned successfully";
    // claim success messages
    public static final String CLAIM_SUBMITTED = "Claim submitted successfully";
    public static final String CLAIMS_FETCHED = "Claims fetched successfully";
    public static final String CLAIM_APPROVED = "Claim approved successfully";
    public static final String CLAIM_REJECTED = "Claim rejected successfully";
}

