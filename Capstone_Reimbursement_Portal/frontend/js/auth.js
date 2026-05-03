// redirect if already logged in
if (Auth.isLoggedIn()) {
    redirectByRole(Auth.getRole());
}

document.getElementById("loginBtn").addEventListener("click", login);

/** Handle login */
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
        const res = await fetch(CONFIG.BASE_URL + "/auth/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email, password })
        });

        const data = await res.json();

        if (!res.ok) {
            throw new Error(data.message || "Login failed");
        }

        //  IMPORTANT: match your backend response
        Auth.save(data.data.token, {
            email: email,
            role: data.data.role,
            id: data.data.id
        });

        redirectByRole(data.data.role);

    } catch (err) {
        errorDiv.innerText = err.message;
    }
}