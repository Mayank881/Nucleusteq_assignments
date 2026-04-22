package com.todo.todo_app.service;

import com.todo.todo_app.dto.TodoDTO;
import com.todo.todo_app.entity.Status;
import com.todo.todo_app.entity.Todo;
import com.todo.todo_app.repository.TodoRepository;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;


import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

public class TodoServiceImplTest {

    @Mock
    private TodoRepository repo;

    @Mock
    private NotificationServiceClient notificationClient;

    @InjectMocks
    private TodoServiceImpl service;

    public TodoServiceImplTest() {
        MockitoAnnotations.openMocks(this);
    }

    // test create todo
    @Test
    void testCreateTodo() {

        TodoDTO dto = new TodoDTO();
        dto.setTitle("Test Todo");
        dto.setDescription("Test Desc");

        Todo saved = new Todo();
        saved.setId(1L);
        saved.setTitle("Test Todo");
        saved.setStatus(Status.PENDING);

        when(repo.save(any(Todo.class))).thenReturn(saved);

        var result = service.createTodo(dto);

        assertNotNull(result);
        assertEquals("Test Todo", result.getTitle());

        verify(notificationClient, times(1))
                .sendNotification(anyString());
    }

    // test get all todos
    @Test
    void testGetAllTodos() {

        Todo t1 = new Todo();
        t1.setId(1L);

        Todo t2 = new Todo();
        t2.setId(2L);

        when(repo.findAll()).thenReturn(List.of(t1, t2));

        var result = service.getAllTodos();

        assertEquals(2, result.size());
    }

    // test get by id
    @Test
    void testGetTodoById() {

        Todo todo = new Todo();
        todo.setId(1L);

        when(repo.findById(1L)).thenReturn(Optional.of(todo));

        var result = service.getTodoById(1L);

        assertEquals(1L, result.getId());
    }

    // test not found
    @Test
    void testGetTodoById_NotFound() {

        when(repo.findById(1L)).thenReturn(Optional.empty());

        assertThrows(RuntimeException.class, () -> {
            service.getTodoById(1L);
        });
    }

    // test update
    @Test
    void testUpdateTodo() {

        Todo todo = new Todo();
        todo.setId(1L);
        todo.setStatus(Status.PENDING);

        TodoDTO dto = new TodoDTO();
        dto.setStatus(Status.COMPLETED);

        when(repo.findById(1L)).thenReturn(Optional.of(todo));
        when(repo.save(any())).thenReturn(todo);

        var result = service.updateTodo(1L, dto);

        assertEquals(Status.COMPLETED, result.getStatus());
    }

    // invalid status test
    @Test
    void testUpdateTodo_InvalidStatus() {

        Todo todo = new Todo();
        todo.setId(1L);
        todo.setStatus(Status.PENDING);

        TodoDTO dto = new TodoDTO();
        dto.setStatus(Status.PENDING); // invalid

        when(repo.findById(1L)).thenReturn(Optional.of(todo));

        assertThrows(IllegalArgumentException.class, () -> {
            service.updateTodo(1L, dto);
        });
    }

    // delete test
    @Test
    void testDeleteTodo() {

        Todo todo = new Todo();
        todo.setId(1L);

        when(repo.findById(1L)).thenReturn(Optional.of(todo));

        service.deleteTodo(1L);

        verify(repo, times(1)).delete(todo);
    }
}