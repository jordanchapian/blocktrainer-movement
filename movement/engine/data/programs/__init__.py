from engine.data.programs.five_by_five import api as five_by_five_api
from engine.data.programs.ProgramBase import ProgramBase


class ProgramsAPI(object):

    __program_list = [
        five_by_five_api
    ]

    __program_list_map = {x.id: x for x in __program_list}

    print(__program_list)

    @staticmethod
    def get_all():
        return ProgramsAPI.__program_list

    @staticmethod
    def get(id: str) -> [ProgramBase, None]:
        if id not in ProgramsAPI.__program_list_map:
            return None
        else:
            return ProgramsAPI.__program_list_map[id]
