from engine.data.blocks.chest import ChestBlocksAPI
from engine.data.blocks.back import BackBlocksAPI


class BlocksAPI(object):

    @staticmethod
    def get_all():
        return ChestBlocksAPI.get_all() + BackBlocksAPI.get_all()
