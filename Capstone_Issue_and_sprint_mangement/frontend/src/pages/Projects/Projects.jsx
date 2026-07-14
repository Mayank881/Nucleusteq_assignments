import { useEffect, useMemo, useState } from "react";
import {
    FaEdit,
    FaEye,
    FaPlus,
    FaSearch,
    FaTrash,
    FaUserPlus,
    FaUserMinus,
} from "react-icons/fa";

import "./Projects.css";

import ProjectForm from "../../components/projects/ProjectForm";

import projectService from "../../services/projectService";
import userService from "../../services/userService";

const Projects = () => {
    const [projects, setProjects] = useState([]);
    const [users, setUsers] = useState([]);

    const [selectedProject, setSelectedProject] =
        useState(null);

    const [selectedUser, setSelectedUser] =
        useState("");

    const [loading, setLoading] =
        useState(true);

    const [saving, setSaving] =
        useState(false);

    const [searchTerm, setSearchTerm] =
        useState("");

    const [showCreateModal, setShowCreateModal] =
        useState(false);

    const [showEditModal, setShowEditModal] =
        useState(false);

    const [showDetailsModal, setShowDetailsModal] =
        useState(false);

    const loadProjects = async () => {
        try {
            setLoading(true);

            const response =
                await projectService.getAllProjects();

            setProjects(response);
        } catch (error) {
            alert(
                error?.response?.data?.detail ||
                "Unable to load projects."
            );
        } finally {
            setLoading(false);
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

    useEffect(() => {
        loadProjects();
        loadUsers();
    }, []);

    const filteredProjects = useMemo(() => {
        return projects.filter((project) => {
            const keyword =
                searchTerm.toLowerCase();

            return (
                project.name
                    .toLowerCase()
                    .includes(keyword) ||
                project.description
                    .toLowerCase()
                    .includes(keyword)
            );
        });
    }, [projects, searchTerm]);

    const getUserName = (userId) => {
        const user = users.find(
            (u) => u.id === userId
        );

        return user ? user.name : userId;
    };

    const availableUsers = selectedProject
        ? users.filter(
              (user) =>
                  !selectedProject.members.includes(
                      user.id
                  )
          )
        : [];

    const handleCreateProject = async (
        formData
    ) => {
        try {
            setSaving(true);

            await projectService.createProject(
                formData
            );

            setShowCreateModal(false);

            await loadProjects();
        } catch (error) {
            alert(
                error?.response?.data?.detail ||
                "Unable to create project."
            );
        } finally {
            setSaving(false);
        }
    };

    const openEditModal = (project) => {
        setSelectedProject(project);
        setShowEditModal(true);
    };

    const openDetailsModal = (project) => {
        setSelectedProject(project);
        setSelectedUser("");
        setShowDetailsModal(true);
    };

    const handleDeleteProject = async (
        projectId
    ) => {
        const confirmDelete =
            window.confirm(
                "Are you sure you want to delete this project?"
            );

        if (!confirmDelete) {
            return;
        }

        try {
            await projectService.deleteProject(
                projectId
            );

            await loadProjects();
        } catch (error) {
            alert(
                error?.response?.data?.detail ||
                "Unable to delete project."
            );
        }
    };

    const handleAddMember = async () => {
        if (!selectedUser) {
            alert("Please select a user.");
            return;
        }

        try {
            const updatedProject =
                await projectService.addMember(
                    selectedProject.id,
                    selectedUser
                );

            setSelectedProject(updatedProject);

            setProjects((prev) =>
                prev.map((project) =>
                    project.id ===
                    updatedProject.id
                        ? updatedProject
                        : project
                )
            );

            setSelectedUser("");
        } catch (error) {
            alert(
                error?.response?.data?.detail ||
                "Unable to add member."
            );
        }
    };

    const handleRemoveMember = async (
        userId
    ) => {
        const confirmRemove =
            window.confirm(
                "Remove this member?"
            );

        if (!confirmRemove) {
            return;
        }

        try {
            const updatedProject =
                await projectService.removeMember(
                    selectedProject.id,
                    userId
                );

            setSelectedProject(updatedProject);

            setProjects((prev) =>
                prev.map((project) =>
                    project.id ===
                    updatedProject.id
                        ? updatedProject
                        : project
                )
            );
        } catch (error) {
            alert(
                error?.response?.data?.detail ||
                "Unable to remove member."
            );
        }
    };

    return (
                 <main className="projects-page">
            <div className="projects-header">
                <div>
                    <h1>Projects</h1>
                    <p>
                        Manage all your projects
                    </p>
                </div>

                <button
                    className="primary-btn"
                    onClick={() =>
                        setShowCreateModal(true)
                    }
                >
                    <FaPlus />
                    <span>Create Project</span>
                </button>
            </div>

            <div className="search-container">
                <FaSearch className="search-icon" />

                <input
                    type="text"
                    placeholder="Search project..."
                    value={searchTerm}
                    onChange={(e) =>
                        setSearchTerm(
                            e.target.value
                        )
                    }
                />
            </div>

            {loading ? (
                <div className="loading">
                    Loading Projects...
                </div>
            ) : filteredProjects.length === 0 ? (
                <div className="empty-state">
                    No Projects Found
                </div>
            ) : (
                <table className="project-table">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Description</th>
                            <th>Owner</th>
                            <th>Members</th>
                            <th>Actions</th>
                        </tr>
                    </thead>

                    <tbody>
                        {filteredProjects.map(
                            (project) => (
                                <tr key={project.id}>
                                    <td>
                                        {project.name}
                                    </td>

                                    <td>
                                        {project.description}
                                    </td>

                                    <td>
                                        {getUserName(
                                            project.owner_id
                                        )}
                                    </td>

                                    <td>
                                        {
                                            project.members
                                                .length
                                        }
                                    </td>

                                    <td className="action-buttons">
                                        <button
                                            className="icon-btn view-btn"
                                            onClick={() =>
                                                openDetailsModal(
                                                    project
                                                )
                                            }
                                        >
                                            <FaEye />
                                        </button>

                                        <button
                                            className="icon-btn edit-btn"
                                            onClick={() =>
                                                openEditModal(
                                                    project
                                                )
                                            }
                                        >
                                            <FaEdit />
                                        </button>

                                        <button
                                            className="icon-btn delete-btn"
                                            onClick={() =>
                                                handleDeleteProject(
                                                    project.id
                                                )
                                            }
                                        >
                                            <FaTrash />
                                        </button>
                                    </td>
                                </tr>
                            )
                        )}
                    </tbody>
                </table>
            )}

            {showCreateModal && (
                <div className="modal-overlay">
                    <div className="modal">
                        <div className="modal-header">
                            <h2>
                                Create Project
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

                        <ProjectForm
                            submitButtonText="Create Project"
                            onSubmit={
                                handleCreateProject
                            }
                            loading={saving}
                        />
                    </div>
                </div>
            )}

            {showEditModal && (
                <div className="modal-overlay">
                    <div className="modal">
                        <div className="modal-header">
                            <h2>
                                Edit Project
                            </h2>

                            <button
                                className="close-btn"
                                onClick={() =>
                                    setShowEditModal(
                                        false
                                    )
                                }
                            >
                                ×
                            </button>
                        </div>

                        <ProjectForm
                            defaultValues={{
                                name:
                                    selectedProject?.name,
                                description:
                                    selectedProject?.description,
                            }}
                            submitButtonText="Update Project"
                            loading={saving}
                            onSubmit={async (
                                formData
                            ) => {
                                try {
                                    setSaving(
                                        true
                                    );

                                    await projectService.updateProject(
                                        selectedProject.id,
                                        formData
                                    );

                                    setShowEditModal(
                                        false
                                    );

                                    setSelectedProject(
                                        null
                                    );

                                    await loadProjects();
                                } catch (
                                    error
                                ) {
                                    alert(
                                        error
                                            ?.response
                                            ?.data
                                            ?.detail ||
                                            "Unable to update project."
                                    );
                                } finally {
                                    setSaving(
                                        false
                                    );
                                }
                            }}
                        />
                    </div>
                </div>
            )}

                    {showDetailsModal && selectedProject && (
                <div className="modal-overlay">
                    <div className="modal">
                        <div className="modal-header">
                            <h2>Project Details</h2>

                            <button
                                className="close-btn"
                                onClick={() => {
                                    setShowDetailsModal(false);
                                    setSelectedProject(null);
                                    setSelectedUser("");
                                }}
                            >
                                ×
                            </button>
                        </div>

                        <div className="project-details">

                            <div className="detail-item">
                                <span className="detail-label">
                                    Project Name
                                </span>

                                <span className="detail-value">
                                    {selectedProject.name}
                                </span>
                            </div>

                            <div className="detail-item">
                                <span className="detail-label">
                                    Description
                                </span>

                                <span className="detail-value">
                                    {selectedProject.description}
                                </span>
                            </div>

                            <div className="detail-item">
                                <span className="detail-label">
                                    Owner
                                </span>

                                <span className="detail-value">
                                    {getUserName(
                                        selectedProject.owner_id
                                    )}
                                </span>
                            </div>

                            <div className="detail-item">
                                <span className="detail-label">
                                    Total Members
                                </span>

                                <span className="detail-value">
                                    {
                                        selectedProject.members
                                            .length
                                    }
                                </span>
                            </div>

                            <hr />

                            <div className="members-list">
                                <h3>
                                    Project Members
                                </h3>

                                {selectedProject.members
                                    .length === 0 ? (
                                    <p>
                                        No members found.
                                    </p>
                                ) : (
                                    <ul>
                                        {selectedProject.members.map(
                                            (
                                                memberId
                                            ) => (
                                                <li
                                                    key={
                                                        memberId
                                                    }
                                                    className="member-item"
                                                >
                                                    <span>
                                                        {getUserName(
                                                            memberId
                                                        )}
                                                    </span>

                                                    {memberId !==
                                                        selectedProject.owner_id && (
                                                        <button
                                                            className="icon-btn delete-btn"
                                                            onClick={() =>
                                                                handleRemoveMember(
                                                                    memberId
                                                                )
                                                            }
                                                            title="Remove Member"
                                                        >
                                                            <FaUserMinus />
                                                        </button>
                                                    )}
                                                </li>
                                            )
                                        )}
                                    </ul>
                                )}

                            </div>

                            <hr />

                            <div className="add-member-section">
                                <h3>
                                    Add Member
                                </h3>

                                <select
                                    value={
                                        selectedUser
                                    }
                                    onChange={(e) =>
                                        setSelectedUser(
                                            e.target
                                                .value
                                        )
                                    }
                                >
                                    <option value="">
                                        Select User
                                    </option>

                                    {availableUsers.map(
                                        (user) => (
                                            <option
                                                key={
                                                    user.id
                                                }
                                                value={
                                                    user.id
                                                }
                                            >
                                                {
                                                    user.name
                                                }
                                                {" - "}
                                                {
                                                    user.email
                                                }
                                            </option>
                                        )
                                    )}
                                </select>

                                <button
                                    className="primary-btn"
                                    onClick={
                                        handleAddMember
                                    }
                                >
                                    <FaUserPlus />

                                    <span>
                                        Add Member
                                    </span>
                                </button>
                            </div>
                       </div>
                    </div>
                </div>
            )}
        </main>
    );
};

export default Projects;