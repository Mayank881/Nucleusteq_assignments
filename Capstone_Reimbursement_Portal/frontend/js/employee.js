// protect page
if (!Auth.isLoggedIn()) {
    window.location.href = "index.html";
}

window.onload = function () {

    const user = Auth.getUser();

    const name = user?.email ? user.email.split("@")[0] : "User";

    document.getElementById("nav-name").innerText = name;
    document.getElementById("nav-role").innerText = user?.role || "EMPLOYEE";

    const avatar = document.getElementById("avatar");
    if (avatar) {
        avatar.innerText = name.charAt(0).toUpperCase();
    }
};

let page = 0;
const size = 5;

/** switch tabs */
function showTab(name) {
    document.getElementById("tab-claims").style.display = name === "claims" ? "block" : "none";
    document.getElementById("tab-submit").style.display = name === "submit" ? "block" : "none";
}

/** load claims */
async function loadClaims() {
    try {
        const res = await apiFetch(`/claims?page=${page}&size=${size}`);
        const claims = res.data.content || res.data;

        renderClaims(claims);
        updateStats(claims);

        document.getElementById("page-info").innerText =
            `Page ${page + 1}`;

    } catch (err) {
        console.error(err);
    }
}

/** render claims */
function renderClaims(claims) {
    const container = document.getElementById("claims-list");

    if (!claims.length) {
        container.innerHTML = `<p>No claims found</p>`;
        return;
    }

    container.innerHTML = claims.map(c => `
        <div class="claim-item">
            <div class="claim-top">
                <div class="claim-info">
                    <div class="claim-desc">${c.description}</div>
                    <div class="claim-meta">
                        <span>${c.date}</span>
                    </div>
                </div>

                <div>
                    <div class="claim-amount">₹${c.amount}</div>
                    <div>${c.status}</div>
                </div>
            </div>

            ${c.reviewerComment ? `
                <div class="claim-comment">
                    <strong>Reviewer:</strong> ${c.reviewerComment}
                </div>
            ` : ""}
        </div>
    `).join("");
}

/** stats */
function updateStats(claims) {
    document.getElementById("stat-total").innerText = claims.length;
    document.getElementById("stat-approved").innerText =
        claims.filter(c => c.status === "APPROVED").length;
    document.getElementById("stat-pending").innerText =
        claims.filter(c => c.status === "SUBMITTED").length;
    document.getElementById("stat-rejected").innerText =
        claims.filter(c => c.status === "REJECTED").length;
}

/** pagination */
function changePage(dir) {
    if (page + dir < 0) return;
    page += dir;
    loadClaims();
}

/** submit claim */
async function submitClaim() {

    const description = document.getElementById("description").value;
    const amount = document.getElementById("amount").value;
    const date = document.getElementById("date").value;

    if (!description || !amount || !date) {
        alert("All fields required");
        return;
    }

    const user = Auth.getUser();

    console.log("Submitting:", {
        description,
        amount,
        date,
        user
    });

    try {
        await apiFetch(`/claims/${user.id}`, "POST", {
            description,
            amount: Number(amount),
            date
        });


        alert("Claim submitted");

        showTab("claims");
        loadClaims();

    } catch (err) {
        console.error(err);
        alert(err.message);
    }
}

// init
loadClaims();