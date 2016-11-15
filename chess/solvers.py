from abc import ABCMeta, abstractmethod
from collections import deque
from itertools import permutations

from .structures import Board


class Solver(metaclass=ABCMeta):

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
        self.time = 0

    @classmethod
    @abstractmethod
    def identifier(cls) -> str:
        """Solver unique identifier

        Returns:
            Unique identifier
        """
        pass

    @abstractmethod
    def solutions(self):
        """Generator of available solutions

        Yields:
            Board: Solution board
        """
        pass


class NaiveBruteForceSolver(Solver):
    """
    TODO: Fix this, is not working properly
    """

    @classmethod
    def identifier(cls) -> str:
        return 'naive'

    def __init__(self, rows: int, cols: int, pieces: list):
        super(NaiveBruteForceSolver, self).__init__(rows, cols, pieces)

    def solutions(self):
        available_pieces = []
        for piece, count in self.pieces:
            for _ in range(count):
                available_pieces.append(piece())

        for pieces in permutations(available_pieces):
            for row in range(self.rows):
                for col in range(self.cols):
                    available_pieces = deque(pieces)
                    board = Board.new(self.rows, self.cols)
                    while available_pieces and board.next_position()[0] is not None:
                        next_piece = available_pieces.popleft()
                        for arow, acol in board.available_positions():
                            if board.add_piece(next_piece, arow, acol):
                                break
                        else:
                            available_pieces.appendleft(next_piece)
                            del board
                            break

                    if not available_pieces:
                        yield board
