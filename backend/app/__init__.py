from flask import Flask, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from .extensions import db, jwt, migrate

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    # Permitir todos los orígenes en todas las rutas:
    CORS(app, origins=['http://localhost:3000'])
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
    
    @app.route("/")
    def index():
        return render_template("index.html")

    from .utils.error_handlers import register_error_handlers
    register_error_handlers(app)

    return app
