
package com.reimbursement.backend.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import com.reimbursement.backend.dto.ApiResponse;

import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.MethodArgumentNotValidException;


/**
 * handles all exceptions globally
 */
@RestControllerAdvice
public class GlobalExceptionHandler {

    /**
     * handles cases when requested resource is not found
     */
    @ExceptionHandler(ResourceNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ApiResponse<Object> handleNotFound(ResourceNotFoundException ex) {

        return new ApiResponse<>(false, ex.getMessage(), null);
    }

    /**
     * handles bad request exceptions like invalid input or duplicate data
     */
    @ExceptionHandler(BadRequestException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ApiResponse<Object> handleBadRequest(BadRequestException ex) {

        return new ApiResponse<>(false, ex.getMessage(), null);
    }

    /**
     * handles validation errors (DTO validation)
     */
    @ExceptionHandler(MethodArgumentNotValidException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ApiResponse<Object> handleValidation(MethodArgumentNotValidException ex) {

        String msg = ex.getBindingResult()
                .getFieldErrors()
                .get(0)
                .getDefaultMessage();

        return new ApiResponse<>(false, msg, null);
    }

    /**
     * handles unexpected server errors
     */
    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ApiResponse<Object> handleGeneral(Exception ex) {

        return new ApiResponse<>(false, "Something went wrong", null);
    }
}
