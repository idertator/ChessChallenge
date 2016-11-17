import unittest

from chess.structures import Board, KingPiece, QueenPiece, BishopPiece, RookPiece, KnightPiece
from chess.solvers import RecursiveBruteForceSolver


class TestRecursiveBruteForce(unittest.TestCase):

    def test_3_3_board(self):

        pieces = [
            (KingPiece, 2),
            (RookPiece, 1),
        ]
        solver = RecursiveBruteForceSolver(rows=3, cols=3, pieces=pieces)
        set1 = {frozenset(solution.pieces) for solution in solver.solutions()}

        self.assertEqual(len(set1), 4)

        solution1 = Board.new(3, 3)
        solution1.add_piece(KingPiece, 0, 0)
        solution1.add_piece(KingPiece, 0, 2)
        solution1.add_piece(RookPiece, 2, 1)
        self.assertIn(solution1.pieces, set1)

        solution2 = Board.new(3, 3)
        solution2.add_piece(KingPiece, 0, 0)
        solution2.add_piece(RookPiece, 1, 2)
        solution2.add_piece(KingPiece, 2, 0)
        self.assertIn(solution2.pieces, set1)

        solution3 = Board.new(3, 3)
        solution3.add_piece(KingPiece, 0, 2)
        solution3.add_piece(RookPiece, 1, 0)
        solution3.add_piece(KingPiece, 2, 2)
        self.assertIn(solution3.pieces, set1)

        solution4 = Board.new(3, 3)
        solution4.add_piece(RookPiece, 0, 1)
        solution4.add_piece(KingPiece, 2, 0)
        solution4.add_piece(KingPiece, 2, 2)
        self.assertIn(solution4.pieces, set1)