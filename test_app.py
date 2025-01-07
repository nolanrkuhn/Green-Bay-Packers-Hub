
import pytest
from app import create_app, db
from app.models import Player, User

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for tests

    with app.app_context():
        db.create_all()
        # Seed mock data for testing
        db.session.add(Player(name="Aaron Rodgers", position="Quarterback"))
        db.session.add(Player(name="Davante Adams", position="Wide Receiver"))
        db.session.commit()

    yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_player_search_by_name(client):
    response = client.get('/players?name=Aaron')
    assert response.status_code == 200
    assert b"Aaron Rodgers" in response.data

def test_player_search_by_position(client):
    response = client.get('/players?position=Wide Receiver')
    assert response.status_code == 200
    assert b"Davante Adams" in response.data

def test_user_signup_password_validation(client):
    response = client.post('/signup', data={
        'username': 'testuser',
        'password': '123',  # Too short
    })
    assert response.status_code == 200
    assert b"Password must be at least 6 characters long" in response.data
