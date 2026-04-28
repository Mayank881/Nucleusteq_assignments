
package com.reimbursement.backend.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.MethodArgumentNotValidException;

import java.util.HashMap;
import java.util.Map;

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
    public Map<String, String> handleNotFound(ResourceNotFoundException ex) {

        Map<String, String> response = new HashMap<>();
        response.put("message", ex.getMessage());

        return response;
    }

    /**
     * handles bad request exceptions like invalid input or duplicate data
     */
    @ExceptionHandler(BadRequestException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public Map<String, String> handleBadRequest(BadRequestException ex) {

        Map<String, String> response = new HashMap<>();
        response.put("message", ex.getMessage());

        return response;
    }

    /**
     * handles validation errors (DTO validation)
     */
    @ExceptionHandler(MethodArgumentNotValidException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public Map<String, String> handleValidation(MethodArgumentNotValidException ex) {

        Map<String, String> response = new HashMap<>();

        String msg = ex.getBindingResult()
                .getFieldErrors()
                .get(0)
                .getDefaultMessage();

        response.put("message", msg);

        return response;
    }

    /**
     * handles unexpected server errors
     */
    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public Map<String, String> handleGeneral(Exception ex) {

        Map<String, String> response = new HashMap<>();
        response.put("message", "Something went wrong");

        return response;
    }
}

