from fastapi.testclient import TestClient

from olympics import api


client = TestClient(api.app)


def test_countries():
    response = client.get('/countries/')
    assert response.status_code == 200
    assert len(response.json()) > 100

def test_countries_id():
    response = client.get('/countries/?id=5')
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_athletes():
    response = client.get('/athletes/')
    assert response.status_code == 200
    assert len(response.json()) > 100

def test_athletes_id():
    response = client.get('/athletes/?id=5')
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_disciplines():
    response = client.get('/disciplines/')
    assert response.status_code == 200
    assert len(response.json()) > 1

def test_disciplines_id():
    response = client.get('/disciplines/?id=5')
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_teams():
    response = client.get('/teams/')
    assert response.status_code == 200
    assert len(response.json()) > 1

def test_teams_id():
    response = client.get('/teams/?id=5')
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_events():
    response = client.get('/events/')
    assert response.status_code == 200
    assert len(response.json()) > 1

def test_events_id():
    response = client.get('/events/?id=5')
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_medals():
    response = client.get('/medals/')
    assert response.status_code == 200
    assert len(response.json()) > 1

def test_medals_id():
    response = client.get('/medals/?id=5')
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_discipline_athletes():
    response = client.get('/discipline-athletes/5')
    assert response.status_code == 200
    assert len(response.json()) > 1

def test_top_countries():
    response = client.get('/top-countries/')
    assert response.status_code == 200
    assert len(response.json()) == 10

def test_top_countries_id():
    response = client.get('/top-countries/?top=50')
    assert response.status_code == 200
    assert len(response.json()) == 50

def test_collective_medals():
    response = client.get('/collective-medals/')
    assert response.status_code == 200
    assert len(response.json()) > 1

def test_collective_medals_id():
    response = client.get('/collective-medals/?team_id=198')
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_top_collective():
    response = client.get('/top-collective/')
    assert response.status_code == 200
    assert len(response.json()) > 1

def test_top_collective_id():
    response = client.get('/top-collective/?top=8')
    assert response.status_code == 200
    assert len(response.json()) == 8

def test_individual_medals():
    response = client.get('/individual-medals/')
    assert response.status_code == 200
    assert len(response.json()) > 1

def test_individual_medals_id():
    response = client.get('/individual-medals/?athlete_id=2')
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_top_individual():
    response = client.get('/top-individual/')
    assert response.status_code == 200
    assert len(response.json()) > 1

def test_top_individual_id():
    response = client.get('/top-individual/?top=4')
    assert response.status_code == 200
    assert len(response.json()) == 4
