"""
Application-wide constants.
"""

# MongoDB Collection Names

USER_COLLECTION = "users"

PROJECT_COLLECTION = "projects"

ISSUE_COLLECTION = "issues"

SPRINT_COLLECTION = "sprints"

COMMENT_COLLECTION = "comments"


# API Prefixes

API_V1_PREFIX = "/api/v1"

USER_PREFIX = "/users"

PROJECT_PREFIX = "/projects"

ISSUE_PREFIX = "/issues"

SPRINT_PREFIX = "/sprints"

COMMENT_PREFIX = "/comments"

# Error Messages

INVALID_CREDENTIALS = "Invalid email or password."
INVALID_PROJECT_ID = "Invalid project ID."
INVALID_USER_ID = "Invalid user ID."

PROJECT_NOT_FOUND = "Project not found."
PROJECT_CREATED = "Project created successfully."

ISSUE_NOT_FOUND = "Issue not found."
INVALID_ISSUE_ID = "Invalid issue ID."

USER_NOT_FOUND = "User not found."

MEMBER_ALREADY_EXISTS = "User is already a project member."
MEMBER_NOT_FOUND = "User is not a project member."

PROJECT_NAME_EXISTS = "Project with this name already exists."

USER_ALREADY_EXISTS = "Email already registered."

PROJECT_OWNER_CANNOT_BE_REMOVED = (
    "Project owner cannot be removed."
)

UNAUTHORIZED_ACTION = (
    "You are not authorized to perform this action."
)

ISSUE_NOT_ASSIGNEE = (
    "Only the assignee can update the issue status."
)

INVALID_STATUS_TRANSITION = (
    "Invalid status transition."
)
# sprint module constants

SPRINT_STATUS_PLANNED = "PLANNED"
SPRINT_STATUS_ACTIVE = "ACTIVE"
SPRINT_STATUS_COMPLETED = "COMPLETED"

INVALID_SPRINT_DATES = (
    "Sprint start date must be before end date."
)

SPRINT_NOT_FOUND = "Sprint not found."
INVALID_SPRINT_ID = "Invalid sprint ID."

ISSUE_ALREADY_IN_SPRINT = (
    "Issue is already added to this sprint."
)

DONE_ISSUE_NOT_ALLOWED = (
    "Completed issues cannot be added to a sprint."
)

ISSUE_NOT_IN_SPRINT = (
    "Issue is not part of this sprint."
)

SPRINT_ALREADY_ACTIVE = (
    "Sprint is already active."
)

SPRINT_ALREADY_COMPLETED = (
    "Sprint is already completed."
)

SPRINT_NOT_ACTIVE = (
    "Sprint must be active before it can be completed."
)

ISSUE_NOT_FOUND = "Issue not found."


ISSUE_PROJECT_MISMATCH = (
    "Issue and sprint belong to different projects."
)

DONE_ISSUE_NOT_ALLOWED = (
    "Completed issues cannot be added to a sprint."
)

ASSIGNEE_NOT_IN_PROJECT = (
    "Selected assignee is not a member of this project."
)

PARENT_ISSUE_NOT_FOUND = (
    "Parent issue not found."
)

PARENT_ISSUE_PROJECT_MISMATCH = (
    "Parent issue must belong to the same project."
)
# Comment Module

COMMENT_NOT_FOUND = "Comment not found."

ONLY_COMMENT_OWNER = (
    "Only the comment owner can perform this action."
)

COMMENT_CREATED = "Comment created successfully."

COMMENT_UPDATED = "Comment updated successfully."

COMMENT_DELETED = "Comment deleted successfully."

ADMIN_REGISTERED_NOT_ALLOWED = (
    "Admin registration is not allowed through public API."
)
ACTIVE_SPRINT_DELETE_NOT_ALLOWED = "Active sprint cannot be deleted."