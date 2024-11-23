import pytest
from app.calculator import app

@pytest.fixture
def client():
    # Configuration pour tester l'application Flask
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_addition(client):
    response = client.post("/", data={"num1": "5", "num2": "3", "operation": "+"})
    assert response.status_code == 200
    assert b"8.0" in response.data  # Vérifie si le résultat est affiché sur la page

def test_subtraction(client):
    response = client.post("/", data={"num1": "10", "num2": "7", "operation": "-"})
    assert response.status_code == 200
    assert b"3.0" in response.data

def test_multiplication(client):
    response = client.post("/", data={"num1": "4", "num2": "5", "operation": "*"})
    assert response.status_code == 200
    assert b"20.0" in response.data

def test_division(client):
    response = client.post("/", data={"num1": "10", "num2": "2", "operation": "/"})
    assert response.status_code == 200
    assert b"5.0" in response.data

def test_division_by_zero(client):
    response = client.post("/", data={"num1": "10", "num2": "0", "operation": "/"})
    assert response.status_code == 200
    assert b"Division par z&#233;ro non permise" in response.data  # Vérifie le message d'erreur

def test_invalid_operation(client):
    response = client.post("/", data={"num1": "10", "num2": "2", "operation": "%"})
    assert response.status_code == 200
    assert b"Op&#233;ration non valide." in response.data

def test_invalid_input(client):
    response = client.post("/", data={"num1": "abc", "num2": "2", "operation": "+"})
    assert response.status_code == 200
    assert b"Veuillez entrer des nombres valides." in response.data
