from engine.data.programs.ProgramBase import ProgramBase, program_to_dict
from engine.data.programs.configurationOptions import ConfigurationOption, ConfigurationKeys, ConfigurationTypes, ConfigurationSelection
from engine.data.blocks.chest import ChestBlocks
from engine.data.blocks.back import BackBlocks
from engine.data.equipment import Equipment
from engine.data.blocks.instance import BlockInstance

from typing import List, Dict

chestCoreBlockInstances = [
    BlockInstance(ChestBlocks.WEIGHTED_COMPOUND_CHEST),
    ChestBlocks.WEIGHTED_ISOLATION_CHEST
]

backCoreBlockInstances = [
    BackBlocks.WEIGHTED_COMPOUND_BACK,
    BackBlocks.WEIGHTED_ISOLATION_BACK
]


class FiveByFive(ProgramBase):

    def __init__(self, variations):

        # Unique key for the program
        self.__key = "five-by-five"

        # Set the configuration options for this
        self.__configurationOptions = [
            ConfigurationOption(ConfigurationKeys.NUMBER_OF_DAYS, ConfigurationTypes.DISCRETE_SELECTION, {
                'options': [3, 4, 5]
            })
        ]

        # Create a cached version of this to return as a dict
        self.to_dict_cached = program_to_dict(self)

    @property
    def configuration_options(self) -> List:
        return self.__configurationOptions

    @property
    def key(self) -> str:
        return self.__key

    def to_dict(self) -> Dict:
        return self.to_dict_cached

    def generate_split(self, configuration_selections: List[ConfigurationSelection]):
        # TODO: - We can use timeline data here to optimize how difficult these block should be (keep it in a callable service)
        return self._generate_3_day_split()

    @staticmethod
    def _generate_3_day_split():

        # Generate the first day
        dayOne = [

            BlockInstance(ChestBlocks.WEIGHTED_COMPOUND_CHEST)
            .set_equipment_restriction([Equipment.BARBELL, Equipment.DUMBBELL])
            .set_n_occurrences(3)
            .set_static_reps_and_sets(reps=5, sets=5),

            BlockInstance(ChestBlocks.WEIGHTED_ISOLATION_CHEST)
            .set_n_occurrences(2)
            .set_static_reps_and_sets(reps=10, sets=2),

            BlockInstance(BackBlocks.WEIGHTED_COMPOUND_BACK)
            .set_equipment_restriction([Equipment.BARBELL, Equipment.DUMBBELL])
            .set_n_occurrences(3)
            .set_static_reps_and_sets(reps=5, sets=5),

            BlockInstance(BackBlocks.WEIGHTED_ISOLATION_BACK)
            .set_n_occurrences(3)
            .set_static_reps_and_sets(reps=10, sets=2)

        ]
