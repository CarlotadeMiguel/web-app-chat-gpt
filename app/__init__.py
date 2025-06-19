from flask import Flask
from dotenv import load_dotenv
from .extensions import db, jwt, migrate

def create_app():
    app = Flask(__name__)
    load_dotenv()
    
    app.config.from_object('app.config.Config')
    
    # Inicializar extensiones
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    
    # Registrar blueprints
    from .routes.auth import auth_bp
    from .routes.chat import chat_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(chat_bp)
    
    from .utils.error_handlers import register_error_handlers
    register_error_handlers(app)

    return app
