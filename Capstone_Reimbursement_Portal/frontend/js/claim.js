/**
 * handles claim submission
 */
document.getElementById("claimForm").addEventListener("submit", function(e) {

    e.preventDefault();

    const employeeId = document.getElementById("employeeId").value;

    const claimData = {
        amount: document.getElementById("amount").value,
        date: document.getElementById("date").value,
        description: document.getElementById("description").value
    };

    fetch(`http://localhost:8080/claims/${employeeId}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(claimData)
    })
    .then(async res => {
        const data = await res.json();

        if (!res.ok) {
            throw new Error(data.message || "Failed to submit claim");
        }

        document.getElementById("message").innerText = "Claim submitted successfully";
        document.getElementById("claimForm").reset();  // clear form
    })
    .catch(err => {
        document.getElementById("message").innerText = err.message;
    });

});