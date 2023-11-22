import requests

# Tests for my APIs


def test_get_ships_by_country():
    response = requests.get("http://127.0.0.1:8001/ships/by-country/Cyprus")
    assert response.status_code == 200
    assert response.json()


def test_get_ships_by_distance():
    response = requests.get("http://127.0.0.1:8001/ships/by-distance?lat=39.1617&lon=21.4767&radius_km=5")
    assert response.status_code == 200
    assert response.json()
