/**
 * Handles login form submission
 */
document.getElementById("loginForm").addEventListener("submit", async function (e) {

    e.preventDefault();

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    const message = document.getElementById("message");

    // validation
    if (!email) {
        message.innerText = "Email is required";
        return;
    }

    if (!email.includes("@")) {
        message.innerText = "Invalid email format";
        return;
    }

    if (!password) {
        message.innerText = "Password is required";
        return;
    }

    try {
        // fetch all users
        const res = await getRequest("/users");

        if (!res || !res.success) {
            message.innerText = "Unable to login";
            return;
        }

        const users = res.data;
        // currently  using a simple client-side check for demo purposes
        const user = users.find(u => u.email === email);

        if (!user) {
            message.innerText = "Invalid email or password";
            return;
        }

        // store user in localStorage
        localStorage.setItem("user", JSON.stringify(user));

        //success message
        message.innerText = "Login successful";

        // redirect based on role
        if (user.role === "EMPLOYEE") {
            window.location.href = "claim.html";
        } else if (user.role === "MANAGER" || user.role === "ADMIN") {
            window.location.href = "reviewer.html";
        }

    } catch (err) {
        message.innerText = err.message || "Login failed";
    }
});