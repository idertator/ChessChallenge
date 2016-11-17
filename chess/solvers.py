from abc import ABCMeta, abstractmethod
from time import time

from .structures import Board
from .utils import piece_pluralized, capitalize


_SOLVER_REPR_TEMPLATE = '''Solver     : %s
Board size : (%s, %s)
Pieces     :
%s
'''


class Solver(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def identifier(cls) -> str:
        """Solver unique identifier

        Returns:
            Unique identifier
        """
        pass

    @abstractmethod
    def _solutions(self):
        """Generator of available solutions

        Yields:
            Board: Solution board
        """
        pass

    def __init__(self, rows: int, cols: int, pieces: list):
        """Abstract base class for solvers

        Args:
            rows: Row count
            cols: Column count
            pieces: List of tuples of two elements (Piece, Count)
        """
        self.rows = rows
        self.cols = cols
        self.pieces = pieces
        self._time = 0

    def solutions(self):
        """Generator of available solutions

        Yields:
            Board: Solution board
        """
        self._time = time()
        yield from self._solutions()
        self._time = time() - self._time

    @property
    def time(self) -> float:
        """Time used for the computation in seconds"""
        return self._time

    def __str__(self):
        return _SOLVER_REPR_TEMPLATE % (
            self.identifier(),
            self.rows, self.cols,
            '\n'.join(['\t* %s: %d' % (capitalize(piece_pluralized(piece.name())), count)
                       for piece, count in self.pieces if count > 0])
        )


class RecursiveBruteForceSolver(Solver):
    """ Recursive brute force solver

    Uses a recursive backtracking technique to test all possible solutions.
    The solver uses the set *completed* to avoid repeating calculations from
    the same combination of pieces and locations.
    """

    completed_set = None
    solutions_set = None

    @classmethod
    def identifier(cls):
        return 'recursive'

    def _solutions(self):
        available_pieces = []
        for piece, count in self.pieces:
            for _ in range(count):
                available_pieces.append(piece())

        RecursiveBruteForceSolver.completed_set = set()
        RecursiveBruteForceSolver.solutions_set = set()

        board = Board.new(self.rows, self.cols)
        yield from RecursiveBruteForceSolver._solutions_recursive(board, available_pieces)

    @staticmethod
    def _solutions_recursive(board: Board, pieces: list):
        if board.next_position()[0] is not None:
            next_board = board.copy()
            for index, piece in enumerate(pieces):
                for next_row, next_col in board.available_positions():
                    if next_board.add_piece(piece, next_row, next_col):
                        if len(pieces) == 1 and next_board.pieces not in RecursiveBruteForceSolver.solutions_set:
                            RecursiveBruteForceSolver.solutions_set.add(frozenset(next_board.pieces))
                            yield next_board
                        elif next_board.pieces not in RecursiveBruteForceSolver.completed_set:
                            next_pieces = pieces.copy()
                            del next_pieces[index]
                            yield from RecursiveBruteForceSolver._solutions_recursive(next_board, next_pieces)
                        next_board = board.copy()

        RecursiveBruteForceSolver.completed_set.add(frozenset(board.pieces))


SOLVERS_LIST = (
    RecursiveBruteForceSolver,
)

SOLVERS_DICT = {solver.identifier(): solver for solver in SOLVERS_LIST}




