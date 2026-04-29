
/**
 * Handles user form submission with validation and API call
 */
document.getElementById("userForm").addEventListener("submit", async function (e) {

    e.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const role = document.getElementById("role").value;

    const message = document.getElementById("message");

    // validate inputs
    if (name === "") {
        message.innerText = "Name is required";
        return;
    }

    if (email === "") {
        message.innerText = "Email is required";
        return;
    }

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

    const userData = { name, email, password, role };

    try {
        const res = await postRequest("/users", userData);

        if (res && res.success) {
            message.innerText = res.message;
            document.getElementById("userForm").reset();
        }

    } catch (err) {
        message.innerText = err.message;
    }
});


/**
 * Fetches all users from backend and displays them in table
 */
async function loadUsers() {

    try {
        const res = await getRequest("/users");

        if (!res || !res.success) return;

        const users = res.data;

        const tableBody = document.getElementById("userTableBody");
        tableBody.innerHTML = "";

        users.forEach(user => {

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

    } catch (err) {
        document.getElementById("message").innerText = "Error loading users";
    }
}
