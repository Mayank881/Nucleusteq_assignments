import { useEffect, useMemo, useState } from "react";
import {
    FaCheck,
    FaEdit,
    FaEye,
    FaPlay,
    FaPlus,
    FaSearch,
} from "react-icons/fa";

import "./Sprints.css";

import SprintForm from "../../components/sprints/SprintForm";

import sprintService from "../../services/sprintService";
import projectService from "../../services/projectService";
import issueService from "../../services/issueService";
import Pagination from "../../components/common/Pagination";

const Sprints = () => {
    const [sprints, setSprints] =
        useState([]);

    const [currentPage, setCurrentPage] = useState(1);
    const [totalPages, setTotalPages] = useState(1);

    const PAGE_SIZE = 10;

    const [projects, setProjects] =
        useState([]);

    const [issues, setIssues] =
        useState([]);

    const [selectedSprint, setSelectedSprint] =
        useState(null);

    const [loading, setLoading] =
        useState(true);

    const [saving, setSaving] =
        useState(false);

    const [searchTerm, setSearchTerm] =
        useState("");

    const [issueId, setIssueId] =
        useState("");

    const [showCreateModal, setShowCreateModal] =
        useState(false);

    const [showEditModal, setShowEditModal] =
        useState(false);

    const [showDetailsModal, setShowDetailsModal] =
        useState(false);

    const loadProjects = async () => {
        try {
            const response =
                await projectService.getAllProjects(
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

    const loadIssues = async () => {
        try {
            const response =
                await issueService.getAllIssues(
                    1,
                    1000
                );

            setIssues(response.items || []);
        } catch (error) {
            alert(
                error?.response?.data?.detail ||
                "Unable to load issues."
            );
        }
    };

    const loadSprints = async () => {
        try {
            setLoading(true);

            const response =
                await sprintService.getAllSprints(
                    currentPage,
                    PAGE_SIZE
                );

            setSprints(response.items || []);
            setCurrentPage(response.page);
            setTotalPages(response.total_pages);
        } catch (error) {
            alert(
                error?.response?.data?.detail ||
                "Unable to load sprints."
            );
        } finally {
            setLoading(false);
        }
    };
    useEffect(() => {
        loadProjects();
        loadIssues();
    }, []);

    useEffect(() => {
        loadSprints();
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



    const filteredSprints = useMemo(() => {
        const keyword =
            searchTerm.toLowerCase();

        return sprints.filter((sprint) => {
            const project =
                projects.find(
                    (p) =>
                        p.id ===
                        sprint.project_id
                );

            return (
                sprint.name
                    .toLowerCase()
                    .includes(keyword) ||
                sprint.status
                    .toLowerCase()
                    .includes(keyword) ||
                project?.name
                    ?.toLowerCase()
                    .includes(keyword)
            );
        });
    }, [
        sprints,
        projects,
        searchTerm,
    ]);

    const refreshSelectedSprint =
        async (sprintId) => {
            const updated =
                await sprintService.getSprintById(
                    sprintId
                );

            setSelectedSprint(updated);
        };

    const formatDateForInput = (
        date
    ) => {
        return new Date(date)
            .toISOString()
            .slice(0, 16);
    };
    const handleCreateSprint = async (
        formData
    ) => {
        try {
            setSaving(true);

            await sprintService.createSprint({
                name: formData.name,
                project_id: formData.projectId,
                start_date:
                    formData.start_date,
                end_date:
                    formData.end_date,
            });

            setShowCreateModal(false);

            await loadSprints();
        } catch (error) {
            alert(
                error?.response?.data?.detail ||
                "Unable to create sprint."
            );
        } finally {
            setSaving(false);
        }
    };

    const handleEditSprint = async (
        formData
    ) => {
        try {
            setSaving(true);

            await sprintService.updateSprint(
                selectedSprint.id,
                {
                    name: formData.name,
                    start_date:
                        formData.start_date,
                    end_date:
                        formData.end_date,
                }
            );

            setShowEditModal(false);

            setSelectedSprint(null);

            await loadSprints();
        } catch (error) {
            alert(
                error?.response?.data?.detail ||
                "Unable to update sprint."
            );
        } finally {
            setSaving(false);
        }
    };

    const openDetailsModal =
        async (sprint) => {
            try {
                const response =
                    await sprintService.getSprintById(
                        sprint.id
                    );

                setSelectedSprint(
                    response
                );

                setShowDetailsModal(
                    true
                );
            } catch (error) {
                alert(
                    error?.response?.data?.detail ||
                    "Unable to load sprint."
                );
            }
        };

    const openEditModal = (
        sprint
    ) => {
        setSelectedSprint({
            ...sprint,
            projectId:
                sprint.project_id,
            start_date:
                formatDateForInput(
                    sprint.start_date
                ),
            end_date:
                formatDateForInput(
                    sprint.end_date
                ),
        });

        setShowEditModal(true);
    };

    const handleStartSprint =
        async (sprintId) => {
            try {
                await sprintService.startSprint(
                    sprintId
                );

                await loadSprints();

                if (
                    selectedSprint?.id ===
                    sprintId
                ) {
                    await refreshSelectedSprint(
                        sprintId
                    );
                }
            } catch (error) {
                alert(
                    error?.response?.data?.detail ||
                    "Unable to start sprint."
                );
            }
        };

    const handleCompleteSprint =
        async (sprintId) => {
            try {
                await sprintService.completeSprint(
                    sprintId
                );

                await loadSprints();

                if (
                    selectedSprint?.id ===
                    sprintId
                ) {
                    await refreshSelectedSprint(
                        sprintId
                    );
                }
            } catch (error) {
                alert(
                    error?.response?.data?.detail ||
                    "Unable to complete sprint."
                );
            }
        };

    const handleAddIssue =
        async () => {
            if (
                !issueId.trim()
            ) {
                return;
            }

            try {
                await sprintService.addIssueToSprint(
                    selectedSprint.id,
                    issueId
                );

                setIssueId("");

                await loadSprints();
                await loadIssues();

                await refreshSelectedSprint(
                    selectedSprint.id
                );
            } catch (error) {
                alert(
                    error?.response?.data?.detail ||
                    "Unable to add issue."
                );
            }
        };

    const handleRemoveIssue =
        async (issueId) => {
            try {
                await sprintService.removeIssueFromSprint(
                    selectedSprint.id,
                    issueId
                );

                await loadSprints();
                await loadIssues();

                await refreshSelectedSprint(
                    selectedSprint.id
                );
            } catch (error) {
                alert(
                    error?.response?.data?.detail ||
                    "Unable to remove issue."
                );
            }
        };

    const availableIssues =
        selectedSprint
            ? issues.filter((issue) => {

                return (

                    issue.project_id ===
                    selectedSprint.project_id &&

                    !selectedSprint.issue_ids.includes(
                        issue.id
                    ) &&

                    issue.status !== "DONE"

                );

            })
            : [];

    return (
        <main className="issues-page">
            <div className="issues-header">
                <div>
                    <h1>Sprints</h1>

                    <p>
                        Plan and manage
                        project sprints
                    </p>
                </div>

                <button
                    className="primary-btn"
                    onClick={() =>
                        setShowCreateModal(true)
                    }
                >
                    <FaPlus />

                    <span>
                        Create Sprint
                    </span>
                </button>
            </div>

            <div className="toolbar">
                <div className="search-container">
                    <FaSearch className="search-icon" />

                    <input
                        type="text"
                        placeholder="Search sprint..."
                        value={searchTerm}
                        onChange={(e) =>
                            setSearchTerm(
                                e.target.value
                            )
                        }
                    />
                </div>
            </div>

            {loading ? (
                <div className="loading">
                    Loading Sprints...
                </div>
            ) : filteredSprints.length === 0 ? (
                <div className="empty-state">
                    No Sprints Found
                </div>
            ) : (
                <table className="issue-table">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Project</th>
                            <th>Status</th>
                            <th>Start</th>
                            <th>End</th>
                            <th>Actions</th>
                        </tr>
                    </thead>

                    <tbody>
                        {filteredSprints.map(
                            (sprint) => {
                                const project =
                                    projects.find(
                                        (p) =>
                                            p.id ===
                                            sprint.project_id
                                    );

                                return (
                                    <tr
                                        key={sprint.id}
                                    >
                                        <td>
                                            {sprint.name}
                                        </td>

                                        <td>
                                            {project
                                                ?.name ||
                                                "N/A"}
                                        </td>

                                        <td>
                                            <span
                                                className={`status-badge status-${sprint.status.toLowerCase()}`}
                                            >
                                                {
                                                    sprint.status
                                                }
                                            </span>
                                        </td>

                                        <td>
                                            {new Date(
                                                sprint.start_date
                                            ).toLocaleDateString()}
                                        </td>

                                        <td>
                                            {new Date(
                                                sprint.end_date
                                            ).toLocaleDateString()}
                                        </td>

                                        <td className="action-buttons">
                                            <button
                                                className="icon-btn view-btn"
                                                onClick={() =>
                                                    openDetailsModal(
                                                        sprint
                                                    )
                                                }
                                            >
                                                <FaEye />
                                            </button>

                                            <button
                                                className="icon-btn edit-btn"
                                                onClick={() =>
                                                    openEditModal(
                                                        sprint
                                                    )
                                                }
                                            >
                                                <FaEdit />
                                            </button>

                                            {sprint.status ===
                                                "PLANNED" && (
                                                    <button
                                                        className="primary-btn small-btn"
                                                        onClick={() =>
                                                            handleStartSprint(
                                                                sprint.id
                                                            )
                                                        }
                                                    >
                                                        <FaPlay />
                                                    </button>
                                                )}

                                            {sprint.status ===
                                                "ACTIVE" && (
                                                    <button
                                                        className="primary-btn small-btn"
                                                        onClick={() =>
                                                            handleCompleteSprint(
                                                                sprint.id
                                                            )
                                                        }
                                                    >
                                                        <FaCheck />
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
                                Create Sprint
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

                        <SprintForm
                            projects={projects}
                            submitButtonText="Create Sprint"
                            onSubmit={
                                handleCreateSprint
                            }
                            loading={saving}
                        />
                    </div>
                </div>
            )}

            {showEditModal &&
                selectedSprint && (
                    <div className="modal-overlay">
                        <div className="modal">
                            <div className="modal-header">
                                <h2>
                                    Edit Sprint
                                </h2>

                                <button
                                    className="close-btn"
                                    onClick={() => {
                                        setShowEditModal(
                                            false
                                        );

                                        setSelectedSprint(
                                            null
                                        );
                                    }}
                                >
                                    ×
                                </button>
                            </div>

                            <SprintForm
                                projects={
                                    projects
                                }
                                defaultValues={
                                    selectedSprint
                                }
                                submitButtonText="Update Sprint"
                                onSubmit={
                                    handleEditSprint
                                }
                                loading={
                                    saving
                                }
                                isEdit
                            />
                        </div>
                    </div>
                )}
            {showDetailsModal &&
                selectedSprint && (
                    <div className="modal-overlay">
                        <div className="modal large-modal">
                            <div className="modal-header">
                                <h2>
                                    Sprint Details
                                </h2>

                                <button
                                    className="close-btn"
                                    onClick={() => {
                                        setShowDetailsModal(
                                            false
                                        );

                                        setSelectedSprint(
                                            null
                                        );

                                        setIssueId("");
                                    }}
                                >
                                    ×
                                </button>
                            </div>

                            <div className="sprint-details-grid">

                                <div className="sprint-detail-item">
                                    <span className="sprint-detail-label">
                                        Sprint Name
                                    </span>

                                    <span className="sprint-detail-value">
                                        {selectedSprint.name}
                                    </span>
                                </div>

                                <div className="sprint-detail-item">
                                    <span className="sprint-detail-label">
                                        Project
                                    </span>

                                    <span className="sprint-detail-value">
                                        {projects.find(
                                            (
                                                project
                                            ) =>
                                                project.id ===
                                                selectedSprint.project_id
                                        )?.name ||
                                            "N/A"}
                                    </span>
                                </div>

                                <div className="sprint-detail-item">
                                    <span className="sprint-detail-label">
                                        Status
                                    </span>

                                    <span className="sprint-detail-value">
                                        <span
                                            className={`status-badge status-${selectedSprint.status.toLowerCase()}`}
                                        >
                                            {
                                                selectedSprint.status
                                            }
                                        </span>
                                    </span>
                                </div>

                               <div className="sprint-detail-item">
                                    <span className="sprint-detail-label">
                                        Start Date
                                    </span>

                                    <span className="sprint-detail-value">
                                        {new Date(
                                            selectedSprint.start_date
                                        ).toLocaleString()}
                                    </span>
                                </div>

                                <div className="sprint-detail-item">
                                    <span className="sprint-detail-label">
                                        End Date
                                    </span>

                                    <span className="sprint-detail-value">
                                        {new Date(
                                            selectedSprint.end_date
                                        ).toLocaleString()}
                                    </span>
                                </div>

                                <div className="sprint-detail-item">
                                    <span className="sprint-detail-label">
                                        Created By
                                    </span>

                                    <span className="sprint-detail-value">
                                        {
                                            selectedSprint.created_by
                                        }
                                    </span>
                                </div>
                            </div>

                            <hr />

                            <div className="details-actions">

                                {selectedSprint.status ===
                                    "PLANNED" && (
                                        <button
                                            className="primary-btn"
                                            onClick={() =>
                                                handleStartSprint(
                                                    selectedSprint.id
                                                )
                                            }
                                        >
                                            <FaPlay />

                                            <span>
                                                Start Sprint
                                            </span>
                                        </button>
                                    )}

                                {selectedSprint.status ===
                                    "ACTIVE" && (
                                        <button
                                            className="primary-btn"
                                            onClick={() =>
                                                handleCompleteSprint(
                                                    selectedSprint.id
                                                )
                                            }
                                        >
                                            <FaCheck />

                                            <span>
                                                Complete Sprint
                                            </span>
                                        </button>
                                    )}

                            </div>

                            <hr />

                            <h3>Add Issue</h3>

                            <div className="toolbar">

                                <select
                                    value={issueId}
                                    onChange={(e) =>
                                        setIssueId(
                                            e.target.value
                                        )
                                    }
                                >
                                    <option value="">
                                        {availableIssues.length === 0
                                            ? "No Available Issues"
                                            : "Select Issue"}
                                    </option>

                                    {availableIssues.map(
                                        (issue) => (
                                            <option
                                                key={issue.id}
                                                value={issue.id}
                                            >
                                                {issue.title}
                                            </option>
                                        )
                                    )}
                                </select>

                                <button
                                    className="primary-btn"
                                    onClick={handleAddIssue}
                                    disabled={!issueId}
                                >
                                    Add Issue
                                </button>

                            </div>

                            <hr />

                            <h3>
                                Sprint Issues
                            </h3>

                            {selectedSprint
                                .issue_ids
                                ?.length ===
                                0 ? (
                                <div className="empty-state">
                                    No Issues
                                    Added
                                </div>
                            ) : (
                                <table className="issue-table">

                                    <thead>

                                        <tr>

                                            <th>Title</th>

                                            <th>Status</th>

                                            <th>Priority</th>

                                            <th>Action</th>

                                        </tr>

                                    </thead>

                                    <tbody>

                                        {selectedSprint.issue_ids.map(
                                            (issueId) => {

                                                const issue =
                                                    issues.find(
                                                        (i) =>
                                                            i.id === issueId
                                                    );

                                                if (!issue) {
                                                    return null;
                                                }

                                                return (

                                                    <tr key={issue.id}>

                                                        <td>
                                                            {issue.title}
                                                        </td>

                                                        <td>

                                                            <span
                                                                className={`status-badge status-${issue.status.toLowerCase()}`}
                                                            >
                                                                {issue.status}
                                                            </span>

                                                        </td>

                                                        <td>

                                                            <span
                                                                className={`priority-badge priority-${issue.priority.toLowerCase()}`}
                                                            >
                                                                {issue.priority}
                                                            </span>

                                                        </td>

                                                        <td>

                                                            <button
                                                                className="primary-btn small-btn"
                                                                onClick={() =>
                                                                    handleRemoveIssue(
                                                                        issue.id
                                                                    )
                                                                }
                                                            >
                                                                Remove
                                                            </button>

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
                        </div>
                    </div>
                )}

        </main>
    );
};

export default Sprints;