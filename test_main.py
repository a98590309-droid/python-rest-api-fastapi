import pytest
from fastapi.testclient import TestClient
from main import app, db

client = TestClient(app)

@pytest.fixture(autouse=True)
def run_around_tests():
    db.clear()
    yield
    db.clear()

def test_create_item_success():
    payload = {"name": "Laptop", "price": 999.99, "in_stock": True}
    res = client.post("/items", json=payload)
    assert res.status_code == 201
    assert res.json()["name"] == "Laptop"
    assert res.json()["id"] == 1

def test_create_item_validation_failure():
    # Negative price and missing name to test malformed payload handling
    payload = {"name": "A", "price": -5.0}
    res = client.post("/items", json=payload)
    assert res.status_code == 422  # Unprocessable Entity

def test_get_item_not_found():
    res = client.get("/items/999")
    assert res.status_code == 404
    assert res.json()["detail"] == "Item not found"

def test_delete_item():
    # Setup
    create_res = client.post("/items", json={"name": "Book", "price": 12.50})
    item_id = create_res.json()["id"]

    # Delete
    del_res = client.delete(f"/items/{item_id}")
    assert del_res.status_code == 204

    # Verify deleted
    get_res = client.get(f"/items/{item_id}")
    assert get_res.status_code == 404
