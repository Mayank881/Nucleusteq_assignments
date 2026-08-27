
import { useEffect, useState } from "react";

import commentService from "../../services/commentService";

function CommentSection({
    issueId,
    comments,
    currentUser,
    users,
    loading,
    refreshComments,
}) {
    const [newComment, setNewComment] =
        useState("");

    const [editingCommentId, setEditingCommentId] =
        useState(null);

    const [editedContent, setEditedContent] =
        useState("");

    const [saving, setSaving] =
        useState(false);

    const [commentList, setCommentList] =
        useState([]);
    
    useEffect(() => {
        setCommentList(comments || []);
    }, [comments]);


    const getUserName = (userId) => {
        const user = users.find(
            (u) => u.id === userId
        );
    
        return user
            ? user.name
            : "Unknown User";
        };

    const handleCreateComment =
        async () => {
            if (!newComment.trim()) {
                return;
            }

            try {
                setSaving(true);

                await commentService.createComment(
                    issueId,
                    {
                        content:
                            newComment,
                    }
                );

                setNewComment("");

                await refreshComments();

            } catch (error) {

                alert(
                    error?.response?.data
                        ?.detail ||
                        "Unable to add comment."
                );

            } finally {
                setSaving(false);
            }
        };

    const startEditing =
        (comment) => {

            setEditingCommentId(
                comment.id
            );

            setEditedContent(
                comment.content
            );
        };

    const cancelEditing =
        () => {

            setEditingCommentId(
                null
            );

            setEditedContent("");
        };

    const saveComment =
        async (
            commentId
        ) => {

            if (
                !editedContent.trim()
            ) {
                return;
            }

            try {

                setSaving(true);

                await commentService.updateComment(
                    commentId,
                    {
                        content:
                            editedContent,
                    }
                );

                setEditingCommentId(
                    null
                );

                setEditedContent(
                    ""
                );

                await refreshComments();

            } catch (error) {

                alert(
                    error?.response?.data
                        ?.detail ||
                        "Unable to update comment."
                );

            } finally {

                setSaving(false);

            }
        };

    const deleteComment =
        async (
            commentId
        ) => {

            const confirmDelete =
                window.confirm(
                    "Delete this comment?"
                );

            if (
                !confirmDelete
            ) {
                return;
            }

            try {

                await commentService.deleteComment(
                    commentId
                );

                await refreshComments();

            } catch (error) {

                alert(
                    error?.response?.data
                        ?.detail ||
                        "Unable to delete comment."
                );
            }
        };
            return (
        <div className="comment-section">

            <h3>Comments</h3>

            {loading ? (
                <p>Loading comments...</p>
            ) : (
                <>
                    <div className="comment-form">

                        <textarea
                            rows="3"
                            placeholder="Write a comment..."
                            value={newComment}
                            onChange={(e) =>
                                setNewComment(
                                    e.target.value
                                )
                            }
                        />

                        <button
                            className="primary-btn"
                            disabled={saving}
                            onClick={
                                handleCreateComment
                            }
                        >
                            Add Comment
                        </button>

                    </div>

                    {commentList.length === 0 ? (
                        <div className="empty-state">
                            No comments yet.
                        </div>
                    ) : (
                        commentList.map(
                            (comment) => (
                                <div
                                    key={comment.id}
                                    className="comment-card"
                                >
                                    <div className="comment-header">

                                        <strong>
                                            {currentUser &&
                                            currentUser.id === comment.user_id
                                                ? "You"
                                                : getUserName(
                                                      comment.user_id
                                                  )}
                                        </strong>

                                        <small>
                                            {new Date(
                                                comment.created_at
                                            ).toLocaleString()}
                                        </small>

                                    </div>

                                    {editingCommentId ===
                                    comment.id ? (
                                        <>
                                            <textarea
                                                rows="3"
                                                value={
                                                    editedContent
                                                }
                                                onChange={(
                                                    e
                                                ) =>
                                                    setEditedContent(
                                                        e
                                                            .target
                                                            .value
                                                    )
                                                }
                                            />

                                            <div className="comment-actions">

                                                <button
                                                    className="primary-btn"
                                                    disabled={
                                                        saving
                                                    }
                                                    onClick={() =>
                                                        saveComment(
                                                            comment.id
                                                        )
                                                    }
                                                >
                                                    Save
                                                </button>

                                                <button
                                                    className="secondary-btn"
                                                    onClick={
                                                        cancelEditing
                                                    }
                                                >
                                                    Cancel
                                                </button>

                                            </div>
                                        </>
                                    ) : (
                                        <>
                                            <p>
                                                {
                                                    comment.content
                                                }
                                            </p>

                                            {currentUser &&
                                                currentUser.id ===
                                                    comment.user_id && (
                                                    <div className="comment-actions">

                                                        <button
                                                            className="secondary-btn"
                                                            onClick={() =>
                                                                startEditing(
                                                                    comment
                                                                )
                                                            }
                                                        >
                                                            Edit
                                                        </button>

                                                        <button
                                                            className="danger-btn"
                                                            onClick={() =>
                                                                deleteComment(
                                                                    comment.id
                                                                )
                                                            }
                                                        >
                                                            Delete
                                                        </button>

                                                    </div>
                                                )}
                                        </>
                                    )}
                                </div>
                            )
                        )
                    )}
                </>
            )}
        </div>
    );
}

export default CommentSection;