package com.todo.todo_app.service;

import com.todo.todo_app.dto.TodoDTO; //connecting all the layers together
import com.todo.todo_app.entity.Status;
import com.todo.todo_app.entity.Todo;
import com.todo.todo_app.exception.ResourceNotFoundException;
import com.todo.todo_app.repository.TodoRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class TodoServiceImpl implements TodoService {

   //repo used to talk to database
    private final TodoRepository repo;

    // constructor injection 
    public TodoServiceImpl(TodoRepository repo) {
        this.repo = repo;
    }

    
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

        todo.setCreatedAt(LocalDateTime.now());

        // saving todo to database
        return repo.save(todo);
    }

    // get all todos
    @Override
    public List<Todo> getAllTodos() {

        // returns list of all 
        return repo.findAll();
    }

    // getting todos by id
    @Override
    public Todo getTodoById(Long id) {

        // finding todo using id
       // updating the code to throw custom exception if todo not found
       return repo.findById(id)
        .orElseThrow(() -> new ResourceNotFoundException("Todo not found"));
        //USES ARROW FUNCTION TO THROW EXCEPTION IF TODO NOT FOUND
    }

       // update todo
    @Override
    public Todo updateTodo(Long id, TodoDTO dto) {

       //UPDATING THIS ONE TOO TO THROW EXCEPTION IF TODO NOT FOUND

        Todo todo = repo.findById(id)
        .orElseThrow(() -> new ResourceNotFoundException("Todo not found"));

        // if not found, return null
   
        if (todo == null) {
            return null;
        }

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
            }
        }

        // saving updated todo
        return repo.save(todo);
    }

    // DELETE TODO
    @Override
    public void deleteTodo(Long id) {

        // find todo by id

        Todo todo = repo.findById(id)
        .orElseThrow(() -> new ResourceNotFoundException("Todo not found"));
        // if not found, return'
   

        if (todo == null) {
            return;
        }

        // deleting todo
        repo.delete(todo);
    }
}