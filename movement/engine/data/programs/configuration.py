from typing import Dict
from collections import Iterable
from logging import getLogger

logger = getLogger("Some Logger")


class ConfigurationTypes(object):
    DISCRETE_SELECTION = "discrete_selection"


class ConfigurationIds(object):
    NUMBER_OF_DAYS = "n_days"
    INTENSITY = "intensity"


class ConfigurationSelectionGroup:
    def __init__(self, configuration_selections):
        self.__configuration_selections = configuration_selections
        self.__configuration_selections_map = {x.configuration_id: x for x in self.__configuration_selections}

    @property
    def selections(self):
        return self.__configuration_selections

    def get_selections_by_configuration_id(self, configuration_id):
        return self.__configuration_selections_map[configuration_id]


class ConfigurationSelection:
    def __init__(self, configuration_id=None, value=None):
        self.__configuration_id = configuration_id
        self.__value = value

    @property
    def configuration_id(self):
        return self.__configuration_id

    @property
    def value(self):
        return self.__value


class ConfigurationOptionGroup:

    def __init__(self, options):
        self.__options = options
        self.__options_map = {x.id: x for x in self.__options}

    def validate_selections(self, selections):
        # Ensure that the selections are iterable
        if not isinstance(selections, Iterable):
            return False

        # Ensure that each of the selections provided are of the appropriate class
        for selection in selections:
            if not isinstance(selection, ConfigurationSelection):
                return False

        # Ensure that the required options are present
        for required_option in filter(lambda x: x.required, self.__options):
            found = False
            for provided_selection in selections:
                if provided_selection.configuration_id == required_option.id:
                    found = True
                    break
            if not found:
                return False

        # Ensure that the provided values work for the configuration option
        for selection in selections:
            if selection.configuration_id in self.__options_map:
                if not self.__options_map[selection.configuration_id].value_is_valid(selection.value):
                    return False

        # Passed all checks
        return True

    @property
    def options(self):
        return self.__options

    def validate_configuration(self):
        for configOption in self.__options:
            if not configOption.is_valid():
                return False
        return True


class ConfigurationOption:

    def __init__(self, configuration_id, configuration_type, type_settings, required=False):
        self.__type_settings = type_settings
        self.__id = configuration_id
        self.__configuration_type = configuration_type
        self.__required = required
    
    @property
    def id(self):
        return self.__id
    
    @property
    def type(self):
        return self.__configuration_type

    @property
    def required(self):
        return self.__required

    @property
    def type_settings(self):
        return self.__type_settings

    @staticmethod
    def configuration_is_valid(self):
        # This is kind of an optimization so we can catch issues on compile
        return True

    def value_is_valid(self, selection):
        return True

    def to_dict(self) -> Dict:
        return {
            "id": self.__id,
            "type": self.__configuration_type,
            "type_settings": self.__type_settings
        }
