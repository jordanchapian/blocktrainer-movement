from marshmallow_sqlalchemy import ModelSchema
from schemas.base import BaseSchema
from models.movement import Movement


class MovementSchema(BaseSchema):

    class Meta(BaseSchema.Meta):
        model = Movement
