#app/routes/chat.py
from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Chat
from app.extensions import db
from app.services.gemini import get_gemini_response
from app.schemas import chat_send_schema

chat_bp = Blueprint('chat', __name__, url_prefix='/chat')

@chat_bp.route('/send', methods=['POST'])
@jwt_required()
def send_message():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    
    # Validar entrada
    errors = chat_send_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400
    
    # Guardar mensaje del usuario
    user_message = Chat(
        user_id=current_user_id,
        content=data['content'],
        role='user'
    )
    db.session.add(user_message)
    
    # Obtener respuesta de Gemini
    try:
        ai_response = get_gemini_response(data['content'])
    except Exception as e:
        return jsonify({"error": "Error al conectar con Gemini"}), 502
    
    # Guardar respuesta del asistente
    assistant_message = Chat(
        user_id=current_user_id,
        content=ai_response,
        role='assistant'
    )
    db.session.add(assistant_message)
    db.session.commit()
    
    return jsonify({"response": ai_response}), 200

@chat_bp.route('/history', methods=['GET'])
@jwt_required()
def get_history():
    current_user_id = get_jwt_identity()
    chats = Chat.query.filter_by(user_id=current_user_id).order_by(Chat.timestamp.asc()).all()
    return jsonify([{"role": c.role, "content": c.content, "timestamp": c.timestamp.isoformat()} for c in chats]), 200
