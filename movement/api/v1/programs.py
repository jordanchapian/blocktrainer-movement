from engine.data.programs import ProgramsAPI
from http import HTTPStatus
from collections import Iterable
from engine.data.programs.configuration import ConfigurationSelection, ConfigurationSelectionGroup


def search():
    return list(map(lambda x: x.to_dict(), ProgramsAPI.get_all()))


def generate_split(program_id, config):
    program = ProgramsAPI.get(program_id)

    if program is None:
        return "Program Not Found", HTTPStatus.NOT_FOUND

    # Ensure that the provided configration is iterable
    if not isinstance(config, Iterable):
        return "Invalid Input", HTTPStatus.BAD_REQUEST

    # Convert the provided config to configuration objects
    config_mapped = list(map(lambda x: ConfigurationSelection(x['configuration_id'], x['value']), config))
    config_group = ConfigurationSelectionGroup(config_mapped)

    # Ensure that we have valid configuration
    if not program.configuration_options.validate_selections(config_mapped):
        return "Invalid Input", HTTPStatus.BAD_REQUEST

    # Generate the split
    return program.generate_split(config_group)
