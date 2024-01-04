import pytest
from bs4 import BeautifulSoup
from main import app  

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_mindset_check_title(client):
    response = client.get('/teamwork')
    assert response.status_code == 200
    # just checking in entire html response, if title is there, but
    # not checking if title is in correct place in html.
    assert b"Software Development, A Tale of Teamwork" in response.data

def test_mindset_check_all_html(client):
    response = client.get('/teamwork')
    assert response.status_code == 200

    soup = BeautifulSoup(response.data, 'html.parser')
    stanzas = [
        "In a realm of code and digital dreams,",
        "Where logic reigns and algorithms gleam,",
        "A software project takes its flight,",
        "A journey fraught with challenges and strife.",

        "A team of developers, skilled and keen,",
        "Converge their minds, their passion keen,",
        "To craft a masterpiece, a digital art,",
        "A software marvel, destined to impart.",

        "With agile steps and focused minds,",
        "They tackle bugs and conquer binds,",
        "Through requirements, tests, and endless days,",
        "Their project grows, in vibrant ways.",

        "User stories flow, like verses clear,",
        "Functional specs, dispelling all fear,",
        "Designs unfurl, like tapestries grand,",
        "A symphony of code, in their creative hand.",

        "Yet challenges arise, like storms at sea,",
        "Bugs persist, delaying speed,",
        "Deadlines loom, their shadows cast,",
        "Yet the developers, their spirits unfazed.",

        "Through collaboration, they find their way,",
        "Each member, adding their unique display,",
        "Code intertwines, like threads so fine,",
        "A web of logic, where ideas intertwine.",

        "So onward they march, with hearts ablaze,",
        "Their project's vision, in their dazzled gaze,",
        "Software development, a journey grand,",
        "A tale of teamwork, in this digital land."
    ]

    line_nr_in_http_response_poem = 1 
    for i, stanza in enumerate(stanzas, start=line_nr_in_http_response_poem):
        assert soup.find('p', class_=f'stanza{i}').text == stanza 


    
