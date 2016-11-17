#!python3

from chess.solvers import RecursiveBruteForceSolver
from chess.structures import KingPiece, QueenPiece, BishopPiece, RookPiece, KnightPiece


if __name__ == '__main__':
    ROWS = 7
    COLS = 7
    PIECES = (
        (KingPiece, 2),
        (QueenPiece, 2),
        (BishopPiece, 2),
        (KnightPiece, 1),
    )

    solver = RecursiveBruteForceSolver(rows=ROWS, cols=COLS, pieces=PIECES)

    solution_count = 0
    for solution in solver.solutions():
        solution_count += 1
        #print(solution.pieces)

    print(len(solver.solutions_set))
    print('%s solutions founded in %.2f seconds' % (solution_count, solver.time))