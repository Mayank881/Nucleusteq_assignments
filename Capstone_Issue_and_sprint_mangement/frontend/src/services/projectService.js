import api from "./api";

const projectService = {
    async getAllProjects() {
        const response = await api.get("/projects");
        return response.data;
    },

    async getProjectById(projectId) {
        const response = await api.get(
            `/projects/${projectId}`
        );

        return response.data;
    },

    async createProject(projectData) {
        const response = await api.post(
            "/projects",
            projectData
        );

        return response.data;
    },

    async updateProject(
        projectId,
        projectData
    ) {
        const response = await api.put(
            `/projects/${projectId}`,
            projectData
        );

        return response.data;
    },

    async deleteProject(projectId) {
        const response = await api.delete(
            `/projects/${projectId}`
        );

        return response.data;
    },

    async addMember(projectId, userId) {
        const response = await api.post(
            `/projects/${projectId}/members`,
            {
                user_id: userId,
            }
        );

        return response.data;
    },

    async removeMember(projectId, userId) {
        const response = await api.delete(
            `/projects/${projectId}/members/${userId}`
        );

        return response.data;
    },
};

export default projectService;