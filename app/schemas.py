# app/schemas.py

from marshmallow import Schema, fields, validate, ValidationError

class UserRegisterSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=8))

class UserLoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)

class ChatSendSchema(Schema):
    content = fields.Str(required=True, validate=validate.Length(min=1))

# Opcional: para serializar mensajes del historial
class ChatMessageSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(dump_only=True)
    role = fields.Str()
    content = fields.Str()
    timestamp = fields.DateTime()

# Puedes instanciar los esquemas donde los necesites:
user_register_schema = UserRegisterSchema()
user_login_schema = UserLoginSchema()
chat_send_schema = ChatSendSchema()
chat_message_schema = ChatMessageSchema()
