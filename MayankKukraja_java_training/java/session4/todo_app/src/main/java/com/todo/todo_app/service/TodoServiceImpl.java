package com.todo.todo_app.service;

import com.todo.todo_app.dto.TodoDTO; //connecting all the layers together
import com.todo.todo_app.dto.TodoResponseDTO;
import com.todo.todo_app.entity.Status;
import com.todo.todo_app.entity.Todo;
import com.todo.todo_app.exception.ResourceNotFoundException;
import com.todo.todo_app.repository.TodoRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class TodoServiceImpl implements TodoService {

    // repo used to talk to database
    private final TodoRepository repo;

    // constructor injection
    public TodoServiceImpl(TodoRepository repo) {
        this.repo = repo;
    }

    // method to map entity to response dto
    // this will help to not expose our entity directly to client
    private TodoResponseDTO mapToDTO(Todo todo) {

        TodoResponseDTO dto = new TodoResponseDTO();

        dto.setId(todo.getId());
        dto.setTitle(todo.getTitle());
        dto.setDescription(todo.getDescription());
        dto.setStatus(todo.getStatus());
        dto.setCreatedAt(todo.getCreatedAt());

        return dto;
    }

    @Override
    public TodoResponseDTO createTodo(TodoDTO dto) {

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

        todo.setCreatedAt(LocalDateTime.now());

        // save and convert to response dto
        Todo savedTodo = repo.save(todo);

        return mapToDTO(savedTodo);
    }

    @Override
    public List<TodoResponseDTO> getAllTodos() {

        List<Todo> todos = repo.findAll();

        return todos.stream()
                .map(this::mapToDTO)
                .toList();
    }

    // getting todos by id
    @Override
    public TodoResponseDTO getTodoById(Long id) {

        Todo todo = repo.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Todo not found"));

        return mapToDTO(todo);
    }

    // update todo
    @Override
    public TodoResponseDTO updateTodo(Long id, TodoDTO dto) {

        // UPDATING THIS ONE TOO TO THROW EXCEPTION IF 
        Todo todo = repo.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Todo not found"));

        // updating feilds if they are provided in dto
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

            // only allow valid transitions
            if ((current == Status.PENDING && newStatus == Status.COMPLETED) ||
                    (current == Status.COMPLETED && newStatus == Status.PENDING)) {

                todo.setStatus(newStatus);
            } else {
                throw new IllegalArgumentException("Invalid status change"); //illegal arg, exc. used 
            }
        }
        // saving updated todo
        return mapToDTO(repo.save(todo));
    }

    // DELETE todo
    @Override
    public void deleteTodo(Long id) {

        // find todo by id

        Todo todo = repo.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Todo not found"));

        // deleting todo
        repo.delete(todo);
    }
}