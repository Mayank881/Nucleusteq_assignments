import { useForm } from "react-hook-form";

function SprintForm({
    projects = [],
    defaultValues = {
        projectId: "",
        name: "",
        start_date: "",
        end_date: "",
    },
    onSubmit,
    submitButtonText,
    loading = false,
    isEdit = false,
}) {
    const {
        register,
        handleSubmit,
        watch,
        formState: { errors },
    } = useForm({
        defaultValues,
    });

    const startDate = watch("start_date");

    return (
        <form
            className="project-form"
            onSubmit={handleSubmit(onSubmit)}
        >
            <div className="form-group">
                <label>Project</label>

                <select
                    disabled={isEdit}
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
                <label>Sprint Name</label>

                <input
                    type="text"
                    placeholder="Enter sprint name"
                    {...register("name", {
                        required: "Sprint name is required",
                        minLength: {
                            value: 3,
                            message:
                                "Sprint name must be at least 3 characters",
                        },
                    })}
                />

                {errors.name && (
                    <p className="form-error">
                        {errors.name.message}
                    </p>
                )}
            </div>

            <div className="form-group">
                <label>Start Date</label>

                <input
                    type="datetime-local"
                    {...register("start_date", {
                        required: "Start date is required",
                    })}
                />

                {errors.start_date && (
                    <p className="form-error">
                        {errors.start_date.message}
                    </p>
                )}
            </div>

            <div className="form-group">
                <label>End Date</label>

                <input
                    type="datetime-local"
                    {...register("end_date", {
                        required: "End date is required",
                        validate: (value) =>
                            new Date(value) >
                                new Date(startDate) ||
                            "End date must be after start date",
                    })}
                />

                {errors.end_date && (
                    <p className="form-error">
                        {errors.end_date.message}
                    </p>
                )}
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

export default SprintForm;