# Este archivo permite que Python trate la carpeta 'routes' como un módulo
# No necesita contenido específico, pero puede incluir imports comunes

from .auth import auth_bp
from .chat import chat_bp

__all__ = ['auth_bp', 'chat_bp']
