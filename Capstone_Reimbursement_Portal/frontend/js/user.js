console.log("User JS loaded");

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

    // validation
    if (name === "") {
        message.innerText = "Name is required";
        return;
    }

    if (email === "") {
        message.innerText = "Email is required";
        return;
    }

    if (!email.endsWith("@company.com")) {
        message.innerText = "Email must be @company.com domain";
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
 * Fetch users and display in table
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


/**
 * Assign manager to employee
 */
window.assignManager = async function () {

    console.log("Assign button clicked");

    const employeeId = document.getElementById("employeeId").value;
    const managerId = document.getElementById("managerId").value;
    const message = document.getElementById("message");

    if (!employeeId || !managerId) {
        message.innerText = "Enter employee and manager ID";
        return;
    }

    try {
        const res = await postRequest("/users/assign", {
            employeeId,
            managerId
        });

        console.log("Response:", res);

        if (res && res.success) {
            message.innerText = res.message || "Manager assigned";
        } else {
            message.innerText = "Assignment failed";
        }

    } catch (err) {
        console.error(err);
        message.innerText = "Error assigning manager";
    }
};