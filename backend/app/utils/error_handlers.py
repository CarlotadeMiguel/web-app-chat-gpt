#app/utils/error_handlers.py
from flask import jsonify
from marshmallow import ValidationError

def register_error_handlers(app):
    """Registra manejadores de errores globales"""
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Solicitud incorrecta"}), 400
    
    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({"error": "No autorizado"}), 401
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Recurso no encontrado"}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Error interno del servidor"}), 500
    
    @app.errorhandler(ValidationError)
    def validation_error(error):
        return jsonify({"error": "Error de validación", "messages": error.messages}), 400
