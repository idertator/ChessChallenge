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


class AbstractPiece(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def identifier(cls) -> int:
        """Piece unique identifier

        Returns:
            Unique identifier
        """
        pass

    @classmethod
    @abstractmethod
    def positions(cls, board, row: int, col: int):
        """Generator of available attacking slots

        Args:
            board: Board object
            row: Row number starting at 0
            col: Column number starting at 0

        Yields:
            (int, int): Available row and column position in a tuple (row, col)
        """
        yield (None, None)

    @classmethod
    def positions_step(cls, board, row: int, col: int, moves: tuple):
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
    def positions_run(cls, board, row: int, col: int, moves: tuple):
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
        return 2

    @classmethod
    def positions(cls, board, row: int, col: int):
        yield from AbstractPiece.positions_step(board, row, col, _KING_QUEEN_MOVES)


class QueenPiece(AbstractPiece):

    @classmethod
    def identifier(cls):
        return 3

    @classmethod
    def positions(cls, board, row: int, col: int):
        yield from AbstractPiece.positions_run(board, row, col, _KING_QUEEN_MOVES)


class BishopPiece(AbstractPiece):

    @classmethod
    def identifier(cls):
        return 4

    @classmethod
    def positions(cls, board, row: int, col: int):
        yield from AbstractPiece.positions_run(board, row, col, _BISHOP_MOVES)


class RookPiece(AbstractPiece):

    @classmethod
    def identifier(cls):
        return 5

    @classmethod
    def positions(cls, board, row: int, col: int):
        yield from AbstractPiece.positions_run(board, row, col, _ROOK_MOVES)


class KnightPiece(AbstractPiece):

    @classmethod
    def identifier(cls):
        return 6

    @classmethod
    def positions(cls, board, row: int, col: int):
        yield from AbstractPiece.positions_step(board, row, col, _KNIGHT_MOVES)


PIECES_LIST = [KingPiece, QueenPiece, BishopPiece, RookPiece, KnightPiece]
PIECES_DICT = {piece.identifier(): piece for piece in PIECES_LIST}


class Board:
    __slots__ = ['state', '_next_row', '_next_col']

    @staticmethod
    def new(rows: int, cols: int):
        state = zeros((rows, cols), dtype=uint8)
        return Board(state)

    @staticmethod
    def copy(board):
        pass

    def __init__(self, state: ndarray, next_position: tuple=(0, 0)):
        """

        Args:
            state:
            next_position:
        """
        self.state = state
        self._next_row, self._next_col = next_position

    def add_piece(self, piece: AbstractPiece, row: int, col: int) -> bool:
        """Try to add a new piece to the board

        Args:
            piece: Piece class
            row: Row number starting at 0
            col: Column number starting at 0

        Returns:
            int: True if the piece was added successfully, False otherwise
        """
        if self.state[row][col] != 0:
            return False

        for drow, dcol in piece.positions(self, row, col):
            if self.state[drow][dcol] > 1:
                return False
        else:
            self.state[row][col] = piece.identifier()
            for drow, dcol in piece.positions(self, row, col):
                self.state[drow][dcol] = 1
            return True

    @property
    def rows(self):
        return self.state.shape[0]

    @property
    def cols(self):
        return self.state.shape[1]

    def clone(self):
        return Board(state=self.state.copy(), next_position=(self._next_row, self._next_col))

    def next_position(self):
        while self.state[self._next_row][self._next_col] != 0:
            if self._next_col < self.cols - 1:
                self._next_col += 1
            elif self._next_row < self.rows - 1:
                self._next_row += 1
                self._next_col = 0
            else:
                return None, None

        if self.state[self._next_row][self._next_col] != 0:
            return None, None
        return self._next_row, self._next_col



