import { useEffect, useMemo, useState } from "react";
import {
    FaEye,
    FaPlus,
    FaSearch,
} from "react-icons/fa";

import "./Issues.css";

import IssueForm from "../../components/issues/IssueForm";
import IssueDetails from "../../components/issues/IssueDetails";
import Pagination from "../../components/common/Pagination";

import issueService from "../../services/issueService";
import projectService from "../../services/projectService";
import userService from "../../services/userService";

const STATUS_OPTIONS = [
    "ALL",
    "BACKLOG",
    "TODO",
    "IN_PROGRESS",
    "DONE",
];

const Issues = () => {
    const [issues, setIssues] =
        useState([]);

    const [currentPage, setCurrentPage] = useState(1);
    const [totalPages, setTotalPages] = useState(1);

    const PAGE_SIZE = 10;
    const [projects, setProjects] =
        useState([]);

    const [users, setUsers] =
        useState([]);

    const [loading, setLoading] =
        useState(true);

    const [saving, setSaving] =
        useState(false);

    const [selectedIssue, setSelectedIssue] =
        useState(null);

    const [showCreateModal, setShowCreateModal] =
        useState(false);

    const [showDetailsModal, setShowDetailsModal] =
        useState(false);

    const [searchTerm, setSearchTerm] =
        useState("");

    const [statusFilter, setStatusFilter] =
        useState("ALL");

    const [projectFilter, setProjectFilter] =
        useState("ALL");

    const [assigneeFilter, setAssigneeFilter] =
        useState("ALL");

    const loadProjects = async () => {
        try {
            const response = await projectService.getAllProjects(
                1,
                1000
            );

            setProjects(response.items || []);
        } catch (error) {
            alert(
                error?.response?.data?.detail ||
                "Unable to load projects."
            );
        }
    };

    const loadUsers = async () => {
        try {
            const response =
                await userService.getAllUsers();

            setUsers(response);
        } catch (error) {
            alert(
                error?.response?.data?.detail ||
                "Unable to load users."
            );
        }
    };

    const loadIssues = async () => {
        try {
            setLoading(true);

            const response =
                await issueService.getAllIssues(
                    currentPage,
                    PAGE_SIZE
                );

            setIssues(response.items || []);
            setCurrentPage(response.page);
            setTotalPages(response.total_pages);
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
        loadUsers();
    }, []);;

    useEffect(() => {
        loadIssues();
    }, [currentPage]);

    const handlePreviousPage = () => {
        if (currentPage > 1) {
            setCurrentPage((prev) => prev - 1);
        }
    };

    const handleNextPage = () => {
        if (currentPage < totalPages) {
            setCurrentPage((prev) => prev + 1);
        }
    };

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
                    selectedIssue.id ===
                    issueId
                ) {
                    const updated =
                        await issueService.getIssueById(
                            issueId
                        );

                    setSelectedIssue(
                        updated
                    );
                }
            } catch (error) {
                alert(
                    error?.response?.data?.detail ||
                    "Unable to update status."
                );
            }
        };

    const getUserName = (
        userId
    ) => {
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
    const filteredIssues = useMemo(() => {
        return issues.filter((issue) => {
            const keyword =
                searchTerm
                    .trim()
                    .toLowerCase();

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

            const matchesProject =
                projectFilter === "ALL"
                    ? true
                    : issue.project_id ===
                    projectFilter;

            const matchesAssignee =
                assigneeFilter === "ALL"
                    ? true
                    : issue.assignee_id ===
                    assigneeFilter;

            return (
                matchesSearch &&
                matchesStatus &&
                matchesProject &&
                matchesAssignee
            );
        });
    }, [
        issues,
        searchTerm,
        statusFilter,
        projectFilter,
        assigneeFilter,
    ]);

    const projectOptions =
        useMemo(() => {
            return projects.map(
                (project) => ({
                    id: project.id,
                    name: project.name,
                })
            );
        }, [projects]);

    const assigneeOptions =
        useMemo(() => {
            return users.map(
                (user) => ({
                    id: user.id,
                    name: user.name,
                })
            );
        }, [users]);
    return (
        <main className="issues-page">
            <div className="issues-header">
                <div>
                    <h1>Issues</h1>

                    <p>
                        Track and manage project
                        issues.
                    </p>
                </div>

                <button
                    className="primary-btn"
                    onClick={() =>
                        setShowCreateModal(true)
                    }
                >
                    <FaPlus />

                    <span>Create Issue</span>
                </button>
            </div>

            <div className="toolbar">

                <div className="search-container">

                    <FaSearch className="search-icon" />

                    <input
                        type="text"
                        placeholder="Search issues..."
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

                <select
                    value={projectFilter}
                    onChange={(e) =>
                        setProjectFilter(
                            e.target.value
                        )
                    }
                >
                    <option value="ALL">
                        All Projects
                    </option>

                    {projectOptions.map(
                        (project) => (
                            <option
                                key={project.id}
                                value={
                                    project.id
                                }
                            >
                                {
                                    project.name
                                }
                            </option>
                        )
                    )}
                </select>

                <select
                    value={assigneeFilter}
                    onChange={(e) =>
                        setAssigneeFilter(
                            e.target.value
                        )
                    }
                >
                    <option value="ALL">
                        All Assignees
                    </option>

                    {assigneeOptions.map(
                        (user) => (
                            <option
                                key={user.id}
                                value={
                                    user.id
                                }
                            >
                                {user.name}
                            </option>
                        )
                    )}
                </select>

            </div>

            {loading ? (
                <div className="loading">
                    Loading Issues...
                </div>
            ) : filteredIssues.length ===
                0 ? (
                <div className="empty-state">
                    No Issues Found
                </div>
            ) : (
                <table className="issue-table">

                    <thead>

                        <tr>

                            <th>Title</th>

                            <th>Project</th>

                            <th>Type</th>

                            <th>Priority</th>

                            <th>Status</th>

                            <th>Assignee</th>

                            <th>Actions</th>

                        </tr>

                    </thead>

                    <tbody>

                        {filteredIssues.map(
                            (issue) => {

                                const nextStatus =
                                    getNextStatus(
                                        issue.status
                                    );

                                return (
                                    <tr
                                        key={
                                            issue.id
                                        }
                                    >
                                        <td>
                                            {
                                                issue.title
                                            }
                                        </td>

                                        <td>
                                            {getProjectName(
                                                issue.project_id
                                            )}
                                        </td>

                                        <td>
                                            {
                                                issue.type
                                            }
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
                                            {getUserName(
                                                issue.assignee_id
                                            )}
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

            <Pagination
                currentPage={currentPage}
                totalPages={totalPages}
                onPrevious={handlePreviousPage}
                onNext={handleNextPage}
            />
            {showCreateModal && (
                <div className="modal-overlay">
                    <div className="modal">

                        <div className="modal-header">
                            <h2>Create Issue</h2>

                            <button
                                className="close-btn"
                                onClick={() =>
                                    setShowCreateModal(false)
                                }
                            >
                                ×
                            </button>
                        </div>

                        <IssueForm
                            projects={projects}
                            users={users}
                            issues={issues}
                            submitButtonText="Create Issue"
                            onSubmit={handleCreateIssue}
                            loading={saving}
                        />

                    </div>
                </div>
            )}

            {showDetailsModal &&
                selectedIssue && (
                    <IssueDetails
                        issue={selectedIssue}
                        users={users}
                        projects={projects}
                        issues={issues}
                        onClose={() => {
                            setShowDetailsModal(false);
                            setSelectedIssue(null);
                        }}
                        onStatusUpdate={
                            handleStatusUpdate
                        }
                    />
                )}

        </main>
    );
};

export default Issues;