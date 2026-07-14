import { useForm } from "react-hook-form";

function AddIssueModal({
    sprintId,
    loading = false,
    onSubmit,
    onClose,
}) {
    const {
        register,
        handleSubmit,
        reset,
        formState: { errors },
    } = useForm({
        defaultValues: {
            issueId: "",
        },
    });

    const handleFormSubmit = (data) => {
        onSubmit(
            sprintId,
            data.issueId
        );

        reset();
    };

    return (
        <div className="modal-overlay">
            <div className="modal">
                <div className="modal-header">
                    <h2>Add Issue To Sprint</h2>

                    <button
                        className="close-btn"
                        onClick={onClose}
                    >
                        ✕
                    </button>
                </div>

                <form
                    className="project-form"
                    onSubmit={handleSubmit(
                        handleFormSubmit
                    )}
                >
                    <div className="form-group">
                        <label>
                            Issue ID
                        </label>

                        <input
                            type="text"
                            placeholder="Enter Issue ID"
                            {...register(
                                "issueId",
                                {
                                    required:
                                        "Issue ID is required",
                                }
                            )}
                        />

                        {errors.issueId && (
                            <p className="form-error">
                                {
                                    errors
                                        .issueId
                                        .message
                                }
                            </p>
                        )}
                    </div>

                    <div className="modal-actions">
                        <button
                            type="submit"
                            className="btn-primary"
                            disabled={loading}
                        >
                            {loading
                                ? "Please Wait..."
                                : "Add Issue"}
                        </button>

                        <button
                            type="button"
                            className="btn-secondary"
                            onClick={onClose}
                        >
                            Cancel
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default AddIssueModal;