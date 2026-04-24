package com.reimbursement.backend.entity;

import com.reimbursement.backend.enums.Role;
import jakarta.persistence.*;
import lombok.*;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;

// this class represents users table
@Entity
@Table(name = "users")

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor

public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // basic user info

    @NotBlank(message = "Name is required")
    @Column(nullable = false)
    private String name;

    @NotBlank(message = "Email is required")
    @Email(message = "Invalid email format")
    @Column(nullable = false, unique = true)
    private String email;

    @NotBlank(message = "Password is required")
    @Column(nullable = false)
    private String password;

    // role like admin, manager, employee
    @Enumerated(EnumType.STRING)
    private Role role;

    // many employees -> one manager
    @ManyToOne
    @JoinColumn(name = "manager_id")
    private User manager;

}