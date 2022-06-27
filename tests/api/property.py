import json
import pytest
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)


@pytest.mark.parametrize("filter", ["simple_request", "year", "limit", "city", "address"])
def test_read_list(filter):
    if filter == "year":
        response = client.get(f"/properties?year=2021")
    if filter == "limit":
        response = client.get(f"/properties?limit=1")
    if filter == "city":
        response = client.get(f"/properties?city=bogota")
    if filter == "address":
        response = client.get(f"/properties?address=calle 23 #45-67")
    else:
        response = client.get(f"/properties")
    data = response.json()
    print("response")
    print(data)
    assert response.status_code == 200
    assert len(data) > 0


@pytest.mark.parametrize("item", ["available", "unavailable"])
def test_read_single(item):
    property_id = 1
    if item == "unavailable":
        property_id = 10000

    response = client.get(f"/properties/{property_id}")
    assert response.status_code == 200
    if item == "available":
        assert response.json()
    if item == "unavailable":
        assert response.json() == "No item available"
