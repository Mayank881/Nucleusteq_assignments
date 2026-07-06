import uuid

from fastapi.testclient import TestClient

from app.main import app
from app.database import users_collection

client = TestClient(app)


def create_admin():
    """
    Create and login an admin user.
    """

    unique_email = f"{uuid.uuid4()}@gmail.com"

    payload = {
        "name": "Admin User",
        "email": unique_email,
        "password": "Password@123",
    }

    client.post(
        "/users/register",
        json=payload,
    )

    users_collection.update_one(
        {"email": unique_email},
        {
            "$set": {
                "role": "admin",
            }
        },
    )

    login_response = client.post(
        "/users/login",
        data={
            "username": unique_email,
            "password": "Password@123",
        },
    )

    token = login_response.json()["access_token"]

    user = users_collection.find_one(
        {"email": unique_email}
    )

    return token, str(user["_id"])


def create_project(token):
    """
    Create a project and return its id.
    """

    response = client.post(
        "/projects",
        json={
            "name": f"Project-{uuid.uuid4()}",
            "description": "Issue Testing Project",
        },
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    return response.json()["id"]

def create_issue(
    token: str,
    user_id: str,
    project_id: str,
):
    """
    Create an issue and return its id.
    """

    response = client.post(
        f"/projects/{project_id}/issues",
        json={
            "title": "Workflow Issue",
            "description": "Testing workflow",
            "type": "Bug",
            "priority": "High",
            "assignee_id": user_id,
            "parent_id": None,
        },
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 201

    return response.json()["id"]


def test_create_issue_success():
    """
    Test successful issue creation.
    """

    token, user_id = create_admin()

    project_id = create_project(token)

    response = client.post(
        f"/projects/{project_id}/issues",
        json={
            "title": "Login Bug",
            "description": "Unable to login",
            "type": "Bug",
            "priority": "High",
            "assignee_id": user_id,
            "parent_id": None,
        },
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Login Bug"
    assert data["project_id"] == project_id
    assert data["status"] == "BACKLOG"


def test_create_issue_invalid_project():
    """
    Test issue creation with invalid project id.
    """

    token, _ = create_admin()

    response = client.post(
        "/projects/686868686868686868686868/issues",
        json={
            "title": "Bug",
            "description": "Testing",
            "type": "Bug",
            "priority": "High",
        },
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Project not found."


def test_create_issue_missing_fields():
    """
    Test issue creation with missing required fields.
    """

    token, _ = create_admin()

    project_id = create_project(token)

    response = client.post(
        f"/projects/{project_id}/issues",
        json={},
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 422

def test_valid_status_transition():
    """
    Test valid issue status transition.
    """

    token, user_id = create_admin()

    project_id = create_project(token)

    issue_id = create_issue(
        token,
        user_id,
        project_id,
    )

    response = client.patch(
        f"/projects/{project_id}/issues/{issue_id}/status",
        json={
            "status": "TODO",
        },
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "TODO"

def test_invalid_status_transition():
    """
    Test invalid status transition.
    """

    token, user_id = create_admin()

    project_id = create_project(token)

    issue_id = create_issue(
        token,
        user_id,
        project_id,
    )

    headers = {
        "Authorization": f"Bearer {token}",
    }

    client.patch(
        f"/projects/{project_id}/issues/{issue_id}/status",
        json={"status": "TODO"},
        headers=headers,
    )

    client.patch(
        f"/projects/{project_id}/issues/{issue_id}/status",
        json={"status": "IN_PROGRESS"},
        headers=headers,
    )

    client.patch(
        f"/projects/{project_id}/issues/{issue_id}/status",
        json={"status": "DONE"},
        headers=headers,
    )

    response = client.patch(
        f"/projects/{project_id}/issues/{issue_id}/status",
        json={"status": "TODO"},
        headers=headers,
    )

    assert response.status_code == 409

    assert response.json()["detail"] == (
        "Invalid status transition."
    )

def test_non_assignee_update():
    """
    Test that a non-assignee cannot update issue status.
    """

    token1, user1 = create_admin()

    project_id = create_project(token1)

    issue_id = create_issue(
        token1,
        user1,
        project_id,
    )

    token2, _ = create_admin()

    response = client.patch(
        f"/projects/{project_id}/issues/{issue_id}/status",
        json={
            "status": "TODO",
        },
        headers={
            "Authorization": f"Bearer {token2}",
        },
    )

    assert response.status_code == 403

    assert response.json()["detail"] == (
        "Only the assignee can update the issue status."
    )        