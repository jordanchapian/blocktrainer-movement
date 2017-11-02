from typing import Dict


class ConfigurationTypes(object):
    DISCRETE_SELECTION = "discrete_selection"


class ConfigurationKeys(object):
    NUMBER_OF_DAYS = "n_days"


class ConfigurationSelection:
    def __init__(self, key, selection):
        self.__selection = selection
        self.__key = key

    def validate(self):
        return True


class ConfigurationOption:

    def __init__(self, key, configuration_type, configuration):
        self.__configuration = configuration
        self.__key = key
        self.__configuration_type = configuration_type

    def validate(self):
        return True

    def to_dict(self) -> Dict:
        return {
            "key": self.__key,
            "configuration_type": self.__configuration_type,
            "configuration": self.__configuration
        }
