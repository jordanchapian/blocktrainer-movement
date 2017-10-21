from engine.data.movements import Movements
from engine.data.blocks.types import BlockTypes


class BackBlocks(object):

    WEIGHTED_COMPOUND_BACK = {
        'id': 'back-compound',
        'block_type': BlockTypes.COMPOUND_WEIGHTED_EXERCISE,

        'title': 'Back Compound',

        'possibilities': [
            {
                'movement': Movements.ONE_HAND_DUMBBELL_ROW
            },
            {
                'movement': Movements.BARBELL_ROW
            },
            {
                'movement': Movements.T_BAR_ROW
            }
        ]
    }

    WEIGHTED_ISOLATION_BACK = {
        'id': 'back-isolation',
        'block_type': BlockTypes.ISOLATION_WEIGHTED_EXERCISE,

        'title': 'Back Isolation',

        'possibilities': [

        ]

    }

    STRETCH_BACK = {
        'id': 'back-stretch',
        'block_type': BlockTypes.STRETCH,

        'title': 'Back Stretch',

        'possibilities': [

        ]
    }


class BackBlocksAPI(object):

    @staticmethod
    def get_all():
        return [
            BackBlocks.WEIGHTED_COMPOUND_BACK,
            BackBlocks.WEIGHTED_ISOLATION_BACK,
            BackBlocks.STRETCH_BACK
        ]