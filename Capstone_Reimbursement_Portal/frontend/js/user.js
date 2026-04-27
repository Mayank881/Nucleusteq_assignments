/*
 handles user form submission
 */
document.getElementById("userForm").addEventListener("submit", function (e) {

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
                throw new Error(data.message);
            }

            document.getElementById("message").innerText = "User created successfully";
            document.getElementById("userForm").reset();
        })
        .catch(err => {
            document.getElementById("message").innerText = err.message;
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