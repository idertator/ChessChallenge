from chess.solvers import NaiveBruteForceSolver
from chess.structures import KingPiece, QueenPiece, BishopPiece, RookPiece, KnightPiece


if __name__ == '__main__':
    # ROWS = 3
    # COLS = 3
    # PIECES = (
    #     (KingPiece, 2),
    #     (RookPiece, 1),
    # )

    ROWS = 4
    COLS = 4
    PIECES = (
        (RookPiece, 2),
        (KnightPiece, 4),
    )


    solver = NaiveBruteForceSolver(rows=ROWS, cols=COLS, pieces=PIECES)

    solutions = {solution for solution in solver.solutions()}

    print(len(solutions))
    for solution in solutions:

        print(solution.hash)
        print(solution.state)
        print()