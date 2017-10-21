from engine.data.movements import Movements
from engine.data.blocks.types import BlockTypes


class ChestBlocks(object):

    WEIGHTED_COMPOUND_CHEST = {
        'id': 'chest-compound',
        'block_type': BlockTypes.COMPOUND_WEIGHTED_EXERCISE,

        'title': 'Chest Compound',

        'possibilities': [
            {
                'movement': Movements.INCLINE_BENCH_PRESS
            },
            {
                'movement': Movements.FLAT_BENCH_PRESS
            },
            {
                'movement': Movements.INCLINE_BENCH_PRESS
            },
            {
                'movement': Movements.REVERSE_GRIP_FLAT_PRESS
            }
        ]
    }

    WEIGHTED_ISOLATION_CHEST = {
        'id': 'chest-isolation',
        'block_type': BlockTypes.ISOLATION_WEIGHTED_EXERCISE,

        'title': 'Chest Isolation',

        'possibilities': [
            {
                'movement': Movements.FLAT_CHEST_FLYES
            },
            {
                'movement': Movements.DECLINE_CHEST_FLYES
            },
            {
                'movement': Movements.INCLINE_CHEST_FLYES
            }
        ]

    }

    STRETCH_CHEST = {
        'id': 'chest-stretch',
        'block_type': BlockTypes.STRETCH,

        'title': 'Chest Stretch',

        'possibilities': [

        ]
    }


class ChestBlocksAPI(object):

    @staticmethod
    def get_all():
        return [
            ChestBlocks.WEIGHTED_COMPOUND_CHEST,
            ChestBlocks.WEIGHTED_ISOLATION_CHEST,
            ChestBlocks.STRETCH_CHEST
        ]