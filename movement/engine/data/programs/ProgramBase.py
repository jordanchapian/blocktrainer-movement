from abc import abstractmethod, ABCMeta
from typing import List, Dict
from engine.data.programs.configurationOptions import ConfigurationSelection


class ProgramBase(metaclass=ABCMeta):

    @property
    @abstractmethod
    def configuration_options(self):
        return []

    @property
    @abstractmethod
    def key(self):
        return None

    @abstractmethod
    def to_dict(self) -> Dict:
        return {}

    @abstractmethod
    def generate_split(self, configuration_selections: List[ConfigurationSelection]):
        return []


def program_to_dict(program: ProgramBase) -> Dict:
    output = {
        'key': program.key,
        'configuration_options': list(map(lambda x: x.to_dict(), program.configuration_options))
    }

    return output
