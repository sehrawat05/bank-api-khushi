from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_banks():
    response = client.get("/banks")
    assert response.status_code == 200
    assert "banks" in response.json()



def test_invalid_bank():
    response = client.get("/banks/UNKNOWN_BANK/branches")
    assert response.status_code == 404