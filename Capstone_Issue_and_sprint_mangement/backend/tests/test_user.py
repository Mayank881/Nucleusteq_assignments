from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

import uuid


def test_register_user_success():
    """
    Test successful user registration.
    """

    unique_email = f"{uuid.uuid4()}@gmail.com"

    response = client.post(
        "/users/register",
        json={
            "name": "Test User",
            "email": unique_email,
            "password": "Password@123",
            "role": "MEMBER",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Test User"
    assert data["email"] == unique_email
    assert data["role"] == "MEMBER"
    assert "id" in data
def test_register_duplicate_email():
    """
    Test registration with an already registered email.
    """

    payload = {
        "name": "Duplicate User",
        "email": "duplicate@gmail.com",
        "password": "Password@123",
        "role": "MEMBER",
    }

    # First registration
    client.post(
        "/users/register",
        json=payload,
    )

    # Duplicate registration
    response = client.post(
        "/users/register",
        json=payload,
    )

    assert response.status_code == 409
    assert response.json()["detail"] == "Email already registered."

def test_register_invalid_data():
    """
    Test registration with invalid request data.
    """

    response = client.post(
        "/users/register",
        json={
            "name": "",
            "email": "invalid-email",
            "password": "123",
            "role": "MEMBER",
        },
    )

    assert response.status_code == 422