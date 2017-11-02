from engine.data.blocks.chest import ChestBlocks
from engine.data.blocks.back import BackBlocks

class Programs(object):
    FIVE_BY_FIVE = {

        'split_variations':
        [
            # 3 day split
            {
                [
                    # Session 1
                    {
                        'components': {
                            'blocks': [
                                ChestBlocks.WEIGHTED_COMPOUND_CHEST,
                                ChestBlocks.WEIGHTED_ISOLATION_CHEST,
                                BackBlocks.WEIGHTED_COMPOUND_BACK,
                                BackBlocks.WEIGHTED_ISOLATION_BACK
                            ],
                            'movements': [

                            ]
                        }
                    },
                    # Session 2
                    {
                        'components': {
                            'blocks': [

                            ],
                            'movements': [

                            ]
                        }
                    },
                    # Session 3
                    {
                        'components': {
                            'blocks': [

                            ],
                            'movements': [

                            ]
                        }
                    }
                ]
            }
        ]
    }

class ProgramsAPI(object):

    @staticmethod
    def get_all():
        return [
            Programs.FIVE_BY_FIVE
        ]