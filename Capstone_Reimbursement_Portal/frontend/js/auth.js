/**
 * Login user and store session
 */
async function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (!email || !password) {
        alert("Enter email and password");
        return;
    }

    try {
        const user = await apiCall("/users/login", "POST", {
            email,
            password
        });

        // store logged-in user
        localStorage.setItem("user", JSON.stringify(user));

        window.location.href = "index.html";

    } catch (error) {
        alert("Invalid credentials");
    }
}