import api from "./api";

const issueService = {
    async getAllIssues() {
        const response = await api.get(
            "/issues"
        );

        return response.data;
    },

    async getIssueById(issueId) {
        const response = await api.get(
            `/issues/${issueId}`
        );

        return response.data;
    },

    async createIssue(
        projectId,
        issueData
    ) {
        const response = await api.post(
            `/issues/project/${projectId}`,
            issueData
        );

        return response.data;
    },

    async updateIssueStatus(
        projectId,
        issueId,
        status
    ) {
        const response = await api.patch(
            `/issues/${projectId}/${issueId}/status`,
            {
                status,
            }
        );

        return response.data;
    },

    async searchIssues(params) {
        const response = await api.get(
            "/issues/search",
            {
                params,
            }
        );

        return response.data;
    },
};

export default issueService;