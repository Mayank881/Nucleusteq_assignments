package com.reimbursement.backend.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.reimbursement.backend.dto.ClaimActionDTO;
import com.reimbursement.backend.dto.ClaimRequestDTO;
import com.reimbursement.backend.dto.ClaimResponseDTO;
import com.reimbursement.backend.service.ClaimService;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import java.time.LocalDate;
import java.util.List;

import static org.mockito.ArgumentMatchers.*;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest
@AutoConfigureMockMvc(addFilters = false)
class ClaimControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private ClaimService claimService;

    @Autowired
    private ObjectMapper objectMapper;

    // ================= SUBMIT =================
    @Test
    void submitClaim_success() throws Exception {

        ClaimResponseDTO response = new ClaimResponseDTO();
        response.setId(1L);

        when(claimService.submitClaim(any(), anyLong())).thenReturn(response);

        ClaimRequestDTO req = new ClaimRequestDTO();
        req.setAmount(100.0);
        req.setDescription("Food");
        req.setDate(LocalDate.now());

        mockMvc.perform(post("/claims/1")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(req)))
                .andExpect(status().isCreated());
    }

    // ================= GET =================
    @Test
    void getClaims_success() throws Exception {

        ClaimResponseDTO dto = new ClaimResponseDTO();
        dto.setId(1L);

        when(claimService.getAllClaims()).thenReturn(List.of(dto));

        mockMvc.perform(get("/claims"))
                .andExpect(status().isOk());
    }

    // ================= APPROVE =================
    @Test
    void approveClaim_success() throws Exception {

        ClaimResponseDTO dto = new ClaimResponseDTO();
        dto.setId(1L);

        when(claimService.approveClaim(anyLong(), anyLong(), anyString()))
                .thenReturn(dto);

        ClaimActionDTO action = new ClaimActionDTO();
        action.setComment("ok");

        mockMvc.perform(put("/claims/1/approve")
                .param("reviewerId", "2")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(action)))
                .andExpect(status().isOk());
    }

    @Test
    void getClaims_empty() throws Exception {

        when(claimService.getAllClaims()).thenReturn(List.of());

        mockMvc.perform(get("/claims"))
                .andExpect(status().isOk());
    }

    @Test
    void approveClaim_error() throws Exception {

        when(claimService.approveClaim(anyLong(), anyLong(), anyString()))
                .thenThrow(new RuntimeException("error"));

        ClaimActionDTO action = new ClaimActionDTO();
        action.setComment("ok");

        mockMvc.perform(put("/claims/1/approve")
                .param("reviewerId", "2")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(action)))
                .andExpect(status().isInternalServerError());
    }

    @Test
    void rejectClaim_error() throws Exception {

        when(claimService.rejectClaim(anyLong(), anyLong(), anyString()))
                .thenThrow(new RuntimeException("error"));

        ClaimActionDTO action = new ClaimActionDTO();
        action.setComment("no");

        mockMvc.perform(put("/claims/1/reject")
                .param("reviewerId", "2")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(action)))
                .andExpect(status().isInternalServerError());
    }

    @Test
    void submitClaim_error() throws Exception {

        when(claimService.submitClaim(any(), anyLong()))
                .thenThrow(new RuntimeException());

        mockMvc.perform(post("/claims/1")
                .contentType(MediaType.APPLICATION_JSON)
                .content("""
                            {
                                "amount":100,
                                "description":"food",
                                "date":"2024-01-01"
                            }
                        """))
                .andExpect(status().isInternalServerError());
    }
}