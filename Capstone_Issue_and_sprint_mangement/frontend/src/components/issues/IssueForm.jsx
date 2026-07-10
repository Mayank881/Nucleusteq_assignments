import { useForm } from "react-hook-form";

function IssueForm({
    projects = [],
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
        formState: { errors },
    } = useForm({
        defaultValues,
    });

    return (
        <form
            className="project-form"
            onSubmit={handleSubmit(onSubmit)}
        >
            <div className="form-group">
                <label>Project</label>

                <select
                    {...register("projectId", {
                        required: "Project is required",
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
                        required: "Title is required",
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
                    {...register("description", {
                        required:
                            "Description is required",
                    })}
                />

                {errors.description && (
                    <p className="form-error">
                        {errors.description.message}
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
                <label>Assignee ID (Optional)</label>

                <input
                    type="text"
                    placeholder="Enter Assignee ID"
                    {...register("assignee_id")}
                />
            </div>

            <div className="form-group">
                <label>Parent Issue ID (Optional)</label>

                <input
                    type="text"
                    placeholder="Enter Parent Issue ID"
                    {...register("parent_id")}
                />
            </div>

            <button
                className="btn-primary"
                type="submit"
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