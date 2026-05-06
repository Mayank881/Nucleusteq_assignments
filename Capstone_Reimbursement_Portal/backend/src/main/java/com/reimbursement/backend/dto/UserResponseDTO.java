package com.reimbursement.backend.dto;

import com.reimbursement.backend.enums.Role;
import lombok.Getter;
import lombok.Setter;
/**
 * DTO for sending user data in response
 */
@Getter
@Setter
public class UserResponseDTO {

    private Long id;
    private String name;
    private String email;
    private Role role;
    private Long managerId;
    private String managerName;
}