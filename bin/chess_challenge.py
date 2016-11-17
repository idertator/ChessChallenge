#!python3

from chess.solvers import RecursiveBruteForceSolver
from chess.structures import KingPiece, QueenPiece, BishopPiece, RookPiece, KnightPiece


if __name__ == '__main__':
    # ROWS = 3
    # COLS = 3
    # PIECES = (
    #     (KingPiece, 1),
    # )

    # ROWS = 3
    # COLS = 3
    # PIECES = [
    #     (KingPiece, 2),
    #     (RookPiece, 1),
    # ]

    # ROWS = 4
    # COLS = 4
    # PIECES = [
    #     (RookPiece, 2),
    #     (KnightPiece, 4),
    # ]

    ROWS = 5
    COLS = 5
    PIECES = [
        (KingPiece, 2),
        (QueenPiece, 1),
        (BishopPiece, 1),
        (KnightPiece, 1),
    ]

    # ROWS = 7
    # COLS = 7
    # PIECES = (
    #     (KingPiece, 2),
    #     (QueenPiece, 2),
    #     (BishopPiece, 2),
    #     (KnightPiece, 1),
    # )

    solver = RecursiveBruteForceSolver(rows=ROWS, cols=COLS, pieces=PIECES)

    solution_count = 0
    for solution in solver.solutions():
        solution_count += 1
        #print(solution.pieces)

    print(len(solver.solutions_set))
    print('%s solutions founded in %.2f seconds' % (solution_count, solver.time))