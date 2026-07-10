import { useEffect, useMemo, useState } from "react";
import {
    FaEye,
    FaPlus,
    FaSearch,
} from "react-icons/fa";

import "./Issues.css";

import IssueForm from "../../components/issues/IssueForm";

import issueService from "../../services/issueService";
import projectService from "../../services/projectService";

const STATUS_OPTIONS = [
    "ALL",
    "BACKLOG",
    "TODO",
    "IN_PROGRESS",
    "DONE",
];

const Issues = () => {
    const [issues, setIssues] = useState([]);
    const [projects, setProjects] = useState([]);

    const [selectedIssue, setSelectedIssue] =
        useState(null);

    const [loading, setLoading] =
        useState(true);

    const [saving, setSaving] =
        useState(false);

    const [searchTerm, setSearchTerm] =
        useState("");

    const [statusFilter, setStatusFilter] =
        useState("ALL");

    const [showCreateModal, setShowCreateModal] =
        useState(false);

    const [showDetailsModal, setShowDetailsModal] =
        useState(false);

    const loadProjects = async () => {
        try {
            const response =
                await projectService.getAllProjects();

            setProjects(response);
        } catch (error) {
            alert(
                error?.response?.data?.detail ||
                "Unable to load projects."
            );
        }
    };

    const loadIssues = async () => {
        try {
            setLoading(true);

            const response =
                await issueService.getAllIssues();

            setIssues(response);
        } catch (error) {
            alert(
                error?.response?.data?.detail ||
                "Unable to load issues."
            );
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        loadProjects();
        loadIssues();
    }, []);

    const filteredIssues = useMemo(() => {
        return issues.filter((issue) => {
            const keyword =
                searchTerm.toLowerCase();

            const matchesSearch =
                issue.title
                    .toLowerCase()
                    .includes(keyword) ||
                issue.description
                    .toLowerCase()
                    .includes(keyword);

            const matchesStatus =
                statusFilter === "ALL"
                    ? true
                    : issue.status ===
                    statusFilter;

            return (
                matchesSearch &&
                matchesStatus
            );
        });
    }, [
        issues,
        searchTerm,
        statusFilter,
    ]);

    const handleCreateIssue = async (
        formData
    ) => {
        try {
            setSaving(true);

            const {
                projectId,
                ...issueData
            } = formData;

            await issueService.createIssue(
                projectId,
                issueData
            );

            setShowCreateModal(false);

            await loadIssues();
        } catch (error) {
            alert(
                error?.response?.data?.detail ||
                "Unable to create issue."
            );
        } finally {
            setSaving(false);
        }
    };

    const openDetailsModal = (
        issue
    ) => {
        setSelectedIssue(issue);
        setShowDetailsModal(true);
    };

    const handleStatusUpdate =
        async (
            issueId,
            projectId,
            status
        ) => {
            try {
                await issueService.updateIssueStatus(
                    projectId,
                    issueId,
                    status
                );

                await loadIssues();

                if (
                    selectedIssue &&
                    selectedIssue.id === issueId
                ) {
                    const updated =
                        await issueService.getIssueById(
                            issueId
                        );

                    setSelectedIssue(updated);
                }
            } catch (error) {
                alert(
                    error?.response?.data?.detail ||
                    "Unable to update status."
                );
            }
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

    return (
        <main className="issues-page">
            <div className="issues-header">
                <div>
                    <h1>Issues</h1>

                    <p>
                        Track and manage
                        project issues
                    </p>
                </div>

                <button
                    className="primary-btn"
                    onClick={() =>
                        setShowCreateModal(
                            true
                        )
                    }
                >
                    <FaPlus />

                    <span>
                        Create Issue
                    </span>
                </button>
            </div>

            <div className="toolbar">

                <div className="search-container">

                    <FaSearch className="search-icon" />

                    <input
                        type="text"
                        placeholder="Search issue..."
                        value={searchTerm}
                        onChange={(e) =>
                            setSearchTerm(
                                e.target.value
                            )
                        }
                    />
                </div>

                <select
                    value={statusFilter}
                    onChange={(e) =>
                        setStatusFilter(
                            e.target.value
                        )
                    }
                >
                    {STATUS_OPTIONS.map(
                        (status) => (
                            <option
                                key={status}
                                value={status}
                            >
                                {status}
                            </option>
                        )
                    )}
                </select>

            </div>
                        {loading ? (
                <div className="loading">
                    Loading Issues...
                </div>
            ) : filteredIssues.length === 0 ? (
                <div className="empty-state">
                    No Issues Found
                </div>
            ) : (
                <table className="issue-table">
                    <thead>
                        <tr>
                            <th>Title</th>
                            <th>Project</th>
                            <th>Priority</th>
                            <th>Status</th>
                            <th>Assignee</th>
                            <th>Actions</th>
                        </tr>
                    </thead>

                    <tbody>
                        {filteredIssues.map(
                            (issue) => {
                                const project =
                                    projects.find(
                                        (p) =>
                                            p.id ===
                                            issue.project_id
                                    );

                                const nextStatus =
                                    getNextStatus(
                                        issue.status
                                    );

                                return (
                                    <tr
                                        key={issue.id}
                                    >
                                        <td>
                                            {
                                                issue.title
                                            }
                                        </td>

                                        <td>
                                            {project
                                                ?.name ||
                                                "N/A"}
                                        </td>

                                        <td>
                                            <span
                                                className={`priority-badge priority-${issue.priority.toLowerCase()}`}
                                            >
                                                {
                                                    issue.priority
                                                }
                                            </span>
                                        </td>

                                        <td>
                                            <span
                                                className={`status-badge status-${issue.status.toLowerCase()}`}
                                            >
                                                {
                                                    issue.status
                                                }
                                            </span>
                                        </td>

                                        <td>
                                            {issue.assignee_id ||
                                                "--"}
                                        </td>

                                        <td className="action-buttons">

                                            <button
                                                className="icon-btn view-btn"
                                                onClick={() =>
                                                    openDetailsModal(
                                                        issue
                                                    )
                                                }
                                            >
                                                <FaEye />
                                            </button>

                                            {nextStatus && (
                                                <button
                                                    className="primary-btn small-btn"
                                                    onClick={() =>
                                                        handleStatusUpdate(
                                                            issue.id,
                                                            issue.project_id,
                                                            nextStatus
                                                        )
                                                    }
                                                >
                                                    Move to{" "}
                                                    {
                                                        nextStatus
                                                    }
                                                </button>
                                            )}
                                        </td>
                                    </tr>
                                );
                            }
                        )}
                    </tbody>
                </table>
            )}

            {showCreateModal && (
                <div className="modal-overlay">
                    <div className="modal">

                        <div className="modal-header">

                            <h2>
                                Create Issue
                            </h2>

                            <button
                                className="close-btn"
                                onClick={() =>
                                    setShowCreateModal(
                                        false
                                    )
                                }
                            >
                                ×
                            </button>

                        </div>

                        <IssueForm
                            projects={
                                projects
                            }
                            submitButtonText="Create Issue"
                            onSubmit={
                                handleCreateIssue
                            }
                            loading={
                                saving
                            }
                        />

                    </div>
                </div>
            )}

            {showDetailsModal &&
                selectedIssue && (
                    <div className="modal-overlay">

                        <div className="modal">

                            <div className="modal-header">

                                <h2>
                                    Issue Details
                                </h2>

                                <button
                                    className="close-btn"
                                    onClick={() => {
                                        setShowDetailsModal(
                                            false
                                        );

                                        setSelectedIssue(
                                            null
                                        );
                                    }}
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
                                        {
                                            selectedIssue.title
                                        }
                                    </span>
                                </div>

                                <div className="detail-item">
                                    <span className="detail-label">
                                        Description
                                    </span>

                                    <span className="detail-value">
                                        {
                                            selectedIssue.description
                                        }
                                    </span>
                                </div>

                                <div className="detail-item">
                                    <span className="detail-label">
                                        Project
                                    </span>

                                    <span className="detail-value">
                                        {
                                            projects.find(
                                                (project) =>
                                                    project.id ===
                                                    selectedIssue.project_id
                                            )?.name || "N/A"
                                        }
                                    </span>
                                </div>

                                <div className="detail-item">
                                    <span className="detail-label">
                                        Reporter
                                    </span>

                                    <span className="detail-value">
                                        {
                                            selectedIssue.reporter_id
                                        }
                                    </span>
                                </div>

                                <div className="detail-item">
                                    <span className="detail-label">
                                        Assignee
                                    </span>

                                    <span className="detail-value">
                                        {selectedIssue.assignee_id ||
                                            "--"}
                                    </span>
                                </div>

                                <div className="detail-item">
                                    <span className="detail-label">
                                        Type
                                    </span>

                                    <span className="detail-value">
                                        {
                                            selectedIssue.type
                                        }
                                    </span>
                                </div>

                                <div className="detail-item">
                                    <span className="detail-label">
                                        Priority
                                    </span>

                                    <span className="detail-value">
                                        {
                                            selectedIssue.priority
                                        }
                                    </span>
                                </div>

                                <div className="detail-item">
                                    <span className="detail-label">
                                        Status
                                    </span>

                                    <span className="detail-value">
                                        {
                                            selectedIssue.status
                                        }
                                    </span>
                                </div>

                                <div className="detail-item">
                                    <span className="detail-label">
                                        Parent Issue
                                    </span>

                                    <span className="detail-value">
                                        {selectedIssue.parent_id ||
                                            "--"}
                                    </span>
                                </div>
                                                            </div>

                            <div className="modal-footer">
                                {getNextStatus(
                                    selectedIssue.status
                                ) && (
                                    <button
                                        className="primary-btn"
                                        onClick={() =>
                                            handleStatusUpdate(
                                                selectedIssue.id,
                                                selectedIssue.project_id,
                                                getNextStatus(
                                                    selectedIssue.status
                                                )
                                            )
                                        }
                                    >
                                        Move to{" "}
                                        {getNextStatus(
                                            selectedIssue.status
                                        )}
                                    </button>
                                )}
                            </div>

                        </div>
                    </div>
                )}
        </main>
    );
};

export default Issues;