import unittest

from chess.structures import Board, KingPiece, QueenPiece, BishopPiece, RookPiece, KnightPiece


class PieceTestCase(unittest.TestCase):

    def setUp(self):
        self.board = Board.new(5, 5)

    def tearDown(self):
        del self.board


class TestKingPiece(PieceTestCase):

    def test_central_positions(self):
        positions = list(KingPiece.positions(self.board, 2, 2))
        self.assertEqual(positions, [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)])

    def test_upper_left_positions(self):
        positions = list(KingPiece.positions(self.board, 0, 0))
        self.assertEqual(positions, [(0, 1), (1, 0), (1, 1)])


class TestQueenPiece(PieceTestCase):

    def test_central_positions(self):
        positions = list(QueenPiece.positions(self.board, 2, 2))
        self.assertEqual(len(set(positions)), 16)

    def test_upper_left_positions(self):
        positions = list(QueenPiece.positions(self.board, 0, 0))
        self.assertEqual(len(set(positions)), 12)


class TestBishopPiece(PieceTestCase):

    def test_central_positions(self):
        positions = list(BishopPiece.positions(self.board, 2, 2))
        self.assertEqual(len(set(positions)), 8)

    def test_upper_left_positions(self):
        positions = list(BishopPiece.positions(self.board, 0, 0))
        self.assertEqual(len(set(positions)), 4)


class TestRookPiece(PieceTestCase):

    def test_central_positions(self):
        positions = list(RookPiece.positions(self.board, 2, 2))
        self.assertEqual(len(set(positions)), 8)

    def test_upper_left_positions(self):
        positions = list(RookPiece.positions(self.board, 0, 0))
        self.assertEqual(len(set(positions)), 8)


class TestKnightPiece(PieceTestCase):

    def test_central_positions(self):
        positions = list(KnightPiece.positions(self.board, 2, 2))
        self.assertEqual(positions, [(0, 1), (0, 3), (1, 0), (1, 4), (3, 0), (3, 4), (4, 1), (4, 3)])

    def test_upper_left_positions(self):
        positions = list(KnightPiece.positions(self.board, 0, 0))
        self.assertEqual(positions, [(1, 2), (2, 1)])


if __name__ == '__main__':
    unittest.main()