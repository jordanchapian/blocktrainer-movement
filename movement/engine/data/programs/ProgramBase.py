from abc import abstractmethod, ABCMeta
from typing import List, Dict
from engine.data.programs.configuration import ConfigurationSelection, ConfigurationOptionGroup


class ProgramBase(metaclass=ABCMeta):

    @property
    @abstractmethod
    def configuration_options(self) -> ConfigurationOptionGroup:
        return ConfigurationOptionGroup([])

    @property
    @abstractmethod
    def id(self):
        return None

    @abstractmethod
    def to_dict(self) -> Dict:
        return {}

    @abstractmethod
    def generate_split(self, configuration_selections: List[ConfigurationSelection]):
        return []


def program_to_dict(program: ProgramBase) -> Dict:
    output = {
        'id': program.id,
        'configuration_options': list(map(lambda x: x.to_dict(), program.configuration_options.options))
    }

    return output
