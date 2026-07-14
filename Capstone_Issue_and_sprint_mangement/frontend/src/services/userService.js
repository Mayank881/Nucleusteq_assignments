import api from "./api";

const userService = {
    async getAllUsers() {
        const response = await api.get("/users");
        return response.data;
    },
};

export default userService;