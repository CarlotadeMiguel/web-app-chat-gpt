# tests/test_auth.py
import pytest
from app import create_app
from app.extensions import db
from app.models import User

@pytest.fixture
def app():
    """Crea una instancia de la aplicación para testing"""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    """Cliente de prueba para hacer requests"""
    return app.test_client()

def test_register_success(client):
    """Test de registro exitoso"""
    response = client.post('/auth/register', 
                          json={'email': 'test@example.com', 'password': 'password123'})
    assert response.status_code == 201
    assert b'Usuario creado' in response.data

def test_login_success(client):
    """Test de login exitoso"""
    # Primero registrar un usuario
    client.post('/auth/register', 
                json={'email': 'test@example.com', 'password': 'password123'})
    
    # Luego hacer login
    response = client.post('/auth/login', 
                          json={'email': 'test@example.com', 'password': 'password123'})
    assert response.status_code == 200
    assert b'access_token' in response.data
