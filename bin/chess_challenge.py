from numpy import ndarray, bool


class State:
    pass


class Board:
    __slots__ = 'board', 'state'

    @staticmethod
    def from_state(rows: int, cols: int, state: State=None):
        pass

    @staticmethod
    def copy(board):
        pass

    def __init__(self, hitted: ndarray, state: State):
        pass
