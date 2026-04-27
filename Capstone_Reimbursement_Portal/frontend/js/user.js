/**
 * handles user form submission
 */
document.getElementById("userForm").addEventListener("submit", function(e) {

    e.preventDefault();

    const userData = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        password: document.getElementById("password").value,
        role: document.getElementById("role").value
    };

    fetch("http://localhost:8080/users", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(userData)
    })
    .then(async res => {
        const data = await res.json();

        if (!res.ok) {
            throw new Error(data.message || "Failed to create user");
        }

        document.getElementById("message").innerText = "User created successfully";
        document.getElementById("userForm").reset();   // clear form
    })
    .catch(err => {
        document.getElementById("message").innerText = err.message;
    });

});