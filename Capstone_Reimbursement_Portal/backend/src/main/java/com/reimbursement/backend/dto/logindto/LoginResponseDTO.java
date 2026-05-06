package com.reimbursement.backend.dto.logindto;

import lombok.AllArgsConstructor;
import lombok.Getter;

@Getter
@AllArgsConstructor
public class LoginResponseDTO {

    private String token;
    private Long id;       
    private String email;  
    private String role;
}