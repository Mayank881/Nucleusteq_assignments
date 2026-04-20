package com.todo.todo_app.controller;

import com.todo.todo_app.dto.TodoDTO;
import com.todo.todo_app.dto.TodoResponseDTO;
import com.todo.todo_app.service.TodoService;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

import java.util.List;

//@RestController handles incoming HTTP requests and sends responses back to the client
@RestController
@RequestMapping("/todos")
public class TodoController {

    private final TodoService service;

    public TodoController(TodoService service) {
        this.service = service;
    }

    // it handles the post request to create a new todo
    // we use @valid ,,@requestbody to validate the incoming data and map it to our
    // dto obj
    @PostMapping
    public TodoResponseDTO createTodo(@Valid @RequestBody TodoDTO dto) {
        return service.createTodo(dto);
    }

    // handles get request to fetch all todos
    @GetMapping
    public List<TodoResponseDTO> getAllTodos() {
        return service.getAllTodos();
    }

    // handles get request to fetch todo by id
    @GetMapping("/{id}")
    public TodoResponseDTO getTodoById(@PathVariable Long id) {
        return service.getTodoById(id);
    }

    // putmapping will handle the update request to update existing todo
    // path variable get the id and @requestbody get the updated data from user
    @PutMapping("/{id}")
    public TodoResponseDTO updateTodo(@PathVariable Long id, @Valid @RequestBody TodoDTO dto) {
        return service.updateTodo(id, dto);
    }

    // @dkeletemapping will handle the delete request to delete existing todo using
    // id
    @DeleteMapping("/{id}")
    public String deleteTodo(@PathVariable Long id) {
        service.deleteTodo(id);
        return "Todo deleted successfully";
    }
}