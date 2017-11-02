from engine.data.programs import ProgramsAPI
from http import HTTPStatus


def search():
    return list(map(lambda x: x.to_dict(), ProgramsAPI.get_all()))


def generate_split(program_key, config):
    program = ProgramsAPI.get(program_key)

    if program is None:
        return "Program Not Found", HTTPStatus.NOT_FOUND

    return program.generate_split(config)
