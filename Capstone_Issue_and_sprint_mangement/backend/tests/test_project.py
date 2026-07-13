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


def create_member():
    """
    Create and login a member user.
    """

    unique_email = f"{uuid.uuid4()}@gmail.com"

    payload = {
        "name": "Member User",
        "email": unique_email,
        "password": "Password@123",
    }

    client.post(
        "/users/register",
        json=payload,
    )

    user = users_collection.find_one(
        {"email": unique_email}
    )

    login_response = client.post(
        "/users/login",
        data={
            "username": unique_email,
            "password": "Password@123",
        },
    )

    token = login_response.json()["access_token"]

    return token, str(user["_id"])


def test_admin_can_create_project():
    """
    Test that an admin can create a project.
    """

    token = create_admin()

    response = client.post(
        "/projects",
        json={
            "name": f"Project-{uuid.uuid4()}",
            "description": "Testing Project",
        },
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert "id" in data
    assert "owner_id" in data
    assert len(data["members"]) == 1


def test_member_cannot_create_project():
    """
    Test that a member cannot create a project.
    """

    token, _ = create_member()

    response = client.post(
        "/projects",
        json={
            "name": f"Project-{uuid.uuid4()}",
            "description": "Testing",
        },
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 403


def test_add_member():
    """
    Test adding a member to a project.
    """

    admin_token = create_admin()

    response = client.post(
        "/projects",
        json={
            "name": f"Project-{uuid.uuid4()}",
            "description": "Testing",
        },
        headers={
            "Authorization": f"Bearer {admin_token}",
        },
    )

    project_id = response.json()["id"]

    _, member_id = create_member()

    response = client.post(
        f"/projects/{project_id}/members",
        json={
            "user_id": member_id,
        },
        headers={
            "Authorization": f"Bearer {admin_token}",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert member_id in data["members"]


def test_remove_member():
    """
    Test removing a member from a project.
    """

    admin_token = create_admin()

    response = client.post(
        "/projects",
        json={
            "name": f"Project-{uuid.uuid4()}",
            "description": "Testing",
        },
        headers={
            "Authorization": f"Bearer {admin_token}",
        },
    )

    project_id = response.json()["id"]

    _, member_id = create_member()

    client.post(
        f"/projects/{project_id}/members",
        json={
            "user_id": member_id,
        },
        headers={
            "Authorization": f"Bearer {admin_token}",
        },
    )

    response = client.delete(
        f"/projects/{project_id}/members/{member_id}",
        headers={
            "Authorization": f"Bearer {admin_token}",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert member_id not in data["members"]