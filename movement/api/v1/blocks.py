from engine.data.blocks import BlocksAPI


def search():
    return BlocksAPI.get_all()