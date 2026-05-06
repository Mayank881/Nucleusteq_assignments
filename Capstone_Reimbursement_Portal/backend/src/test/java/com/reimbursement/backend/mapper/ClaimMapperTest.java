package com.reimbursement.backend.mapper;

import com.reimbursement.backend.entity.Claim;
import com.reimbursement.backend.entity.User;
import com.reimbursement.backend.enums.ClaimStatus;
import com.reimbursement.backend.enums.Role;

import org.junit.jupiter.api.Test;

import java.time.LocalDate;

import static org.junit.jupiter.api.Assertions.*;

public class ClaimMapperTest {

    @Test
    void mapper_toDTO_full() {

        User employee = new User();
        employee.setId(1L);
        employee.setRole(Role.EMPLOYEE);

        User manager = new User();
        manager.setId(2L);
        manager.setRole(Role.MANAGER);

        Claim c = new Claim();
        c.setId(1L);
        c.setAmount(200.0);
        c.setDescription("Taxi");
        c.setStatus(ClaimStatus.SUBMITTED);
        c.setDate(LocalDate.now());
        c.setEmployee(employee);
        c.setReviewer(manager);
        c.setReviewerComment("ok");

        var dto = ClaimMapper.toDTO(c);

        assertEquals(1L, dto.getEmployeeId());
        assertEquals(2L, dto.getReviewerId());
        assertEquals("ok", dto.getReviewerComment());
    }

    @Test
    void mapper_nullComment() {

        User employee = new User();
        employee.setId(1L);

        User manager = new User();
        manager.setId(2L);

        Claim c = new Claim();
        c.setEmployee(employee);
        c.setReviewer(manager);

        var dto = ClaimMapper.toDTO(c);

        assertNull(dto.getReviewerComment());
    }


}

