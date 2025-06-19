#app/routes/auth.py

from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token
from app.models import User
from app.extensions import db
from app.schemas import UserSchema

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
user_schema = UserSchema()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400
        
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email ya registrado"}), 409
        
    new_user = User(email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "Usuario creado"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if not user or user.password != data['password']:
        return jsonify({"error": "Credenciales inválidas"}), 401
    
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200
