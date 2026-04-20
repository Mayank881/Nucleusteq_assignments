package com.todo.todo_app.service;

import com.todo.todo_app.dto.TodoDTO;
import com.todo.todo_app.entity.Todo;

import java.util.List;

// interface for todo service
public interface TodoService {

    Todo createTodo(TodoDTO dto); // method to create a new todo item

    List<Todo> getAllTodos(); // retreive all todo items

    Todo getTodoById(Long id); // retreive a specific todo item by its id

    Todo updateTodo(Long id, TodoDTO dto);  //updates exisiting item

    void deleteTodo(Long id);  //delete the item by id
}