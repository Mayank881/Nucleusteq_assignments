package com.todo.todo_app.repository;

import com.todo.todo_app.entity.Todo;
import org.springframework.data.jpa.repository.JpaRepository;

// repository interface for todo entity
public interface TodoRepository extends JpaRepository<Todo, Long> {

}