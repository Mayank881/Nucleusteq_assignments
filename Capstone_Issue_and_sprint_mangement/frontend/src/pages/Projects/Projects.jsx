import { useEffect, useMemo, useState } from "react";
import { FaEdit, FaEye, FaPlus, FaSearch, FaTrash } from "react-icons/fa";

import "./Projects.css";

import ProjectForm from "../../components/projects/ProjectForm";
import projectService from "../../services/projectService";

const Projects = () => {
    const [projects, setProjects] = useState([]);
    const [selectedProject, setSelectedProject] = useState(null);

    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);

    const [searchTerm, setSearchTerm] = useState("");

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

    useEffect(() => {
        loadProjects();
    }, []);

    const filteredProjects = useMemo(() => {
        return projects.filter((project) => {
            const keyword = searchTerm.toLowerCase();

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

    const handleCreateProject = async (formData) => {
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
        setShowDetailsModal(true);
    };

    const handleDeleteProject = async (
        projectId
    ) => {
        const confirmDelete = window.confirm(
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
                                        {project.owner_id}
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
                                    {selectedProject.owner_id}
                                </span>
                            </div>

                            <div className="detail-item">
                                <span className="detail-label">
                                    Members
                                </span>

                                <span className="detail-value">
                                    {selectedProject.members.length}
                                </span>
                            </div>

                            <div className="members-list">
                                <h3>Member IDs</h3>

                                <ul>
                                    {selectedProject.members.map(
                                        (member) => (
                                            <li key={member}>
                                                {member}
                                            </li>
                                        )
                                    )}
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </main>
    );
};

export default Projects;