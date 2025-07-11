#app/extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

# Inicialización de extensiones
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()
