let allManagers = [];

// protect
if (!Auth.isLoggedIn()) {
    window.location.href = "index.html";
}

const user = Auth.getUser();

if (!user || user.role !== "ADMIN") {
    alert("Unauthorized");
    window.location.href = "index.html";
}

// NAVBAR
const name = user.email ? user.email.split("@")[0] : "Admin";

document.getElementById("admin-name").innerText = name;
document.getElementById("admin-role").innerText = user.role || "ADMIN";
document.getElementById("avatar").innerText = name.charAt(0).toUpperCase();

// pagination
let page = 0;
const size = 5;
let usersData = [];

// ================= USERS =================

async function loadUsers() {
    try {
        const res = await apiFetch(`/users?page=${page}&size=${size}`);
        const data = res.data;

        usersData = data.content;

        console.log("USERS:", usersData); // debug

        renderUsers(usersData);

        document.getElementById("page-info").innerText =
            `Page ${data.page + 1} of ${data.totalPages}`;

    } catch (err) {
        alert(err.message);
    }
}

async function loadManagers() {
    try {
        const res = await apiFetch("/users?page=0&size=100");
        const data = res.data;

        allManagers = data.content.filter(
            u => u.role === "MANAGER" || u.role === "ADMIN"
        );

        console.log("MANAGERS:", allManagers); // debug

    } catch (err) {
        console.error(err);
    }
}

// ================= RENDER =================

function renderUsers(users) {

    const table = document.getElementById("user-table");
    table.innerHTML = "";

    users.forEach(u => {

        const managerOptions = allManagers
            .map(m => `
    <option value="${m.id}" 
      ${(u.managerId && u.managerId === m.id) ||
                    (!u.managerId && m.role === "ADMIN")
                    ? "selected"
                    : ""
                }>
      ${m.name || m.email}
    </option>
  `)
            .join("");

        table.innerHTML += `
            <tr>
                <td>${u.name}</td>
                <td>${u.email}</td>
                <td>${u.role}</td>

                <td>
                  ${u.role === "EMPLOYEE"
                ? `
                        <select onchange="assignManager(${u.id}, this.value)">
                          <option value="">None</option>
                          ${managerOptions}
                        </select>
                      `
                : `<span>-</span>`
            }
                </td>

                <td>
                    <button onclick="deleteUser(${u.id})">Delete</button>
                </td>
            </tr>
        `;
    });
}

// ================= CREATE =================

async function createUser() {

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const role = document.getElementById("role").value;

    if (!email.endsWith("@company.com")) {
        document.getElementById("msg").innerText = "Use company email";
        return;
    }

    try {
        await apiFetch("/users", "POST", {
            name,
            email,
            password,
            role
        });

        document.getElementById("msg").innerText = "User created";
        loadUsers();

    } catch (err) {
        document.getElementById("msg").innerText = err.message;
    }
}

// ================= DELETE =================

async function deleteUser(id) {

    if (!confirm("Delete this user?")) return;

    try {
        await apiFetch(`/users/${id}`, "DELETE");
        loadUsers();

    } catch (err) {
        alert(err.message);
    }
}

// ================= ASSIGN =================

async function assignManager(userId, managerId) {

    if (!managerId) return;

    const selectedUser = usersData.find(u => u.id === userId);

    if (!selectedUser || selectedUser.role !== "EMPLOYEE") {
        alert("Only employee can be assigned manager");
        return;
    }

    try {
        console.log("Assigning:", userId, managerId);

        await apiFetch(`/users/${userId}/assign/${managerId}`, "PUT");

        alert("Manager assigned successfully");

        loadUsers();

    } catch (err) {
        console.error(err);
        alert(err.message);
    }
}

// ================= PAGINATION =================

function nextPage() {
    page++;
    loadUsers();
}

function prevPage() {
    if (page > 0) {
        page--;
        loadUsers();
    }
}

// ================= NAV =================

function goToReviewer() {
    window.location.href = "reviewer.html";
}

// ================= INIT =================

loadManagers();
loadUsers();