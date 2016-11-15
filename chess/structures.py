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
            (int, int): Available row and column position in a tuple (row, column)
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
            (int, int): Available row and column position in a tuple (row, column)
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
            (int, int): Available row and column position in a tuple (row, column)
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

    def __str__(self):
        return 'K'

class QueenPiece(AbstractPiece):

    @classmethod
    def identifier(cls):
        return 3

    @classmethod
    def positions(cls, board, row: int, col: int):
        yield from AbstractPiece.positions_run(board, row, col, _KING_QUEEN_MOVES)

    def __str__(self):
        return 'Q'


class BishopPiece(AbstractPiece):

    @classmethod
    def identifier(cls):
        return 4

    @classmethod
    def positions(cls, board, row: int, col: int):
        yield from AbstractPiece.positions_run(board, row, col, _BISHOP_MOVES)

    def __str__(self):
        return 'B'


class RookPiece(AbstractPiece):

    @classmethod
    def identifier(cls):
        return 5

    @classmethod
    def positions(cls, board, row: int, col: int):
        yield from AbstractPiece.positions_run(board, row, col, _ROOK_MOVES)

    def __str__(self):
        return 'R'


class KnightPiece(AbstractPiece):

    @classmethod
    def identifier(cls):
        return 6

    @classmethod
    def positions(cls, board, row: int, col: int):
        yield from AbstractPiece.positions_step(board, row, col, _KNIGHT_MOVES)

    def __str__(self):
        return 'N'


PIECES_LIST = [KingPiece, QueenPiece, BishopPiece, RookPiece, KnightPiece]
PIECES_DICT = {piece.identifier(): piece for piece in PIECES_LIST}


class Board:
    __slots__ = ['state', 'hash', '_next_row', '_next_col']

    @staticmethod
    def new(rows: int, cols: int):
        state = zeros((rows, cols), dtype=uint8)
        return Board(state)

    def __init__(self, state: ndarray, next_position: tuple=(0, 0)):
        """Board representation

        Args:
            state: State of each slot in the board
            next_position (optional): Next available position (row, column)
        """
        self.state = state
        self.hash = ''
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
            self.hash = '%s%s%d%d' % (self.hash, str(piece), row, col)
            return True

    @property
    def rows(self) -> int:
        """Board row count"""
        return self.state.shape[0]

    @property
    def cols(self) -> int:
        """Board column count"""
        return self.state.shape[1]

    def clone(self):
        """Creates new identical Board object

        Returns:
            Board: Cloned object
        """
        return Board(state=self.state.copy(), next_position=(self._next_row, self._next_col))

    def next_position(self) -> tuple:
        """Next available position in the board

        Returns:
            tuple(int, int): Position (row, column)
        """
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

    def available_positions(self):
        """Generator of board available positions

        Yields:
            (int, int): Available row and column position in a tuple (row, column)
        """
        next_row, next_col = self.next_position()

        if next_row is not None:
            col = next_col
            for row in range(next_row, self.rows):
                while col < self.cols:
                    if self.state[row][col] == 0:
                        yield row, col
                    col += 1
                col = 0

    def __hash__(self):
        return self.hash.__hash__()

    def __eq__(self, other):
        return self.hash == other.hash

