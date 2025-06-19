# tests/conftest.py
import pytest
import os
import tempfile
from app import create_app
from app.extensions import db

@pytest.fixture(scope='session')
def app():
    """Configuración de la aplicación para todas las pruebas"""
    db_fd, db_path = tempfile.mkstemp()
    
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': f'sqlite:///{db_path}',
        'SECRET_KEY': 'test-key',
        'JWT_SECRET_KEY': 'test-jwt-key'
    })
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()
    
    os.close(db_fd)
    os.unlink(db_path)
