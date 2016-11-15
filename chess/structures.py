from abc import ABCMeta, abstractmethod
from numpy import ndarray, zeros, uint8


_KING_QUEEN_MOVES = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)

_BISHOP_MOVES = (
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
)

_ROOK_MOVES = (
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, 0),
)

_KNIGHT_MOVES = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1),
)


class Board:
    pass


class AbstractPiece(metaclass=ABCMeta):
    __slots__ = ('board', 'row', 'col')

    def __init__(self, board: Board, row: int, col: int):
        """Abstract piece base class

        Args:
            board: Board object
            row: Row number starting at 0
            col: Column number starting at 0
        """
        self.board = board
        self.row = row
        self.col = col

    @classmethod
    @abstractmethod
    def identifier(cls) -> int:
        """Piece unique identifier

        Returns:
            int: Unique identifier
        """
        pass

    @classmethod
    @abstractmethod
    def positions(cls, board: Board, row: int, col: int):
        """Generator of available attacking slots

        Args:
            board: Board object
            row: Row number starting at 0
            col: Column number starting at 0

        Yields:
            (int, int): Available row and column position in a tuple (row, col)
        """
        pass

    @classmethod
    @abstractmethod
    def check(cls, board: Board, row: int, col: int) -> bool:
        """Checks if an slot is avaliable for the piece in a board

        Args:
            board: Board object
            row: Row number starting at 0
            col: Column number starting at 0

        Returns:
            If the slot is available or not

        """
        pass

    @classmethod
    def positions_step(cls, board: Board, row: int, col: int, moves: tuple):
        """Generator of available attacking slots using only the specified moves

        Args:
            board: Board object
            row: Row number starting at 0
            col: Column number starting at 0
            moves: Candidates moves in a tuple of tuples with shape (row_delta, col_delta)

        Yields:
            (int, int): Available row and column position in a tuple (row, col)
        """
        for drow, dcol in moves:
            if 0 <= row + drow < board.rows and 0 <= col + dcol < board.cols:
                yield row + drow, col + dcol

    @classmethod
    def positions_run(cls, board: Board, row: int, col: int, moves: tuple):
        """Generator of available attacking slots by running the specified moves

        Args:
            board: Board object
            row: Row number starting at 0
            col: Column number starting at 0
            moves: Candidates moves in a tuple of tuples with shape (row_delta, col_delta)

        Yields:
            (int, int): Available row and column position in a tuple (row, col)
        """
        for drow, dcol in moves:
            if 0 <= row + drow < board.rows and 0 <= col + dcol < board.cols:
                yield row + drow, col + dcol
        for drow, dcol in moves:
            crow, ccol = row, col
            while 0 <= crow + drow < board.rows and 0 <= ccol + dcol < board.cols:
                yield crow + drow, ccol + dcol
                crow += drow
                ccol += dcol


class KingPiece(AbstractPiece):

    @classmethod
    def identifier(cls):
        return 1

    @classmethod
    def positions(cls, board: Board, row: int, col: int):
        yield from AbstractPiece.positions_step(board, row, col, _KING_QUEEN_MOVES)

    @classmethod
    def check(cls, board: Board, row: int, col: int):
        pass

    def __init__(self, board: Board, row: int, col: int):
        """King piece class

        Args:
            board: Board object
            row: Row number starting at 0
            col: Column number starting at 0
        """
        super(KingPiece, self).__init__(board, row, col)


class QueenPiece(AbstractPiece):

    @classmethod
    def identifier(cls):
        return 2

    @classmethod
    def positions(cls, board: Board, row: int, col: int):
        yield from AbstractPiece.positions_run(board, row, col, _KING_QUEEN_MOVES)

    @classmethod
    def check(cls, board: Board, row: int, col: int):
        pass

    def __init__(self, board: Board, row: int, col: int):
        """Queen piece class

        Args:
            board: Board object
            row: Row number starting at 0
            col: Column number starting at 0
        """
        super(QueenPiece, self).__init__(board, row, col)


class BishopPiece(AbstractPiece):

    @classmethod
    def identifier(cls):
        return 3

    @classmethod
    def positions(cls, board: Board, row: int, col: int):
        yield from AbstractPiece.positions_run(board, row, col, _BISHOP_MOVES)

    @classmethod
    def check(cls, board: Board, row: int, col: int):
        pass

    def __init__(self, board: Board, row: int, col: int):
        """Bishop piece class

        Args:
            board: Board object
            row: Row number starting at 0
            col: Column number starting at 0
        """
        super(BishopPiece, self).__init__(board, row, col)


class RookPiece(AbstractPiece):

    @classmethod
    def identifier(cls):
        return 4

    @classmethod
    def positions(cls, board: Board, row: int, col: int):
        yield from AbstractPiece.positions_run(board, row, col, _ROOK_MOVES)

    @classmethod
    def check(cls, board: Board, row: int, col: int):
        pass

    def __init__(self, board: Board, row: int, col: int):
        """Rook piece class

        Args:
            board: Board object
            row: Row number starting at 0
            col: Column number starting at 0
        """
        super(RookPiece, self).__init__(board, row, col)


class KnightPiece(AbstractPiece):

    @classmethod
    def identifier(cls):
        return 5

    @classmethod
    def positions(cls, board: Board, row: int, col: int):
        yield from AbstractPiece.positions_step(board, row, col, _KNIGHT_MOVES)

    @classmethod
    def check(cls, board: Board, row: int, col: int):
        pass

    def __init__(self, board: Board, row: int, col: int):
        """Knight piece class

        Args:
            board: Board object
            row: Row number starting at 0
            col: Column number starting at 0
        """
        super(KnightPiece, self).__init__(board, row, col)


PIECES_LIST = [KingPiece, QueenPiece, BishopPiece, RookPiece, KnightPiece]
PIECES_DICT = {piece.identifier(): piece for piece in PIECES_LIST}


class Board:
    __slots__ = 'board', 'state'

    @staticmethod
    def new(rows: int, cols: int):
        state = zeros((rows, cols), dtype=uint8)
        return Board(state)

    @staticmethod
    def copy(board):
        pass

    def __init__(self, state: ndarray):
        self.state = state

    @property
    def rows(self):
        return self.state.shape[0]

    @property
    def cols(self):
        return self.state.shape[1]

