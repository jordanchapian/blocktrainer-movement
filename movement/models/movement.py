from models.db import db


class Movement(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Movement %r>' % self.title

    def __iter__(self):
        return self.__dict__.iteritems()
