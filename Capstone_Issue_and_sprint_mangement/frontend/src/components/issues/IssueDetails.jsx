import { useEffect, useState } from "react";

import commentService from "../../services/commentService";
import authService from "../../services/authService";

import CommentSection from "./CommentSection";

function IssueDetails({
    issue,
    users,
    projects,
    issues,
    onClose,
    onStatusUpdate,
}) {
    const [comments, setComments] =
        useState([]);

    const [currentUser, setCurrentUser] =
        useState(null);

    const [loadingComments, setLoadingComments] =
        useState(true);

    const loadCurrentUser = async () => {
        try {
            const response =
                await authService.getCurrentUser();

            setCurrentUser(response);

        } catch (error) {
            console.error(error);
        }
    };

    const loadComments = async () => {
        if (!issue) {
            return;
        }

        try {
            setLoadingComments(true);

            const response =
                await commentService.getCommentsByIssue(
                    issue.id
                );

            setComments(response);

        } catch (error) {
            console.error(error);
            setComments([]);
        } finally {
            setLoadingComments(false);
        }
    };

    useEffect(() => {
        loadCurrentUser();
    }, []);

    useEffect(() => {
        loadComments();
    }, [issue]);

    const getUserName = (userId) => {
        if (!userId) {
            return "--";
        }

        const user = users.find(
            (u) => u.id === userId
        );

        return user
            ? user.name
            : "--";
    };

    const getProjectName = (
        projectId
    ) => {
        const project =
            projects.find(
                (p) =>
                    p.id === projectId
            );

        return project
            ? project.name
            : "--";
    };

    const getIssueTitle = (
        issueId
    ) => {
        if (!issueId) {
            return "--";
        }

        const parent =
            issues.find(
                (i) =>
                    i.id === issueId
            );

        return parent
            ? parent.title
            : "--";
    };

    const getNextStatus = (
        status
    ) => {
        switch (status) {
            case "BACKLOG":
                return "TODO";

            case "TODO":
                return "IN_PROGRESS";

            case "IN_PROGRESS":
                return "DONE";

            default:
                return null;
        }
    };

    const refreshComments =
        async () => {
            await loadComments();
        };

    if (!issue) {
        return null;
    }
        return (
        <div className="modal-overlay">
            <div className="modal issue-details-modal">

                <div className="modal-header">
                    <h2>Issue Details</h2>

                    <button
                        className="close-btn"
                        onClick={onClose}
                    >
                        ×
                    </button>
                </div>

                <div className="issue-details">

                    <div className="detail-item">
                        <span className="detail-label">
                            Title
                        </span>

                        <span className="detail-value">
                            {issue.title}
                        </span>
                    </div>

                    <div className="detail-item">
                        <span className="detail-label">
                            Description
                        </span>

                        <span className="detail-value">
                            {issue.description}
                        </span>
                    </div>

                    <div className="detail-item">
                        <span className="detail-label">
                            Project
                        </span>

                        <span className="detail-value">
                            {getProjectName(
                                issue.project_id
                            )}
                        </span>
                    </div>

                    <div className="detail-item">
                        <span className="detail-label">
                            Reporter
                        </span>

                        <span className="detail-value">
                            {getUserName(
                                issue.reporter_id
                            )}
                        </span>
                    </div>

                    <div className="detail-item">
                        <span className="detail-label">
                            Assignee
                        </span>

                        <span className="detail-value">
                            {getUserName(
                                issue.assignee_id
                            )}
                        </span>
                    </div>

                    <div className="detail-item">
                        <span className="detail-label">
                            Parent Issue
                        </span>

                        <span className="detail-value">
                            {getIssueTitle(
                                issue.parent_id
                            )}
                        </span>
                    </div>

                    <div className="detail-item">
                        <span className="detail-label">
                            Type
                        </span>

                        <span className="detail-value">
                            {issue.type}
                        </span>
                    </div>

                    <div className="detail-item">
                        <span className="detail-label">
                            Priority
                        </span>

                        <span className="detail-value">
                            {issue.priority}
                        </span>
                    </div>

                    <div className="detail-item">
                        <span className="detail-label">
                            Status
                        </span>

                        <span
                            className={`status-badge status-${issue.status.toLowerCase()}`}
                        >
                            {issue.status}
                        </span>
                    </div>

                </div>

                <div className="modal-footer">

                    {getNextStatus(
                        issue.status
                    ) && (
                        <button
                            className="primary-btn"
                            onClick={() =>
                                onStatusUpdate(
                                    issue.id,
                                    issue.project_id,
                                    getNextStatus(
                                        issue.status
                                    )
                                )
                            }
                        >
                            Move to{" "}
                            {getNextStatus(
                                issue.status
                            )}
                        </button>
                    )}

                </div>

                <hr />

                <CommentSection
                    issueId={issue.id}
                    comments={comments}
                    users={users}
                    currentUser={currentUser}
                    loading={loadingComments}
                    refreshComments={refreshComments}
                />

            </div>
        </div>
    );
}

export default IssueDetails;