from olympics import db

# tests de get_countries
def test_countries_all():
    rows = db.get_countries()
    assert len(rows) > 100

def test_countries_by_id():
    row = db.get_countries(3)
    assert len(row) == 1

# tests de get_athletes
def test_athletes_all():
    rows = db.get_athletes()
    assert len(rows) > 100

def test_athletes_by_id():
    row = db.get_athletes(3)
    assert len(row) == 1

# tests de get_disciplines
def test_disciplines_all():
    rows = db.get_disciplines()
    assert len(rows) > 1

def test_disciplines_by_id():
    row = db.get_disciplines(3)
    assert len(row) == 1

# tests de get_teams
def test_teams_all():
    rows = db.get_teams()
    assert len(rows) > 100

def test_teams_by_id():
    row = db.get_teams(3)
    assert len(row) == 1

# tests de get_events
def test_events_all():
    rows = db.get_events()
    assert len(rows) > 100

def test_events_by_id():
    row = db.get_events(3)
    assert len(row) == 1

# tests de get_medals
def test_medals_all():
    rows = db.get_medals()
    assert len(rows) > 100

def test_medals_by_id():
    row = db.get_medals(3)
    assert len(row) == 1

# tests de get_discipline_athletes
def test_discipline_athletes():
    rows = db.get_discipline_athletes()
    assert len(rows) == 0

def test_discipline_athletes_with_id():
    rows = db.get_discipline_athletes(7)
    assert len(rows) > 1

# tests de get_top_countries
def test_top_countries():
    rows = db.get_top_countries()
    assert len(rows) == 10

def test_top_countries_with_top():
    rows = db.get_top_countries(6)
    assert len(rows) == 6

# tests de get_collective_medals
def test_collective_medals_all():
    rows = db.get_collective_medals()
    assert len(rows) > 1

def test_collective_medals_by_id():
    row = db.get_collective_medals(3)
    assert len(row) == 1

# tests de get_top_collective
def test_top_collective():
    rows = db.get_top_collective()
    assert len(rows) == 10

def test_top_collective_with_top():
    rows = db.get_top_collective(4)
    assert len(rows) == 4

# test de get_individual_medals
def test_individual_medals_all():
    rows = db.get_individual_medals()
    assert len(rows) > 1

def test_individual_medals_by_id():
    rows = db.get_individual_medals(1)
    assert len(rows) == 1

# test de get_top_individual
def test_top_individual():
    rows = db.get_top_individual()
    assert len(rows) == 10

def test_top_individual_with_top():
    rows = db.get_top_individual(4)
    assert len(rows) == 4