import pytest
from bs4 import BeautifulSoup
from main import app  

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_mindset_check_title(client):
    response = client.get('/mindset')
    assert response.status_code == 200
    # just checking in entire html response, if title is there, but
    # not checking if title is in correct place in html.
    assert b"The Dance of Code: A Developer's Journey" in response.data

def test_mindset_check_all_html(client):
    response = client.get('/mindset')
    assert response.status_code == 200

    soup = BeautifulSoup(response.data, 'html.parser')
    stanzas = [
        "In realms of code, where pixels dance,",
        "A developer's focus, a steadfast stance.",
        "Through lines and loops, they weave and tread,",
        "With passion's flame, their spirits fed.",

        "Like clouds that drift, their thoughts take flight,",
        "Unveiling solutions, shining bright.",
        "In every challenge, an opportunity's call,",
        "To push their limits, stand tall.",

        "With perseverance, they break the mold,",
        "Their fingers flying, a story told.",
        "Through sleepless nights, their minds ignite,",
        "The code unraveling, like moonlight.",

        "In every bug, a puzzle to solve,",
        "A triumph's echo, a story to extol.",
        "With dedication, they piece it together,",
        "A symphony of code, a masterpiece endeavor.",

        "Inspiration sparks, a guiding light,",
        "Revealing new paths, a future so bright.",
        "With every line, a dream takes flight,",
        "A software creation, a beacon of light.",

        "Oh, software developer, with passion and grace,",
        "You weave the digital tapestry, with unwavering embrace.",
        "Your perseverance, dedication, and inspiration's call,",
        "Enriching lives, one line at a time, through the software's fall."
    ]

    line_nr_in_http_response_poem = 1 
    for i, stanza in enumerate(stanzas, start=line_nr_in_http_response_poem):
        assert soup.find('p', class_=f'stanza{i}').text == stanza 


    
