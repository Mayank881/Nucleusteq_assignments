/**
 * Loads all claims and displays them with action buttons
 */
async function loadClaims() {

    //temporary reviewerId until we implement login
    const reviewerId = 2;
    try {
        const res = await getRequest("/claims");

        if (!res || !res.success) return;
        const claims = res.data;

        const body = document.getElementById("claimBody");
        const table = document.getElementById("claimTable");

        body.innerHTML = "";


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
                        ${c.status === "SUBMITTED"
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
        document.getElementById("message").innerText = "Error loading claims";
    }
}


/**
 * Approves a claim
 */
async function approveClaim(claimId, reviewerId) {

    try {
        const res = await putRequest(`/claims/${claimId}/approve?reviewerId=${reviewerId}`);

        if (res && res.success) {
            document.getElementById("message").innerText = res.message;
            loadClaims(); // refresh
        }

    } catch (err) {
        document.getElementById("message").innerText = err.message;
    }
}


/**
 * Rejects a claim
 */
async function rejectClaim(claimId, reviewerId) {

    try {
        const res = await putRequest(`/claims/${claimId}/reject?reviewerId=${reviewerId}`);

        if (res && res.success) {
            document.getElementById("message").innerText = res.message;
            loadClaims(); // refresh
        }

    } catch (err) {
        document.getElementById("message").innerText = err.message;
    }
}
