import api from "./api";

const commentService = {
    async getCommentsByIssue(issueId) {
        const response = await api.get(
            `/comments/issues/${issueId}`
        );

        return response.data;
    },

    async createComment(
        issueId,
        commentData
    ) {
        const response = await api.post(
            `/comments/issues/${issueId}`,
            commentData
        );

        return response.data;
    },

    async updateComment(
        commentId,
        commentData
    ) {
        const response = await api.put(
            `/comments/${commentId}`,
            commentData
        );

        return response.data;
    },

    async deleteComment(commentId) {
        const response = await api.delete(
            `/comments/${commentId}`
        );

        return response.data;
    },
};

export default commentService;