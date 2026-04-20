package com.todo.todo_app.service;

import com.todo.todo_app.dto.TodoDTO;
import com.todo.todo_app.entity.Status;
import com.todo.todo_app.entity.Todo;
import com.todo.todo_app.repository.TodoRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class TodoServiceImpl implements TodoService {

    // repo is used to talk to database
    private final TodoRepository repo;

    // constructor injection 
    public TodoServiceImpl(TodoRepository repo) {
        this.repo = repo;
    }

    // creating todo item
    @Override
    public Todo createTodo(TodoDTO dto) {

        Todo todo = new Todo();

        // taking values from dto and setting in entity
        todo.setTitle(dto.getTitle());
        todo.setDescription(dto.getDescription());

        // if user does not send status, set it to PENDING by default
        if (dto.getStatus() == null) {
            todo.setStatus(Status.PENDING);
        } else {
            todo.setStatus(dto.getStatus());
        }

        // setting current time automatically
        todo.setCreatedAt(LocalDateTime.now());

        // saving todo in database
        return repo.save(todo);
    }

    // GET ALL TODOS
    @Override
    public List<Todo> getAllTodos() {

        // returns list of all todos from database
        return repo.findAll();
    }

    // GET TODO BY ID
    @Override
    public Todo getTodoById(Long id) {

        // finding todo using id
        // if not found, returning null for now (later we will handle exception)
        return repo.findById(id).orElse(null);
    }

    // UPDATE TODO
    @Override
    public Todo updateTodo(Long id, TodoDTO dto) {

        // first find existing todo
        Todo todo = repo.findById(id).orElse(null);

        // if not found, return null
        if (todo == null) {
            return null;
        }

        // updating only those fields which user sends
        if (dto.getTitle() != null) {
            todo.setTitle(dto.getTitle());
        }

        if (dto.getDescription() != null) {
            todo.setDescription(dto.getDescription());
        }

        // handling status change
        if (dto.getStatus() != null) {

            Status current = todo.getStatus();
            Status newStatus = dto.getStatus();

            // only allow valid transitions (PENDING <-> COMPLETED)
            if ((current == Status.PENDING && newStatus == Status.COMPLETED) ||
                (current == Status.COMPLETED && newStatus == Status.PENDING)) {

                todo.setStatus(newStatus);
            }
        }

        // saving updated todo
        return repo.save(todo);
    }

    // DELETE TODO
    @Override
    public void deleteTodo(Long id) {

        // find todo by id
        Todo todo = repo.findById(id).orElse(null);

        // if exists, delete it
        if (todo != null) {
            repo.delete(todo);
        }
    }
}