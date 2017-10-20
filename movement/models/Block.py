from models.connection import db

class Block(db.Document):
    title = db.StringField(max_length=60, unique=True)
