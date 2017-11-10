from engine.data.programs.ProgramBase import ProgramBase, program_to_dict
from engine.data.programs.configuration import ConfigurationOption, ConfigurationIds, ConfigurationTypes, \
    ConfigurationSelection, ConfigurationOptionGroup, ConfigurationSelectionGroup
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

        # Unique id for the program
        self.__id = "five-by-five"

        # Set the configuration options for this
        self.__configurationOptions = ConfigurationOptionGroup([

            ConfigurationOption(ConfigurationIds.NUMBER_OF_DAYS, ConfigurationTypes.DISCRETE_SELECTION, {
                'options': [3, 4, 5]
            }, required=True),

            ConfigurationOption(ConfigurationIds.INTENSITY, ConfigurationTypes.DISCRETE_SELECTION, {
                'options': [1, 2, 3]
            }, required=True)

        ])

        # Create a cached version of this to return as a dict
        self.to_dict_cached = program_to_dict(self)

    @property
    def configuration_options(self) -> ConfigurationOptionGroup:
        return self.__configurationOptions

    @property
    def id(self) -> str:
        return self.__id

    def to_dict(self) -> Dict:
        return self.to_dict_cached

    def generate_split(self, configuration_selections: ConfigurationSelectionGroup):
        # TODO: - We can use timeline data here to optimize how difficult these block should be (keep it in a callable service)

        # Call the appropriate generator based on the config provided
        n_days = configuration_selections.get_selections_by_configuration_id("n_days").value
        if n_days == 3:
            return self._generate_3_day_split(configuration_selections)
        elif n_days == 4:
            return self._generate_4_day_split(configuration_selections)
        elif n_days == 5:
            return self._generate_5_day_split(configuration_selections)

    @staticmethod
    def _generate_3_day_split(configuration_selections: ConfigurationSelectionGroup):

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

        return "3 day split"

    @staticmethod
    def _generate_4_day_split(configuration_selections: ConfigurationSelectionGroup):
        return "4 day split"

    @staticmethod
    def _generate_5_day_split(configuration_selections: ConfigurationSelectionGroup):
        return "5 day split"