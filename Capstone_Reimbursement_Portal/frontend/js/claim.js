
/**
 * Handles claim submission
 */
document.getElementById("claimForm").addEventListener("submit", async function (e) {

    e.preventDefault();

    const amount = document.getElementById("amount").value;
    const date = document.getElementById("date").value;
    const description = document.getElementById("description").value;

    const message = document.getElementById("message");

    // validation
    if (!amount || amount <= 0) {
        message.innerText = "Amount must be greater than 0";
        return;
    }

    if (!date) {
        message.innerText = "Date is required";
        return;
    }

    if (!description) {
        message.innerText = "Description is required";
        return;
    }

    const claimData = { amount, date, description };

    const employeeId = 1; // temporary 

    try {
        const res = await postRequest(`/claims/${employeeId}`, claimData);

        if (res && res.success) {
            message.innerText = res.message;
            document.getElementById("claimForm").reset();
        }

    } catch (err) {
        message.innerText = err.message;
    }
});


/**
 * Loads all claims and displays in table
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
                    <td>${c.status}</td>
                    <td>${c.description}</td>
                </tr>
            `;

            body.innerHTML += row;
        });

        table.style.display = "table";

    } catch (err) {
        document.getElementById("message").innerText = "Error loading claims";
    }
}
