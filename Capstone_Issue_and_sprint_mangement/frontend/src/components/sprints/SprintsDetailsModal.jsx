function SprintDetailsModal({
    sprint,
    onClose,
    onAddIssue,
    onRemoveIssue,
    onStartSprint,
    onCompleteSprint,
    loading = false,
}) {
    if (!sprint) {
        return null;
    }

    return (
        <div className="modal-overlay">
            <div className="modal large-modal">
                <div className="modal-header">
                    <h2>Sprint Details</h2>

                    <button
                        className="close-btn"
                        onClick={onClose}
                    >
                        ✕
                    </button>
                </div>

                <div className="details-grid">
                    <div>
                        <strong>Name</strong>
                        <p>{sprint.name}</p>
                    </div>

                    <div>
                        <strong>Status</strong>

                        <span
                            className={`status-badge status-${sprint.status.toLowerCase()}`}
                        >
                            {sprint.status}
                        </span>
                    </div>

                    <div>
                        <strong>Project ID</strong>
                        <p>{sprint.project_id}</p>
                    </div>

                    <div>
                        <strong>Created By</strong>
                        <p>{sprint.created_by}</p>
                    </div>

                    <div>
                        <strong>Start Date</strong>

                        <p>
                            {new Date(
                                sprint.start_date
                            ).toLocaleString()}
                        </p>
                    </div>

                    <div>
                        <strong>End Date</strong>

                        <p>
                            {new Date(
                                sprint.end_date
                            ).toLocaleString()}
                        </p>
                    </div>

                    <div>
                        <strong>Created At</strong>

                        <p>
                            {new Date(
                                sprint.created_at
                            ).toLocaleString()}
                        </p>
                    </div>

                    <div>
                        <strong>Updated At</strong>

                        <p>
                            {new Date(
                                sprint.updated_at
                            ).toLocaleString()}
                        </p>
                    </div>
                </div>

                <div className="details-actions">
                    {sprint.status === "PLANNED" && (
                        <button
                            className="btn-primary"
                            onClick={() =>
                                onStartSprint(
                                    sprint.id
                                )
                            }
                            disabled={loading}
                        >
                            Start Sprint
                        </button>
                    )}

                    {sprint.status === "ACTIVE" && (
                        <button
                            className="btn-success"
                            onClick={() =>
                                onCompleteSprint(
                                    sprint.id
                                )
                            }
                            disabled={loading}
                        >
                            Complete Sprint
                        </button>
                    )}

                    <button
                        className="btn-secondary"
                        onClick={() =>
                            onAddIssue(
                                sprint.id
                            )
                        }
                    >
                        Add Issue
                    </button>
                </div>

                <hr />

                <h3>Issues</h3>

                {sprint.issue_ids.length === 0 ? (
                    <p>
                        No issues added to this sprint.
                    </p>
                ) : (
                    <table className="project-table">
                        <thead>
                            <tr>
                                <th>Issue ID</th>
                                <th>Action</th>
                            </tr>
                        </thead>

                        <tbody>
                            {sprint.issue_ids.map(
                                (
                                    issueId
                                ) => (
                                    <tr
                                        key={
                                            issueId
                                        }
                                    >
                                        <td>
                                            {
                                                issueId
                                            }
                                        </td>

                                        <td>
                                            <button
                                                className="btn-danger"
                                                onClick={() =>
                                                    onRemoveIssue(
                                                        sprint.id,
                                                        issueId
                                                    )
                                                }
                                                disabled={
                                                    loading
                                                }
                                            >
                                                Remove
                                            </button>
                                        </td>
                                    </tr>
                                )
                            )}
                        </tbody>
                    </table>
                )}
            </div>
        </div>
    );
}

export default SprintDetailsModal;