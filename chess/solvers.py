from abc import ABCMeta, abstractmethod


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


class BruteForceSolver(Solver):

    @classmethod
    def identifier(cls) -> str:
        return 'brute'

    def __init__(self, rows: int, cols: int, pieces: list):
        super(BruteForceSolver, self).__init__(rows, cols, pieces)

    def solutions(self):
        pass
