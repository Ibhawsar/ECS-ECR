import pytest
from fastapi.testclient import TestClient
from main import app

client =TestClient(app)

def test_valid_user():
    
    response = client.get("/octocat")
    assert response.status_code == 200
    assert "gists" in response.json()

def test_invalid_user():
    response = client.get("/thisUserDoesNotExist1234567")
    assert response.status_code == 404