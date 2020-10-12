from app import create_app


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Isuru Gunasekara" in response.data


def test_page_not_found(client):
    response = client.get("/blablabladkfosdfag")
    assert response.status_code == 404
    assert b"Isuru Gunasekara" in response.data
