from marshmallow import Schema, fields

class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    user_id = fields.Int(dump_only=True)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class TokenSchema(Schema):
    access_token = fields.Str(dump_only=True)
    message = fields.Str(dump_only=True)