#app/utils/validators.py
from marshmallow import fields, validate, ValidationError
import re

def validate_strong_password(password):
    """Valida que la contraseña sea fuerte"""
    if len(password) < 8:
        raise ValidationError("La contraseña debe tener al menos 8 caracteres")
    
    if not re.search(r"[A-Z]", password):
        raise ValidationError("La contraseña debe contener al menos una mayúscula")
    
    if not re.search(r"[a-z]", password):
        raise ValidationError("La contraseña debe contener al menos una minúscula")
    
    if not re.search(r"\d", password):
        raise ValidationError("La contraseña debe contener al menos un número")
    
    return password

def validate_email_domain(email):
    """Valida dominios de email permitidos"""
    allowed_domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']
    domain = email.split('@')[1] if '@' in email else ''
    
    if domain not in allowed_domains:
        raise ValidationError(f"Dominio {domain} no permitido")
    
    return email

# Campo personalizado para contraseñas fuertes
class StrongPasswordField(fields.String):
    def _deserialize(self, value, attr, data, **kwargs):
        value = super()._deserialize(value, attr, data, **kwargs)
        return validate_strong_password(value)
