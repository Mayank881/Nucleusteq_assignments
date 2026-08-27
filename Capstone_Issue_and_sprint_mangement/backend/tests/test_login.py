import uuid

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_login_success():
    """
    Test successful user login.
    """

    unique_email = f"{uuid.uuid4()}@gmail.com"

    payload = {
        "name": "Login User",
        "email": unique_email,
        "password": "Password@123",
        "role": "MEMBER",
    }

    # Register the user first
    client.post(
        "/users/register",
        json=payload,
    )

    # Login
    response = client.post(
        "/users/login",
        json={
            "email": unique_email,
            "password": "Password@123",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password():
    """
    Test login with wrong password.
    """

    unique_email = f"{uuid.uuid4()}@gmail.com"

    payload = {
        "name": "Wrong Password",
        "email": unique_email,
        "password": "Password@123",
        "role": "MEMBER",
    }

    client.post(
        "/users/register",
        json=payload,
    )

    # Login with wrong password
    response = client.post(
        "/users/login",
        json={
            "email": unique_email,
            "password": "WrongPassword",
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password."


def test_login_invalid_email():
    """
    Test login with an email that does not exist.
    """

    response = client.post(
        "/users/login",
        json={
            "email": "unknown@gmail.com",
            "password": "Password@123",
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password."