import { useEffect, useMemo, useState } from "react";

import {
    FaFolder,
    FaBug,
    FaFlag,
    FaPlayCircle,
} from "react-icons/fa";

import "./Dashboard.css";

import projectService from "../../services/projectService";
import issueService from "../../services/issueService";
import sprintService from "../../services/sprintService";

const Dashboard = () => {
    const [projects, setProjects] = useState([]);
    const [issues, setIssues] = useState([]);
    const [sprints, setSprints] = useState([]);

    const [loading, setLoading] = useState(true);

    const loadDashboard = async () => {
        try {
            setLoading(true);

            const [
                projectsResponse,
                issuesResponse,
                sprintsResponse,
            ] = await Promise.all([
                projectService.getAllProjects(),
                issueService.getAllIssues(),
                sprintService.getAllSprints(),
            ]);

            setProjects(projectsResponse);
            setIssues(issuesResponse);
            setSprints(sprintsResponse);
        } catch (error) {
            alert(
                error?.response?.data?.detail ||
                "Unable to load dashboard."
            );
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        loadDashboard();
    }, []);

    const totalProjects = projects.length;

    const totalIssues = issues.length;

    const totalSprints = sprints.length;

    const activeSprints = useMemo(() => {
        return sprints.filter(
            (sprint) =>
                sprint.status === "ACTIVE"
        ).length;
    }, [sprints]);

    const recentProjects = useMemo(() => {
        return [...projects]
            .reverse()
            .slice(0, 5);
    }, [projects]);

    const recentIssues = useMemo(() => {
        return [...issues]
            .reverse()
            .slice(0, 5);
    }, [issues]);

    const recentSprints = useMemo(() => {
        return [...sprints]
            .reverse()
            .slice(0, 5);
    }, [sprints]);

    if (loading) {
        return (
            <div className="loading">
                Loading Dashboard...
            </div>
        );
    }

    return (
        <main className="dashboard-page">
            <div className="dashboard-header">
                <div>
                    <h1>Dashboard</h1>

                    <p>
                        Overview of your
                        projects, issues and
                        sprints
                    </p>
                </div>
            </div>

            <div className="dashboard-stats">

                <div className="stat-card">
                    <div className="stat-icon">
                        <FaFolder />
                    </div>

                    <div className="stat-content">
                        <h3>
                            Total Projects
                        </h3>

                        <span>
                            {totalProjects}
                        </span>
                    </div>
                </div>

                <div className="stat-card">
                    <div className="stat-icon">
                        <FaBug />
                    </div>

                    <div className="stat-content">
                        <h3>
                            Total Issues
                        </h3>

                        <span>
                            {totalIssues}
                        </span>
                    </div>
                </div>

                <div className="stat-card">
                    <div className="stat-icon">
                        <FaFlag />
                    </div>

                    <div className="stat-content">
                        <h3>
                            Total Sprints
                        </h3>

                        <span>
                            {totalSprints}
                        </span>
                    </div>
                </div>

                <div className="stat-card">
                    <div className="stat-icon">
                        <FaPlayCircle />
                    </div>

                    <div className="stat-content">
                        <h3>
                            Active Sprints
                        </h3>

                        <span>
                            {activeSprints}
                        </span>
                    </div>
                </div>

            </div>
                         <section className="dashboard-section">
                            <div className="section-header">
                                <h2>Recent Projects</h2>
                            </div>
                        
                            <div className="dashboard-card-list">
                                {recentProjects.length === 0 ? (
                                    <div className="empty-state">
                                        No Projects Found
                                    </div>
                                ) : (
                                    recentProjects.map((project) => (
                                        <div
                                            key={project.id}
                                            className="dashboard-item-card"
                                        >
                                            <div className="dashboard-item-top">
                                                <h3>{project.name}</h3>
                                            </div>
                        
                                            <p className="dashboard-description">
                                                {project.description}
                                            </p>
                        
                                            <div className="dashboard-meta">
                                                <span>
                                                    <strong>Owner:</strong>{" "}
                                                    {project.owner_id}
                                                </span>
                        
                                                <span>
                                                    <strong>Members:</strong>{" "}
                                                    {project.members.length}
                                                </span>
                                            </div>
                                        </div>
                                    ))
                                )}
                            </div>
                        </section>

            <section className="dashboard-section">
                <div className="section-header">
                    <h2>Recent Issues</h2>
                </div>
            
                <div className="dashboard-card-list">
                    {recentIssues.length === 0 ? (
                        <div className="empty-state">
                            No Issues Found
                        </div>
                    ) : (
                        recentIssues.map((issue) => (
                            <div
                                key={issue.id}
                                className="dashboard-item-card"
                            >
                                <div className="dashboard-item-top">
                                    <h3>{issue.title}</h3>
            
                                    <span
                                        className={`badge ${issue.priority.toLowerCase()}`}
                                    >
                                        {issue.priority}
                                    </span>
                                </div>
            
                                <div className="dashboard-meta">
                                    <span>
                                        <strong>Status:</strong>{" "}
                                        {issue.status}
                                    </span>
            
                                    <span>
                                        <strong>Project:</strong>{" "}
                                        {issue.project_id}
                                    </span>
                                </div>
                            </div>
                        ))
                    )}
                </div>
            </section>

            <section className="dashboard-section">
                <div className="section-header">
                    <h2>Recent Sprints</h2>
                </div>
            
                <div className="dashboard-card-list">
                    {recentSprints.length === 0 ? (
                        <div className="empty-state">
                            No Sprints Found
                        </div>
                    ) : (
                        recentSprints.map((sprint) => (
                            <div
                                key={sprint.id}
                                className="dashboard-item-card"
                            >
                                <div className="dashboard-item-top">
                                    <h3>{sprint.name}</h3>
            
                                    <span
                                        className={`badge ${sprint.status.toLowerCase()}`}
                                    >
                                        {sprint.status}
                                    </span>
                                </div>
            
                                <div className="dashboard-meta">
                                    <span>
                                        <strong>Start:</strong>{" "}
                                        {sprint.start_date
                                            ? new Date(
                                                  sprint.start_date
                                              ).toLocaleDateString()
                                            : "-"}
                                    </span>
            
                                    <span>
                                        <strong>End:</strong>{" "}
                                        {sprint.end_date
                                            ? new Date(
                                                  sprint.end_date
                                              ).toLocaleDateString()
                                            : "-"}
                                    </span>
                                </div>
                            </div>
                        ))
                    )}
                </div>
            </section>

        </main>
    );
};

export default Dashboard;