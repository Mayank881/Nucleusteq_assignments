package com.todo.todo_app.controller;

import com.todo.todo_app.dto.TodoDTO;
import com.todo.todo_app.entity.Todo;
import com.todo.todo_app.service.TodoService;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

//@RestController handles incoming HTTP requests and sends responses back to the client
@RestController
@RequestMapping("/todos")
public class TodoController {

    private final TodoService service;

    public TodoController(TodoService service) {
        this.service = service;
    }
   
    // it handles the post request to create a new todo
    // we use @valid ,,@requestbody to validate the incoming data and map it to our dto
    @PostMapping
    public Todo createTodo(@Valid @RequestBody TodoDTO dto) {
        return service.createTodo(dto);
    }
}