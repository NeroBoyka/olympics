from olympics import db

# tests de get_countries
def test_countries_all():
    rows = db.get_countries()
    assert len(rows) > 100

def test_countries_with_id():
    row = db.get_countries(3)
    assert len(row) == 1

def test_countries_invalid_id():
    row = db.get_countries(999999)
    assert row == []
    row = db.get_countries(-1)
    assert row == []
    row = db.get_countries("zfzf")
    assert row == []

# tests de get_athletes
def test_athletes_all():
    rows = db.get_athletes()
    assert len(rows) > 100

def test_athletes_with_id():
    row = db.get_athletes(3)
    assert len(row) == 1

def test_athletes_invalid_id():
    row = db.get_athletes(999999)
    assert row == []
    row = db.get_athletes(-1)
    assert row == []
    row = db.get_athletes("zfzf")
    assert row == []

# tests de get_disciplines
def test_disciplines_all():
    rows = db.get_disciplines()
    assert len(rows) > 1

def test_disciplines_with_id():
    row = db.get_disciplines(3)
    assert len(row) == 1

def test_disciplines_invalid_id():
    row = db.get_disciplines(999999)
    assert row == []
    row = db.get_disciplines(-1)
    assert row == []
    row = db.get_disciplines("zfzf")
    assert row == []

# tests de get_teams
def test_teams_all():
    rows = db.get_teams()
    assert len(rows) > 100

def test_teams_with_id():
    row = db.get_teams(3)
    assert len(row) == 1

def test_teams_invalid_id():
    row = db.get_teams(999999)
    assert row == []
    row = db.get_teams(-1)
    assert row == []
    row = db.get_teams("zfzf")
    assert row == []

# tests de get_events
def test_events_all():
    rows = db.get_events()
    assert len(rows) > 100

def test_events_with_id():
    row = db.get_events(3)
    assert len(row) == 1

def test_events_invalid_id():
    row = db.get_events(999999)
    assert row == []
    row = db.get_events(-1)
    assert row == []
    row = db.get_events("zfzf")
    assert row == []

# tests de get_medals
def test_medals_all():
    rows = db.get_medals()
    assert len(rows) > 100

def test_medals_with_id():
    row = db.get_medals(3)
    assert len(row) == 1

def test_medals_invalid_id():
    row = db.get_medals(999999)
    assert row == []
    row = db.get_medals(-1)
    assert row == []
    row = db.get_medals("zfzf")
    assert row == []

# tests de get_discipline_athletes
def test_discipline_athletes():
    rows = db.get_discipline_athletes()
    assert len(rows) == 0

def test_discipline_athletes_with_id():
    rows = db.get_discipline_athletes(7)
    assert len(rows) > 1

def test_discipline_athletes_invalid_id():
    rows = db.get_discipline_athletes(999999)
    assert rows == []
    rows = db.get_discipline_athletes(-1)
    assert rows == []
    rows = db.get_discipline_athletes("zfzf")
    assert rows == []

# tests de get_top_countries
def test_top_countries():
    rows = db.get_top_countries()
    assert len(rows) == 10

def test_top_countries_with_top():
    rows = db.get_top_countries(6)
    assert len(rows) == 6

def test_top_countries_invalid_top():
    rows = db.get_top_countries(-1)
    assert len(rows) == 0
    rows = db.get_top_countries(0)
    assert len(rows) == 0
    rows = db.get_top_countries(999999)
    assert len(rows) == 10
    rows = db.get_top_countries("zfzf")
    assert len(rows) == 10

# tests de get_collective_medals
def test_collective_medals_all():
    rows = db.get_collective_medals()
    assert len(rows) > 1

def test_collective_medals_with_id():
    row = db.get_collective_medals(3)
    assert len(row) == 1

def test_collective_medals_invalid_id():
    row = db.get_collective_medals(999999)
    assert row == []
    row = db.get_collective_medals(0)
    assert row == []
    row = db.get_collective_medals(-1)
    assert row == []
    row = db.get_collective_medals("zfzf")
    assert row == []

# tests de get_top_collective
def test_top_collective():
    rows = db.get_top_collective()
    assert len(rows) == 10

def test_top_collective_with_top():
    rows = db.get_top_collective(4)
    assert len(rows) == 4

def test_top_collective_invalid_top():
    rows = db.get_top_collective(-1)
    assert len(rows) == 0
    rows = db.get_top_collective(0)
    assert len(rows) == 0
    rows = db.get_top_collective(999999)
    assert len(rows) == 10
    rows = db.get_top_collective("zfzf")
    assert len(rows) == 10

# test de get_individual_medals
def test_individual_medals_all():
    rows = db.get_individual_medals()
    assert len(rows) > 1

def test_individual_medals_with_id():
    rows = db.get_individual_medals(1)
    assert len(rows) == 1

def test_individual_medals_invalid_id():
    rows = db.get_individual_medals(999999)
    assert rows == []
    rows = db.get_individual_medals(0)
    assert rows == []
    rows = db.get_individual_medals(-1)
    assert rows == []
    rows = db.get_individual_medals("zfzf")
    assert rows == []

# test de get_top_individual
def test_top_individual():
    rows = db.get_top_individual()
    assert len(rows) == 10

def test_top_individual_with_top():
    rows = db.get_top_individual(4)
    assert len(rows) == 4

def test_top_individual_invalid_top():
    rows = db.get_top_individual(-1)
    assert len(rows) == 0
    rows = db.get_top_individual(0)
    assert len(rows) == 0
    rows = db.get_top_individual(999999)
    assert len(rows) == 10
    rows = db.get_top_individual("zfzf")
    assert len(rows) == 10

# test de search_countries
def test_search_countries_without_value():
    rows = db.search_countries()
    assert rows == []

def test_search_countries_empty_string():
    rows = db.search_countries('')
    assert len(rows) > 0

def test_search_countries_with_value():
    rows = db.search_countries('uni')
    assert len(rows) > 0

    country_names = []
    for x in rows: country_names.append(x['name'])
    assert 'United States' in country_names
    assert 'Unified Team' in country_names
    assert 'Soviet Union' in country_names

    rows = db.search_countries('france')
    assert len(rows) == 1
    assert rows[0]['name'] == 'France'

    rows = db.search_countries('zzfaf')
    assert rows == []

def test_search_countries_sql_injection():
    rows = db.search_countries('Uganda veut DROP TABLE COUNTRY;')
    assert rows == []