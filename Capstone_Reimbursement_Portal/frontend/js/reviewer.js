/**
 * Loads all claims and displays them with action buttons
 */
async function loadClaims() {

    try {
        const res = await getRequest("/claims");

        if (!res || !res.success) return;

        const claims = res.data;

        const body = document.getElementById("claimBody");
        const table = document.getElementById("claimTable");

        body.innerHTML = "";

        claims.forEach(c => {

            const row = `
                <tr>
                    <td>${c.id}</td>
                    <td>${c.amount}</td>
                    <td>${c.description}</td>
                    <td>${c.status}</td>
                    <td>
                        <button onclick="approveClaim(${c.id})">Approve</button>
                        <button onclick="rejectClaim(${c.id})">Reject</button>
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
async function approveClaim(claimId) {

    const reviewerId = 1; // temporary

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
async function rejectClaim(claimId) {

    const reviewerId = 1; // temporary

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
