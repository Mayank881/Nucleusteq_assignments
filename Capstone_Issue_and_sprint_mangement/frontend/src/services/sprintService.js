import api from "./api";

const sprintService = {
    async getAllSprints() {
        const response = await api.get(
            "/sprints"
        );

        return response.data;
    },

    async getSprintById(sprintId) {
        const response = await api.get(
            `/sprints/${sprintId}`
        );

        return response.data;
    },

    async createSprint(sprintData) {
        const response = await api.post(
            "/sprints",
            sprintData
        );

        return response.data;
    },

    async updateSprint(
        sprintId,
        sprintData
    ) {
        const response = await api.put(
            `/sprints/${sprintId}`,
            sprintData
        );

        return response.data;
    },

    async startSprint(sprintId) {
        const response = await api.patch(
            `/sprints/${sprintId}/start`
        );

        return response.data;
    },

    async completeSprint(sprintId) {
        const response = await api.patch(
            `/sprints/${sprintId}/complete`
        );

        return response.data;
    },

    async addIssueToSprint(
        sprintId,
        issueId
    ) {
        const response = await api.post(
            `/sprints/${sprintId}/issues`,
            {
                issue_id: issueId,
            }
        );

        return response.data;
    },

    async removeIssueFromSprint(
        sprintId,
        issueId
    ) {
        const response = await api.delete(
            `/sprints/${sprintId}/issues/${issueId}`
        );

        return response.data;
    },
};

export default sprintService;