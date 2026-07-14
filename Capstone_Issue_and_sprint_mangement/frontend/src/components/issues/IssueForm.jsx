import { useEffect, useMemo, useState } from "react";
import { useForm } from "react-hook-form";

import projectService from "../../services/projectService";

function IssueForm({
    projects = [],
    users = [],
    issues = [],
    defaultValues = {
        projectId: "",
        title: "",
        description: "",
        type: "Task",
        priority: "Medium",
        assignee_id: "",
        parent_id: "",
    },
    onSubmit,
    submitButtonText,
    loading = false,
}) {
    const {
        register,
        handleSubmit,
        watch,
        resetField,
        formState: { errors },
    } = useForm({
        defaultValues,
    });

    const selectedProject =
        watch("projectId");

    const [projectMembers, setProjectMembers] =
        useState([]);

    const filteredParentIssues =
        useMemo(() => {

            if (!selectedProject) {
                return [];
            }

            return issues.filter(
                (issue) =>
                    issue.project_id ===
                    selectedProject
            );

        }, [
            issues,
            selectedProject,
        ]);

    useEffect(() => {

        const loadMembers =
            async () => {

                if (!selectedProject) {

                    setProjectMembers([]);

                    resetField(
                        "assignee_id"
                    );

                    resetField(
                        "parent_id"
                    );

                    return;
                }

                try {

                    const project =
                        await projectService.getProjectById(
                            selectedProject
                        );

                    const members =
                        users.filter(
                            (user) =>
                                project.members.includes(
                                    user.id
                                )
                        );

                    setProjectMembers(
                        members
                    );

                    resetField(
                        "assignee_id"
                    );

                    resetField(
                        "parent_id"
                    );

                } catch (error) {

                    console.error(
                        error
                    );

                    setProjectMembers(
                        []
                    );
                }
            };

        loadMembers();

    }, [
        selectedProject,
        users,
        resetField,
    ]);
        return (
        <form
            className="project-form"
            onSubmit={handleSubmit(onSubmit)}
        >
            <div className="form-group">
                <label>Project</label>

                <select
                    {...register("projectId", {
                        required:
                            "Project is required",
                    })}
                >
                    <option value="">
                        Select Project
                    </option>

                    {projects.map((project) => (
                        <option
                            key={project.id}
                            value={project.id}
                        >
                            {project.name}
                        </option>
                    ))}
                </select>

                {errors.projectId && (
                    <p className="form-error">
                        {errors.projectId.message}
                    </p>
                )}
            </div>

            <div className="form-group">
                <label>Title</label>

                <input
                    type="text"
                    placeholder="Enter issue title"
                    {...register("title", {
                        required:
                            "Title is required",
                    })}
                />

                {errors.title && (
                    <p className="form-error">
                        {errors.title.message}
                    </p>
                )}
            </div>

            <div className="form-group">
                <label>Description</label>

                <textarea
                    rows="5"
                    placeholder="Enter issue description"
                    {...register(
                        "description",
                        {
                            required:
                                "Description is required",
                        }
                    )}
                />

                {errors.description && (
                    <p className="form-error">
                        {
                            errors.description
                                .message
                        }
                    </p>
                )}
            </div>

            <div className="form-group">
                <label>Issue Type</label>

                <select
                    {...register("type")}
                >
                    <option value="Task">
                        Task
                    </option>

                    <option value="Bug">
                        Bug
                    </option>

                    <option value="Story">
                        Story
                    </option>
                </select>
            </div>

            <div className="form-group">
                <label>Priority</label>

                <select
                    {...register("priority")}
                >
                    <option value="Low">
                        Low
                    </option>

                    <option value="Medium">
                        Medium
                    </option>

                    <option value="High">
                        High
                    </option>
                </select>
            </div>

            <div className="form-group">
                <label>Assignee</label>

                <select
                    {...register(
                        "assignee_id"
                    )}
                    disabled={
                        !selectedProject
                    }
                >
                    <option value="">
                        Unassigned
                    </option>

                    {projectMembers.map(
                        (member) => (
                            <option
                                key={
                                    member.id
                                }
                                value={
                                    member.id
                                }
                            >
                                {
                                    member.name
                                }
                            </option>
                        )
                    )}
                </select>
            </div>

            <div className="form-group">
                <label>
                    Parent Issue
                </label>

                <select
                    {...register(
                        "parent_id"
                    )}
                    disabled={
                        !selectedProject
                    }
                >
                    <option value="">
                        None
                    </option>

                    {filteredParentIssues.map(
                        (issue) => (
                            <option
                                key={
                                    issue.id
                                }
                                value={
                                    issue.id
                                }
                            >
                                {
                                    issue.title
                                }
                            </option>
                        )
                    )}
                </select>
            </div>

            <button
                type="submit"
                className="btn-primary"
                disabled={loading}
            >
                {loading
                    ? "Please Wait..."
                    : submitButtonText}
            </button>
        </form>
    );
}

export default IssueForm;