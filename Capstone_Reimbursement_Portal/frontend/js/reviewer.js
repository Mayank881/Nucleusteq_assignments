/**
 * Loads all claims and displays them with action buttons
 */
async function loadClaims() {

    // get logged-in user info from localStorage
    const user = JSON.parse(localStorage.getItem("user"));

    // safety check (redirect if not logged in)
    if (!user) {
        window.location.href = "login.html";
        return;
    }

    const reviewerId = user.id;

    try {
        const res = await getRequest("/claims");

        if (!res || !res.success) {
            document.getElementById("message").innerText = "Unable to load claims";
            return;
        }

        const claims = res.data;

        const body = document.getElementById("claimBody");
        const table = document.getElementById("claimTable");

        body.innerHTML = "";

        // handle empty claims
        if (!claims.length) {
            body.innerHTML = "<tr><td colspan='6'>No claims found</td></tr>";
            table.style.display = "table";
            return;
        }

        // filter only reviewer claims
        claims
            .filter(c => c.reviewerId === reviewerId)
            .forEach(c => {

                const row = `
                    <tr>
                        <td>${c.id}</td>
                        <td>${c.amount}</td>
                        <td>${c.date}</td>
                        <td>${c.description}</td>
                        <td>${c.status}</td>
                        <td>
                            ${
                                c.status === "SUBMITTED"
                                ? `
                                    <button onclick="approveClaim(${c.id}, ${c.reviewerId})">Approve</button>
                                    <button onclick="rejectClaim(${c.id}, ${c.reviewerId})">Reject</button>
                                  `
                                : "No Action"
                            }
                        </td>
                    </tr>
                `;

                body.innerHTML += row;
            });

        table.style.display = "table";

    } catch (err) {
        document.getElementById("message").innerText =
            err.message || "Error loading claims";
    }
}


/**
 * Approves a claim
 */
async function approveClaim(claimId, reviewerId) {

    try {
        const res = await putRequest(`/claims/${claimId}/approve?reviewerId=${reviewerId}`);

        if (res && res.success) {
            document.getElementById("message").innerText =
                res.message || "Claim approved successfully";
            loadClaims(); // refresh
        }

    } catch (err) {
        document.getElementById("message").innerText =
            err.message || "Error approving claim";
    }
}


/**
 * Rejects a claim
 */
async function rejectClaim(claimId, reviewerId) {

    try {
        const res = await putRequest(`/claims/${claimId}/reject?reviewerId=${reviewerId}`);

        if (res && res.success) {
            document.getElementById("message").innerText =
                res.message || "Claim rejected successfully";
            loadClaims(); // refresh
        }

    } catch (err) {
        document.getElementById("message").innerText =
            err.message || "Error rejecting claim";
    }
}