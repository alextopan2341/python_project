import pytest
from fastapi.testclient import TestClient

from app.db import init_db
from app.main import app
from app.config import settings

client = TestClient(app)
API_KEY = settings.API_KEY

@pytest.fixture(scope="session", autouse=True)
def initialize_sqlite():
    init_db()

def test_pow():
    r = client.post("/pow", json={"x":2,"y":3}, headers={"x-api-key": API_KEY})
    assert r.status_code == 200
    assert r.json()["result"] == 8

def test_fib():
    r = client.post("/fibonacci/7", headers={"x-api-key": API_KEY})
    assert r.status_code == 200
    assert r.json()["result"] == 13

def test_fact():
    r = client.post("/factorial/5", headers={"x-api-key": API_KEY})
    assert r.status_code == 200
    assert r.json()["result"] == 120
