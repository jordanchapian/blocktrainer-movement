import http

from flask import jsonify
from sqlalchemy.exc import IntegrityError

from conf.returnValues import ENTITY_NOT_FOUND
from schemas.movement import MovementSchema
from models.movement import Movement
from models.db import db
from models.utils import sanitizeResourcePatchRequest, sanitizeResourceCreationRequest

movement_schema = MovementSchema()
movements_schema = MovementSchema(many=True)


def put(movement_id, movement):

    # Sanitize the patch request
    sanitizeResourcePatchRequest(movement)

    # Try to fetch this entity
    try:
        existing_movement = Movement.query.get(movement_id)
    except IntegrityError:
        jsonify(ENTITY_NOT_FOUND), http.HTTPStatus.BAD_REQUEST

    movement_schema.load(movement, instance=existing_movement, partial=True)
    db.session.commit()

    result, errors = movement_schema.dump(existing_movement)

    if errors:
        return jsonify(errors), http.HTTPStatus.INTERNAL_SERVER_ERROR
    else:
        return jsonify(result), http.HTTPStatus.OK


def post(movement):

    # Sanitize
    sanitizeResourceCreationRequest(movement)

    # If we are trying to specify an id, error out.
    if 'id' in movement:
        return http.HTTPStatus.BAD_REQUEST

    # Create the entity
    new_movement = Movement()
    movement_schema.load(movement, instance=new_movement, partial=True)

    db.session.add(new_movement)
    db.session.commit()

    result, errors = movement_schema.dump(new_movement)

    if errors:
        return jsonify(errors), http.HTTPStatus.INTERNAL_SERVER_ERROR
    else:
        return jsonify(result), http.HTTPStatus.CREATED


def search():

    result, errors = movements_schema.dump(Movement.query.all())

    if errors:
        return jsonify(errors), http.HTTPStatus.INTERNAL_SERVER_ERROR
    else:
        return jsonify(result), http.HTTPStatus.OK
