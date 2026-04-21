package com.reimbursement.backend.entity;

import com.reimbursement.backend.enums.Role;
import jakarta.persistence.*;
import lombok.*;
// using lombok to reduce boilerplate code for getters, setters, constructors etc.

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
    @Column(nullable = false)
    private String name;

    @Column(nullable = false , unique = true)
    private String email;

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