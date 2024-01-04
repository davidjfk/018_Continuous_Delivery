import pytest
from bs4 import BeautifulSoup
from main import app  

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_bug_check_title(client):
    response = client.get('/bugs')
    assert response.status_code == 200
    assert b"The Developer's Struggle: A Tale of Code and Resilience" in response.data

def test_bug_check_all_html(client):
    response = client.get('/bugs')
    assert response.status_code == 200

    soup = BeautifulSoup(response.data, 'html.parser')
    stanzas = [
        "In the realm of code, where darkness reigns,",
        "A haunting presence, a software bane.",
        "A bug, a glitch, a wicked foe,",
        "It lurks and waits, its presence grows.",

        "\"Nevermore!\" it whispers, dark and deep,",
        "A chilling echo, a sleep to keep.",
        "The developer struggles, lost in the fray,",
        "The bug's relentless grip, day after day.",

        "Debugging tools, they seem so weak,",
        "Against the bug's power, they can't speak.",
        "The developer's sanity slips away,",
        "As the bug's relentless torments play.",

        "\"Nevermore!\" it echoes, from afar,",
        "A haunting reminder, that's always there.",
        "The developer's spirit, crushed and worn,",
        "The bug's relentless grip, a battle sworn.",

        "Oh, woeful developer, lost in despair,",
        "The bug's relentless grip, a never-ending snare.",
        "The only hope, a solution's gleam,",
        "To banish the bug, and bring sweet dream.",

        "So let us pour our hearts and souls,",
        "To vanquish the bug, and make it whole.",
        "With code and logic, we shall fight,",
        "And drive the bug away, into the night.",

        "For in the realm of code, the battle rages,",
        "Between the developer and the software plagues.",
        "May the developer prevail, with skill and grace,",
        "And banish the bug, in its dark place."  
    ]

    line_nr_in_http_response_poem = 1 
    for i, stanza in enumerate(stanzas, start=line_nr_in_http_response_poem):
        assert soup.find('p', class_=f'stanza{i}').text == stanza 


   
