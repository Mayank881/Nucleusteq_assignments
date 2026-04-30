/**
 * Handles claim submission
 */
document.getElementById("claimForm").addEventListener("submit", async function (e) {

    e.preventDefault();

    const amount = parseFloat(document.getElementById("amount").value);
    const date = document.getElementById("date").value;
    const description = document.getElementById("description").value.trim();

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
            message.innerText = res.message || "Claim submitted successfully";
            document.getElementById("claimForm").reset();
        } else {
            message.innerText = "Failed to submit claim";
        }

    } catch (err) {
        message.innerText = err.message || "Something went wrong";
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
                  <td>${c.date}</td>
                  <td>${c.status}</td>
                  <td>${c.description}</td>
                  <td>${c.reviewerId}</td>
              </tr>
          `;

            body.innerHTML += row;
        });

        table.style.display = "table";

    } catch (err) {
        document.getElementById("message").innerText = err.message || "Error loading claims";
    }
}
