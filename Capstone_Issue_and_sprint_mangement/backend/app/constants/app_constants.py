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