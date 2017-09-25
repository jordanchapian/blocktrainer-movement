from marshmallow_sqlalchemy import ModelSchema
from models.db import db


class BaseSchema(ModelSchema):
    class Meta:
        sqla_session = db
