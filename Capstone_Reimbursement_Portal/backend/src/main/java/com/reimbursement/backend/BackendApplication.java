package com.reimbursement.backend;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class BackendApplication {

	public static void main(String[] args) {
		SpringApplication.run(BackendApplication.class, args);
	}

}
// | Folder     | Purpose                      |
// | ---------- | ---------------------------- |
// | controller | APIs (what client calls)     |
// | service    | business logic               |
// | repository | database operations          |
// | entity     | database tables              |
// | dto        | request/response objects     |
// | exception  | error handling               |
// | config     | security/config              |
// | enums      | fixed values (roles, status) |
// | util       | helper functions             |
