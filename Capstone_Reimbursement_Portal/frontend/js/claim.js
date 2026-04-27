//handles claim form submission with validation

document.getElementById("claimForm").addEventListener("submit", function (e) {

    e.preventDefault();

    const employeeId = document.getElementById("employeeId").value.trim();
    const amount = document.getElementById("amount").value.trim();
    const date = document.getElementById("date").value;
    const description = document.getElementById("description").value.trim();

    const message = document.getElementById("message");

    // Validating inputs

    if (employeeId === "") {
        message.innerText = "Employee ID is required";
        return;
    }

    if (amount === "") {
        message.innerText = "Amount is required";
        return;
    }
    // uses parseFloat to convert string to number and checks if it's greater than 0 -- comment for my understanding
    if (parseFloat(amount) <= 0) {
        message.innerText = "Amount must be greater than 0";     
        return;
    }

    if (date === "") {
        message.innerText = "Date is required";
        return;
    }

    if (description === "") {
        message.innerText = "Description is required";
        return;
    }

    // validate and submit claim data
    const claimData = {
        amount,
        date,
        description
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
                throw new Error(data.message);
            }

            message.innerText = "Claim submitted successfully";
            document.getElementById("claimForm").reset();
        })
        .catch(err => {
            message.innerText = err.message;
        });

});