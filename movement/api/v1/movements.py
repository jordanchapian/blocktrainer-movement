# from schemas.movement import MovementSchema
#
# from api.BaseResource import BaseResource
# from models.movement import Movement
#
# disallowedUpdateKeys = [
#     "id"
# ]
#
# base_resource = BaseResource(schema=MovementSchema, model=Movement, disallowUpdatesTo=disallowedUpdateKeys)
#

def post(movement):
    return None
    # return base_resource.post(movement)


def search():
    return None
    # return base_resource.search()


def put(movement_id, movement):
    return None
    # return base_resource.put(movement_id, movement)