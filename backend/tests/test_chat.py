# tests/test_chat.py
import pytest
from app import create_app
from app.extensions import db

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_token(client):
    """Obtiene un token de autenticación para las pruebas"""
    client.post('/auth/register', 
                json={'email': 'test@example.com', 'password': 'password123'})
    
    response = client.post('/auth/login', 
                          json={'email': 'test@example.com', 'password': 'password123'})
    return response.get_json()['access_token']

def test_send_message_requires_auth(client):
    """Test que requiere autenticación para enviar mensajes"""
    response = client.post('/chat/send', 
                          json={'content': 'Hola'})
    assert response.status_code == 401

def test_chat_history_requires_auth(client):
    """Test que requiere autenticación para ver historial"""
    response = client.get('/chat/history')
    assert response.status_code == 401
