from typing import List


class BlockInstance:

    def __init__(self, block):
        self._block = block
        self._equipment_restrictions = []
        self._n_occurrences = 1
        self._rep_and_set_method = None
        self._rep_and_set_method_args = None

    @property
    def equipment_restriction(self) -> List:
        return self._equipment_restrictions

    @property
    def n_occurrences(self) -> int:
        return self._n_occurrences

    def set_static_reps_and_sets(self, reps, sets) -> 'BlockInstance':
        self._rep_and_set_method = "Static"
        self._rep_and_set_method_args = {
            reps: reps,
            sets: sets
        }
        return self

    def set_equipment_restriction(self, equipment_restrictions: List) -> 'BlockInstance':
        self._equipment_restrictions = equipment_restrictions
        return self

    def set_n_occurrences(self, n) -> 'BlockInstance':
        self._n_occurrences = n
        return self
