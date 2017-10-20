# from models.db import db
# from models.utils import sanitize_keys
# from flask import jsonify
# from http import HTTPStatus
# from sqlalchemy.exc import IntegrityError
# from conf.returnValues import ENTITY_NOT_FOUND
#
#
# class BaseResource:
#
#     def __init__(self, model=None, schema=None, disallowUpdatesTo=[]):
#         self.model = model
#         self.schema_single = schema()
#         self.schema_many = schema(many=True)
#         self.disallowUpdatesTo = disallowUpdatesTo
#
#     def search(self):
#         result, errors = self.schema_many.dump(self.model.query.all())
#
#         if errors:
#             return jsonify(errors), HTTPStatus.INTERNAL_SERVER_ERROR
#         else:
#             return jsonify(result), HTTPStatus.OK
#
#     def put(self, collection_id, put_body):
#         # Sanitize the patch request
#         sanitize_keys(put_body, self.disallowUpdatesTo)
#
#         # Try to fetch this entity
#         try:
#             existing_entity = self.model.query.get(collection_id)
#         except IntegrityError:
#             jsonify(ENTITY_NOT_FOUND), HTTPStatus.BAD_REQUEST
#
#         self.schema_single.load(put_body, instance=existing_entity, partial=True)
#         db.session.commit()
#
#         result, errors = self.schema_single.dump(existing_entity)
#
#         if errors:
#             return jsonify(errors), HTTPStatus.INTERNAL_SERVER_ERROR
#         else:
#             return jsonify(result), HTTPStatus.OK
#
#     def post(self, post_body):
#         # Sanitize fields
#         sanitize_keys(post_body, self.disallowUpdatesTo)
#
#         # Create the entity
#         new_entity = self.model()
#         self.schema_single.load(post_body, instance=new_entity, partial=True)
#
#         db.session.add(new_entity)
#         db.session.commit()
#
#         result, errors = self.schema_single.dump(new_entity)
#
#         if errors:
#             return jsonify(errors), HTTPStatus.INTERNAL_SERVER_ERROR
#         else:
#             return jsonify(result), HTTPStatus.CREATED
