package com.reimbursement.backend.config;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.security.Keys;

import org.springframework.stereotype.Component;

import java.security.Key;
import java.util.Date;

@Component
public class JwtUtil {

    // generate secure key (must be at least 256 bits)
    private final Key SECRET_KEY = Keys.hmacShaKeyFor(
            "mysecretkeymysecretkeymysecretkey12345".getBytes()
    );

    //  Generate Token
    public String generateToken(String email) {
        return Jwts.builder()
                .setSubject(email)
                .setIssuedAt(new Date())
                .setExpiration(new Date(System.currentTimeMillis() + 1000 * 60 * 60)) 
                .signWith(SECRET_KEY)   
                .compact();
    }

    // Extract Email
    public String extractEmail(String token) {
        return extractClaims(token).getSubject();
    }

    // Extract Claims
    public Claims extractClaims(String token) {
        return Jwts.parserBuilder()  
                .setSigningKey(SECRET_KEY)
                .build()
                .parseClaimsJws(token)
                .getBody();
    }
}