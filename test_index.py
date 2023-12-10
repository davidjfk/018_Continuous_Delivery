import pytest
from bs4 import BeautifulSoup
from main import app  

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_bug_check_title(client):
    response = client.get('/')
    assert response.status_code == 200
    # just checking in entire html response, if title is there, but
    # not checking if title is in correct place in html.
    assert b"The Symphony of Software: A Tribute to Digital Innovation" in response.data

def test_index_route_first_2_lines_of_html(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"In realms of code, where dreams take flight," in response.data
    assert b"Software reigns, a beacon bright." in response.data

def test_index_route_all_but_first_2_lines_of_html(client):
    response = client.get('/')
    assert response.status_code == 200

    soup = BeautifulSoup(response.data, 'html.parser')
    # first 2 poem lines are (deliberately, arbitrarily) not in list stanzas:
    stanzas = [
        "In every task, in every need,",
        "Software answers, swift and freed.",
        "It connects us, near and far,",
        "A tapestry of lives it shares.",
        "It bridges gaps, it breaks the chains,",
        "A symphony of digital reigns.",
        "It powers commerce, great and small,",
        "From humble shop to tower tall.",
        "It drives innovation, bold and free,",
        "A force of change, for you and me.",
        "It guides us through the endless maze,",
        "A faithful guide, in every phase.",
        "It simplifies, with logic's art,",
        "Unraveling complexities, one by one at heart.",
        "It enhances lives, both near and far,",
        "A blessing to us, beyond compare.",
        "So let us raise our voices high,",
        "And praise the software, reaching for the sky.",
        "For in its depths, we find our way,",
        "A beacon of hope, come what may.",
        "Software, software, you're the best,",
        "A boon to mankind, you're truly blessed.",
        "So let us sing your praises loud,",
        "As you enrich our lives, both new and proud."
    ]
    line_nr_in_http_response_poem = 3 # first 2 poem lines are not in stanzas above.

    for i, stanza in enumerate(stanzas, start=line_nr_in_http_response_poem):
        assert soup.find('p', class_=f'stanza{i}').text == stanza 


    
