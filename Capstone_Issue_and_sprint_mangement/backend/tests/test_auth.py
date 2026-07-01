import uuid

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_profile_without_token():
    """
    Test accessing protected endpoint without JWT token.
    """

    response = client.get("/users/me")

    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"


def test_get_profile_with_token():
    """
    Test accessing protected endpoint with a valid JWT token.
    """

    unique_email = f"{uuid.uuid4()}@gmail.com"

    payload = {
        "name": "Profile User",
        "email": unique_email,
        "password": "Password@123",
        "role": "MEMBER",
    }

    # Register a new user
    register_response = client.post(
        "/users/register",
        json=payload,
    )

    assert register_response.status_code == 201

    # Login to get JWT token
    login_response = client.post(
        "/users/login",
        json={
            "email": unique_email,
            "password": "Password@123",
        },
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    # Access protected endpoint
    response = client.get(
        "/users/me",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Profile User"
    assert data["email"] == unique_email
    assert data["role"] == "MEMBER"