from io import StringIO

from olympics import cli


def test_top_countries_without_value():
    string = StringIO()
    cli.top_countries(file=string)
    text = string.getvalue()
    assert 'Top' in text
    assert 'Country' in text
    assert '10' in text

def test_top_countries_with_top():
    string = StringIO()
    cli.top_countries(top = 5, file=string)
    text = string.getvalue()
    assert 'Top' in text
    assert 'Country' in text
    assert '5' in text

def test_top_collective_without_value():
    string = StringIO()
    cli.top_collective(file=string)
    text = string.getvalue()
    assert 'Top' in text
    assert 'collective' in text
    assert '10' in text

def test_top_collective_with_top():
    string = StringIO()
    cli.top_collective(top = 6, file=string)
    text = string.getvalue()
    assert 'Top' in text
    assert 'collective' in text
    assert '6' in text

def test_top_individual_without_value():
    string = StringIO()
    cli.top_individual(file=string)
    text = string.getvalue()
    assert 'Top' in text
    assert 'individual' in text
    assert '10' in text

def test_top_individual_with_top():
    string = StringIO()
    cli.top_individual(top = 7, file=string)
    text = string.getvalue()
    assert 'Top' in text
    assert 'individual' in text
    assert '7' in text

def test_search_countries_without_value():
    string = StringIO()
    cli.search_countries(file=string)
    text = string.getvalue()
    assert 'Country' in text
    assert 'None' in text

def test_search_countries_with_value():
    string = StringIO()
    cli.search_countries(name='Canada', file=string)
    text = string.getvalue()
    assert 'Country' in text
    assert 'Canada' in text