package session2.demo.model;

// This class is used to store user data
// kind of like a structure / blueprint for user object
public class User {

    private int id;
    private String name;
    private String email;

    // constructor to initialize user object
    // required for creating user object from JSON in API
    public User(int id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }

    // getters - required for returning data as JSON in API
    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }
}