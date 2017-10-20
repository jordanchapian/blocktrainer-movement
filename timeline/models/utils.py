def sanitizeResourcePatchRequest(patch):
    # Make sure that they are not attempting to change any ids
    patch.pop('id', None);


def sanitizeResourceCreationRequest(new_resource_data):
    # Make sure that they are not attempting to change any ids
    new_resource_data.pop('id', None);
