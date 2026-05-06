/** @constant {string} Backend base URL */
const BASE_URL = "http://localhost:8080";

// redirect if already logged in
(() => {
    const token = localStorage.getItem("token");
    const role = localStorage.getItem("role");

    if (token && role) {
        redirectByRole(role);
    }
})();

document.getElementById("loginBtn").addEventListener("click", login);

/**
 * Login user and redirect based on role
 * @returns {Promise<void>}
 */
async function login() {

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const errorDiv = document.getElementById("error");

    errorDiv.innerText = "";

    if (!email || !password) {
        errorDiv.innerText = "All fields required";
        return;
    }

    if (!email.endsWith("@company.com")) {
        errorDiv.innerText = "Use company email";
        return;
    }

    try {
        const res = await fetch(BASE_URL + "/auth/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        const data = await res.json();

        if (!res.ok) {
            throw new Error(data.message || "Login failed");
        }

        localStorage.setItem("token", data.data.token);
        localStorage.setItem("role", data.data.role);
        localStorage.setItem("email", email);

        redirectByRole(data.data.role);

    } catch (err) {
        errorDiv.innerText = err.message;
    }
}

/**
 * Redirect user based on role
 * @param {string} role
 */
function redirectByRole(role) {
    if (role === "EMPLOYEE") {
        window.location.href = "employee.html";
    } else if (role === "MANAGER") {
        window.location.href = "reviewer.html";
    } else {
        window.location.href = "admin.html";
    }
}