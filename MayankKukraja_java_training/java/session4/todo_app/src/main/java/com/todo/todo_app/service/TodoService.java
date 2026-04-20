package com.todo.todo_app.service;

import com.todo.todo_app.dto.TodoDTO;
 import com.todo.todo_app.dto.TodoResponseDTO;

import java.util.List;



// interface for todo service
public interface TodoService {

   

    TodoResponseDTO createTodo(TodoDTO dto); // method to create a new todo item

    List<TodoResponseDTO> getAllTodos();// retreive all todo items

    TodoResponseDTO getTodoById(Long id); // retreive a specific todo item by its id

    TodoResponseDTO updateTodo(Long id, TodoDTO dto);  //updates exisiting item

    void deleteTodo(Long id);  //delete the item by id
}