import "./ConfirmDialog.css";

function ConfirmDialog({
    title = "Confirm",
    message,
    confirmText = "Delete",
    cancelText = "Cancel",
    onConfirm,
    onCancel,
    loading = false,
}) {
    return (
        <div className="confirm-overlay">
            <div className="confirm-dialog">
                <h2>{title}</h2>

                <p>{message}</p>

                <div className="confirm-actions">
                    <button
                        className="cancel-btn"
                        onClick={onCancel}
                        disabled={loading}
                    >
                        {cancelText}
                    </button>

                    <button
                        className="delete-btn"
                        onClick={onConfirm}
                        disabled={loading}
                    >
                        {loading
                            ? "Deleting..."
                            : confirmText}
                    </button>
                </div>
            </div>
        </div>
    );
}

export default ConfirmDialog;