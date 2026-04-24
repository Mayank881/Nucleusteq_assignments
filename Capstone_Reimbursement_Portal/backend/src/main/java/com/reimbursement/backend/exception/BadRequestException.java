package com.reimbursement.backend.exception;

/**
 * thrown for invalid request data
 */
public class BadRequestException extends RuntimeException {

    public BadRequestException(String message) {
        super(message);
    }
}