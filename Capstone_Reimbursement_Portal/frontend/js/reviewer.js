// protect
if (!Auth.isLoggedIn()) {
  window.location.href = "index.html";
}

const user = Auth.getUser();

// safety check
if (!user || !user.id) {
  alert("User ID missing. Please login again.");
  window.location.href = "index.html";
}

const name = user?.email ? user.email.split("@")[0] : "User";

document.getElementById("nav-name").innerText = name;
document.getElementById("nav-role").innerText = user?.role || "MANAGER";

const avatar = document.getElementById("avatar");
if (avatar) {
  avatar.innerText = name.charAt(0).toUpperCase();
}

/** switch tabs */
function showTab(tab) {
  document.getElementById("tab-pending").style.display =
    tab === "pending" ? "block" : "none";

  document.getElementById("tab-reviewed").style.display =
    tab === "reviewed" ? "block" : "none";
}

/** load claims (ONLY reviewer claims) */
async function loadClaims() {
  try {
    const res = await apiFetch(`/claims?reviewerId=${user.id}`);
    const claims = res.data;

    renderClaims(claims);
  } catch (err) {
    console.error(err);
    alert("Failed to load claims");
  }
}

/** render claims */
function renderClaims(claims) {

  const pending = claims.filter(c => c.status === "SUBMITTED");
  const reviewed = claims.filter(c => c.status !== "SUBMITTED");

  document.getElementById("pending-list").innerHTML =
    pending.length ? pending.map(renderCard).join("") : "No pending claims";

  document.getElementById("reviewed-list").innerHTML =
    reviewed.length ? reviewed.map(renderCard).join("") : "No reviewed claims";
}

/** render single card */
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
  try {
    const commentEl = document.getElementById(`comment-${id}`);
    const comment = commentEl ? commentEl.value : "";

    await apiFetch(
      `/claims/${id}/approve?reviewerId=${user.id}`,
      "PUT",
      { comment }
    );

    alert("Approved");
    loadClaims();

  } catch (err) {
    console.error(err);
    alert(err.message);
  }
}

/** reject */
async function reject(id) {
  try {
    const commentEl = document.getElementById(`comment-${id}`);
    const comment = commentEl ? commentEl.value : "";

    await apiFetch(
      `/claims/${id}/reject?reviewerId=${user.id}`,
      "PUT",
      { comment }
    );

    alert("Rejected");
    loadClaims();

  } catch (err) {
    console.error(err);
    alert(err.message);
  }
}

// init
loadClaims();