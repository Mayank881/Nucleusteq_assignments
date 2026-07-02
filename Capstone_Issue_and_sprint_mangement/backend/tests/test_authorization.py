import uuid

from fastapi.testclient import TestClient

from app.main import app
from app.database import users_collection

client = TestClient(app)


def test_admin_can_access_dashboard():
    """
    Test that an admin user can access the admin dashboard.
    """

    unique_email = f"{uuid.uuid4()}@gmail.com"

    payload = {
        "name": "Admin User",
        "email": unique_email,
        "password": "Password@123",
    }

    # Register user
    client.post(
        "/users/register",
        json=payload,
    )

    # Promote user to admin
    users_collection.update_one(
        {"email": unique_email},
        {
            "$set": {
                "role": "admin",
            }
        },
    )

    # Login
    login_response = client.post(
        "/users/login",
        json={
            "email": unique_email,
            "password": "Password@123",
        },
    )

    token = login_response.json()["access_token"]

    # Access admin endpoint
    response = client.get(
        "/admin/dashboard",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Welcome Admin"
    assert data["user"] == "Admin User"


def test_member_cannot_access_dashboard():
    """
    Test that a member cannot access the admin dashboard.
    """

    unique_email = f"{uuid.uuid4()}@gmail.com"

    payload = {
        "name": "Member User",
        "email": unique_email,
        "password": "Password@123",
    }

    # Register member
    client.post(
        "/users/register",
        json=payload,
    )

    # Login
    login_response = client.post(
        "/users/login",
        json={
            "email": unique_email,
            "password": "Password@123",
        },
    )

    token = login_response.json()["access_token"]

    # Try accessing admin endpoint
    response = client.get(
        "/admin/dashboard",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 403
    assert (
        response.json()["detail"]
        == "You are not authorized to perform this action."
    )


def test_admin_dashboard_without_token():
    """
    Test accessing admin endpoint without authentication.
    """

    response = client.get("/admin/dashboard")

    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"


def test_admin_dashboard_with_invalid_token():
    """
    Test accessing admin endpoint with an invalid JWT token.
    """

    response = client.get(
        "/admin/dashboard",
        headers={
            "Authorization": "Bearer invalid_token",
        },
    )

    assert response.status_code == 401
    assert (
        response.json()["detail"]
        == "Could not validate credentials."
    )