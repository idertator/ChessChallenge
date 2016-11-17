#!python3

import argparse

from chess.solvers import SOLVERS_LIST, SOLVERS_DICT
from chess.structures import PIECES_LIST
from chess.utils import piece_character_parameter, piece_pluralized, capitalize


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='ChessChallenge',
        description='Solves the Chess Challenge'
    )

    parser.add_argument(
        '-co', '--count-only',
        dest='count_only',
        action='store_true',
        help='only prints the final solution count'
    )

    parser.add_argument(
        '-s', '--solver',
        dest='solver',
        type=str, default=SOLVERS_LIST[0].identifier(),
        required=False,
        help='which solver use to find solutions'
    )

    parser.add_argument(
        '-bs', '--board-size',
        dest='size',
        type=int, nargs=2,
        required=True,
        help='board size (rows, colums)'
    )

    parser.add_argument(
        '-V', '--version',
        action='version',
        version='chessChallenge v0.1'
    )

    for piece in PIECES_LIST:
        parser.add_argument(
            piece_character_parameter(piece.name()), ('--%s' % piece_pluralized(piece.name())),
            dest=piece.name(),
            type=int, default=0,
            required=False,
            help='%s pieces count' % piece.name().lower()
        )

    args = parser.parse_args()
    rows, cols = args.size

    pieces = [(piece, getattr(args, piece.name())) for piece in PIECES_LIST if getattr(args, piece.name()) > 0]

    solver = SOLVERS_DICT[args.solver](
        rows, cols, pieces
    )

    solution_count = 0
    for solution in solver.solutions():
        solution_count += 1
        if not args.count_only:
            print(solution.state)

    print('%d solutions found in %.2f seconds' % (solution_count, solver.time))