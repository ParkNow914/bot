from fastapi.testclient import TestClient
from main import app

def test_root():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert "Super-Bot API Gateway" in response.json()["message"] or "Super-Bot API Gateway" in response.json().get("version", "") 