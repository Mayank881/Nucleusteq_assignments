const CONFIG = {
    BASE_URL: "http://localhost:8080",
    TOKEN_KEY: "token",
    USER_KEY: "user"
};

// ================= AUTH =================
const Auth = {
    save(token, user) {
        localStorage.setItem(CONFIG.TOKEN_KEY, token);
        localStorage.setItem(CONFIG.USER_KEY, JSON.stringify(user));
    },

    getToken() {
        return localStorage.getItem(CONFIG.TOKEN_KEY);
    },

    getUser() {
        return JSON.parse(localStorage.getItem(CONFIG.USER_KEY));
    },

    getRole() {
        const u = this.getUser();
        return u ? u.role : null;
    },

    isLoggedIn() {
        return !!this.getToken();
    },

    logout() {
        localStorage.clear();
        window.location.href = "index.html";
    }
};

// ================= API =================
async function apiFetch(url, options = {}) {
    const token = Auth.getToken();

    const res = await fetch(CONFIG.BASE_URL + url, {
        ...options,
        headers: {
            "Content-Type": "application/json",
            ...(token && { Authorization: "Bearer " + token })
        }
    });

    const data = await res.json();

    if (!res.ok) {
        throw new Error(data.message || "Error");
    }

    return data;
}

// ================= REDIRECT =================
function redirectByRole(role) {
    if (role === "ADMIN") window.location.href = "admin.html";
    else if (role === "MANAGER") window.location.href = "reviewer.html";
    else window.location.href = "employee.html";
}