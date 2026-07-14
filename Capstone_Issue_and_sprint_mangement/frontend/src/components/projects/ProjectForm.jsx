import { useForm } from "react-hook-form";

function ProjectForm({
    defaultValues = {
        name: "",
        description: "",
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
                <label>Project Name</label>

                <input
                    type="text"
                    placeholder="Enter project name"
                    {...register("name", {
                        required: "Project name is required",
                    })}
                />

                {errors.name && (
                    <p className="form-error">
                        {errors.name.message}
                    </p>
                )}
            </div>

            <div className="form-group">
                <label>Description</label>

                <textarea
                    rows="5"
                    placeholder="Enter project description"
                    {...register("description", {
                        required: "Description is required",
                    })}
                />

                {errors.description && (
                    <p className="form-error">
                        {errors.description.message}
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

export default ProjectForm;