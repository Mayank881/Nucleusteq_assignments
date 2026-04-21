package com.todo.todo_app.controller;

import com.todo.todo_app.dto.TodoDTO;
import com.todo.todo_app.dto.TodoResponseDTO;
import com.todo.todo_app.service.TodoService;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import org.slf4j.Logger; // for logging
import org.slf4j.LoggerFactory; // to create logger instance

//@RestController handles incoming HTTP requests and sends responses back to the client
@RestController
@RequestMapping("/todos")
public class TodoController {

    // creating logger instance for this class
    private static final Logger logger = LoggerFactory.getLogger(TodoController.class);
    private final TodoService service;

    public TodoController(TodoService service) {
        this.service = service;
    }

    // it handles the post request to create a new todo
    // we use @valid ,,@requestbody to validate the incoming data and map it to our
    // dto obj
    @PostMapping
    public TodoResponseDTO createTodo(@Valid @RequestBody TodoDTO dto) {

        // logging the creation of new todo with title
        logger.info("Received request to create todo");
        return service.createTodo(dto);
    }

    // handles get request to fetch all todos
    @GetMapping
    public List<TodoResponseDTO> getAllTodos() {

        // logging the fetching of all todos
        logger.info("Received request to fetch all todos");
        return service.getAllTodos();

    }

    // handles get request to fetch todo by id
    @GetMapping("/{id}")
    public TodoResponseDTO getTodoById(@PathVariable Long id) {
        logger.info("Received request to fetch todo with id: {}", id);
        return service.getTodoById(id);
    }

    // putmapping will handle the update request to update existing todo
    // path variable get the id and @requestbody get the updated data from user
    @PutMapping("/{id}")
    public TodoResponseDTO updateTodo(@PathVariable Long id, @Valid @RequestBody TodoDTO dto) {
        logger.info("Received request to update todo with id: {}", id);
        return service.updateTodo(id, dto);
    }

    // @dkeletemapping will handle the delete request to delete existing todo using
    // id
    @DeleteMapping("/{id}")
    public String deleteTodo(@PathVariable Long id) {
        
        logger.info("Received request to delete todo with id: {}", id);

        service.deleteTodo(id);
        return "Todo deleted successfully";
    }
}