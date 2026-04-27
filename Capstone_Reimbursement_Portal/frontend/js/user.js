//handles user form submission with validation

 document.getElementById("userForm").addEventListener("submit", function (e) {

    e.preventDefault(); // prevent default form submission

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const role = document.getElementById("role").value;

    const message = document.getElementById("message");

    // Validation checks
    if (name === "") {
        message.innerText = "Name is required";
        return;
    }

    if (email === "") {
        message.innerText = "Email is required";
        return;
    }

    // email format check
    if (!email.includes("@")) {
        message.innerText = "Invalid email format";
        return;
    }

    if (password === "") {
        message.innerText = "Password is required";
        return;
    }

    if (password.length < 4) {
        message.innerText = "Password must be at least 4 characters";
        return;
    }

    //  If all valid we can proceed to submit data to backend
    const userData = { name, email, password, role };

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
                throw new Error(data.message);
            }

            message.innerText = "User created successfully";
            document.getElementById("userForm").reset();
        })
        .catch(err => {
            message.innerText = err.message;
        });

});

/*
  loads all users and displays in table
 */
function loadUsers() {

    fetch("http://localhost:8080/users")
        .then(res => res.json())
        .then(data => {

            const tableBody = document.getElementById("userTableBody");
            tableBody.innerHTML = "";

            data.forEach(user => {

                const row = `
                <tr>
                    <td>${user.id}</td>
                    <td>${user.name}</td>
                    <td>${user.email}</td>
                    <td>${user.role}</td>
                </tr>
            `;

                tableBody.innerHTML += row;
            });

            document.getElementById("userTable").style.display = "table";
        })
        .catch(err => {
            document.getElementById("message").innerText = "Error loading users";
        });
}