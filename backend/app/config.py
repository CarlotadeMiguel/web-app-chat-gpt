# app/config.py

import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_jwt_secret')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///chat.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
    # Puedes agregar más configuraciones aquí según crezca el proyecto

    # Opcional: configuración de expiración de tokens JWT
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # segundos (1 hora)

# Si quieres manejar distintos entornos:
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
