const BASE_URL = "http://localhost:8080";

/**
 * Generic GET request
 */
async function getRequest(endpoint) {
    try {
        const response = await fetch(BASE_URL + endpoint);

        if (!response.ok) {
            throw new Error("GET request failed");
        }

        return await response.json();
    } catch (error) {
        console.error("GET Error:", error);
        alert("Something went wrong while fetching data");
    }
}

/**
 * Generic POST request
 */
async function postRequest(endpoint, data) {
    try {
        const response = await fetch(BASE_URL + endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.message);
        }

        return result;
    } catch (error) {
        console.error("POST Error:", error);
        alert(error.message || "Something went wrong");
    }
}

/**
 * Generic PUT request
 */
async function putRequest(endpoint) {
    try {
        const response = await fetch(BASE_URL + endpoint, {
            method: "PUT"
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.message);
        }

        return result;
    } catch (error) {
        console.error("PUT Error:", error);
        alert(error.message || "Something went wrong");
    }
}