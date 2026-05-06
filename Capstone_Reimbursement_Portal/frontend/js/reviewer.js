// protect
if (!Auth.isLoggedIn()) {
    window.location.href = "index.html";
}

const user = Auth.getUser();

// ADMIN BUTTON LOGIC (SAFE)
const adminBtn = document.getElementById("admin-btn");

if (adminBtn && user.role === "ADMIN") {
    adminBtn.style.display = "inline-block";

    adminBtn.onclick = () => {
        window.location.href = "admin.html";
    };
}
const name = user?.email ? user.email.split("@")[0] : "User";

document.getElementById("nav-name").innerText = name;
document.getElementById("nav-role").innerText = user?.role || "MANAGER";
document.getElementById("avatar").innerText = name.charAt(0).toUpperCase();

/** switch tabs */
function showTab(tab) {
    document.getElementById("tab-pending").style.display =
        tab === "pending" ? "block" : "none";

    document.getElementById("tab-reviewed").style.display =
        tab === "reviewed" ? "block" : "none";
}

/** load all claims */
async function loadClaims() {
    try {
        const res = await apiFetch(`/claims?reviewerId=${user.id}`);
        const claims = res.data;

        renderClaims(claims);
    } catch (err) {
        console.error(err);
    }
}

/** render */
function renderClaims(claims) {

    const pending = claims.filter(c => c.status === "SUBMITTED");
    const reviewed = claims.filter(c => c.status !== "SUBMITTED");

    // pending
    document.getElementById("pending-list").innerHTML =
        pending.length ? pending.map(renderCard).join("") : "No pending claims";

    // reviewed
    document.getElementById("reviewed-list").innerHTML =
        reviewed.length ? reviewed.map(renderCard).join("") : "No reviewed claims";
}

/** card html */
function renderCard(c) {
    return `
    <div class="claim-card">
      <div><b>${c.description}</b></div>
      <div>₹${c.amount}</div>
      <div>${c.date}</div>
      <div>Status: ${c.status}</div>

      ${c.status === "SUBMITTED" ? `
        <textarea id="comment-${c.id}" placeholder="Add comment"></textarea>

        <div class="claim-actions">
          <button class="btn btn-approve"
            onclick="approve(${c.id})">Approve</button>

          <button class="btn btn-reject"
            onclick="reject(${c.id})">Reject</button>
        </div>
      ` : `
        ${c.reviewerComment ? `<div>Comment: ${c.reviewerComment}</div>` : ""}
      `}
    </div>
  `;
}

/** approve */
async function approve(id) {
    const comment = document.getElementById(`comment-${id}`).value;

    await apiFetch(`/claims/${id}/approve?reviewerId=${user.id}`, "PUT", {
        comment
    });

    loadClaims();
}

/** reject */
async function reject(id) {
    const comment = document.getElementById(`comment-${id}`).value;

    await apiFetch(`/claims/${id}/reject?reviewerId=${user.id}`, "PUT", {
        comment
    });

    loadClaims();
}

// init
loadClaims();