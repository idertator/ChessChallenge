"""
chess.formats
=============

This module contains functions to print board solutions in different formats.

Attributes:
    FORMAT_DICT (dict): Dictionary which maps format identifiers to their functions
    FORMAT_DEFAULT (str): Default output format
"""


from .structures import Board, PIECES_LIST
from .utils import piece_character

_PIECE_TRANSLATION = {piece.identifier(): piece_character(piece.name()) for piece in PIECES_LIST}
_ART_TRANSLATION = {piece.identifier(): piece.art() for piece in PIECES_LIST}


def print_matrix_format(board: Board):
    """Prints the solution board using a simple matrix format

    Args:
        board: Solution board
    """
    for row in range(board.rows):
        for col in range(board.cols):
            if board.state[row][col] > 1:
                print(_PIECE_TRANSLATION[board.state[row][col]], end=' ')
            else:
                print('-', end=' ')
        print()
    print()


def print_pieces_format(board: Board):
    """Prints the solution board using a compact list with the pieces and their positions

    Args:
        board: Solution board
    """
    for piece in board.pieces:
        piece_char = _PIECE_TRANSLATION[(piece & 0x000F) + 2]
        piece_row = (piece & 0x03F0) >> 4
        piece_col = (piece & 0xFC00) >> 10
        print('%s[%d,%d]' % (piece_char, piece_row, piece_col), end=' ')
    print()


def print_fancy_format(board: Board):
    """Prints the solution board using fancy unicode artwork

    Args:
        board: Solution board
    """
    print('┌', end='')
    for _ in range(board.cols - 1):
        print('───', end='┬')
    print('───┐')
    for row in range(board.rows):
        print('│', end='')
        for col in range(board.cols):
            if board.state[row][col] > 1:
                print(' %s ' % _ART_TRANSLATION[board.state[row][col]], end='│')
            else:
                print('   ', end='│')
        print()
        if row < board.rows - 1:
            print('├', end='')
        else:
            print('└', end='')
        for col in range(board.cols - 1):
            if row < board.rows - 1:
                print('───', end='┼')
            else:
                print('───', end='┴')
        if row < board.rows - 1:
            print('───┤')
        else:
            print('───┘')
    print()

FORMAT_DICT = {
    'fancy': print_fancy_format,
    'matrix': print_matrix_format,
    'pieces': print_pieces_format,
}

FORMAT_DEFAULT = 'fancy'


__author__ = 'Roberto Antonio Becerra García <idertator@gmail.com>'
