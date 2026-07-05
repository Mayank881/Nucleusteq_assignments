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

    return token


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


def test_create_issue_success():
    """
    Test successful issue creation.
    """

    token = create_admin()

    project_id = create_project(token)

    response = client.post(
        f"/projects/{project_id}/issues",
        json={
            "title": "Login Bug",
            "description": "Unable to login",
            "type": "Bug",
            "priority": "High",
            "assignee_id": None,
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

    token = create_admin()

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

    token = create_admin()

    project_id = create_project(token)

    response = client.post(
        f"/projects/{project_id}/issues",
        json={},
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 422