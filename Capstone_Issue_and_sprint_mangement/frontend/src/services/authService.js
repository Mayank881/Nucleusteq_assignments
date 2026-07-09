import api from "./api";

const authService = {
    async register(userData) {
        const response = await api.post(
            "/users/register",
            userData,
            {
                headers: {
                    "Content-Type": "application/json",
                },
            }
        );

        return response.data;
    },

    async login(credentials) {
        const formData = new URLSearchParams();

        formData.append(
            "username",
            credentials.email
        );

        formData.append(
            "password",
            credentials.password
        );

        const response = await api.post(
            "/users/login",
            formData,
            {
                headers: {
                    "Content-Type":
                        "application/x-www-form-urlencoded",
                },
            }
        );

        return response.data;
    },

    async getCurrentUser() {
        const response = await api.get(
            "/users/me"
        );

        return response.data;
    },
};

export default authService;