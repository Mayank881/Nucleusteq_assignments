package com.reimbursement.backend.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.reimbursement.backend.dto.UserRequestDTO;
import com.reimbursement.backend.dto.UserResponseDTO;
import com.reimbursement.backend.enums.Role;
import com.reimbursement.backend.service.UserService;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import java.util.Map;

import static org.mockito.ArgumentMatchers.*;
import static org.mockito.Mockito.doThrow;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest
@AutoConfigureMockMvc(addFilters = false)
class UserControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private UserService userService;

    @Autowired
    private ObjectMapper objectMapper;

    // CREATE USER
    @Test
    void createUser_success() throws Exception {

        UserRequestDTO req = new UserRequestDTO();
        req.setName("test");
        req.setEmail("test@company.com");
        req.setPassword("1234");
        req.setRole(Role.EMPLOYEE);

        UserResponseDTO res = new UserResponseDTO();
        res.setId(1L);

        when(userService.createUser(any())).thenReturn(res);

        mockMvc.perform(post("/users")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(req)))
                .andExpect(status().isCreated());
    }

    // GET USERS
    @Test
    void getUsers_success() throws Exception {

        when(userService.getAllUsers(anyInt(), anyInt()))
                .thenReturn(Map.of("content", java.util.List.of()));

        mockMvc.perform(get("/users")
                .param("page", "0")
                .param("size", "5"))
                .andExpect(status().isOk());
    }

    // DELETE USER
    @Test
    void deleteUser_success() throws Exception {

        mockMvc.perform(delete("/users/1"))
                .andExpect(status().isOk());
    }

    // ASSIGN MANAGER
    @Test
    void assignManager_success() throws Exception {

        mockMvc.perform(put("/users/1/assign/2"))
                .andExpect(status().isOk());
    }

    @Test
    void createUser_error() throws Exception {

        UserRequestDTO req = new UserRequestDTO();
        req.setEmail("test@company.com");

        when(userService.createUser(any()))
                .thenThrow(new RuntimeException("error"));

        mockMvc.perform(post("/users")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(req)))
                .andExpect(status().isBadRequest());
    }

    @Test
    void getUsers_empty() throws Exception {

        when(userService.getAllUsers(anyInt(), anyInt()))
                .thenReturn(Map.of("content", java.util.List.of()));

        mockMvc.perform(get("/users")
                .param("page", "0")
                .param("size", "5"))
                .andExpect(status().isOk());
    }

    @Test
    void deleteUser_error() throws Exception {

        doThrow(new RuntimeException())
                .when(userService).deleteUser(1L);

        mockMvc.perform(delete("/users/1"))
                .andExpect(status().isInternalServerError());
    }

    @Test
    void assignManager_error() throws Exception {

        doThrow(new RuntimeException())
                .when(userService).assignManager(1L, 2L);

        mockMvc.perform(put("/users/1/assign/2"))
                .andExpect(status().isInternalServerError());
    }
}