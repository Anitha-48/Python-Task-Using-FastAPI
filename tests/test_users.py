from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={
        "name": "Anitha",
        "email": "anitha@test.com"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Anitha"


def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200


def test_get_user_by_id():
    response = client.get("/users/1")
    assert response.status_code == 200


def test_update_user():
    response = client.put("/users/1", json={"name": "Updated"})
    assert response.status_code == 200


def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
