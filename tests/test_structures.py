import unittest

from numpy import array, uint8

from chess.structures import Board, KingPiece, QueenPiece, BishopPiece, RookPiece, KnightPiece


class StructuresTestCase(unittest.TestCase):

    def setUp(self):
        self.board = Board.new(5, 5)

    def tearDown(self):
        del self.board


class TestKingStructures(StructuresTestCase):

    def test_central_positions(self):
        positions = list(KingPiece.positions(self.board, 2, 2))
        self.assertEqual(positions, [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)])

    def test_upper_left_positions(self):
        positions = list(KingPiece.positions(self.board, 0, 0))
        self.assertEqual(positions, [(0, 1), (1, 0), (1, 1)])


class TestQueenStructures(StructuresTestCase):

    def test_central_positions(self):
        positions = list(QueenPiece.positions(self.board, 2, 2))
        self.assertEqual(len(set(positions)), 16)

    def test_upper_left_positions(self):
        positions = list(QueenPiece.positions(self.board, 0, 0))
        self.assertEqual(len(set(positions)), 12)


class TestBishopStructures(StructuresTestCase):

    def test_central_positions(self):
        positions = list(BishopPiece.positions(self.board, 2, 2))
        self.assertEqual(len(set(positions)), 8)

    def test_upper_left_positions(self):
        positions = list(BishopPiece.positions(self.board, 0, 0))
        self.assertEqual(len(set(positions)), 4)


class TestRookStructures(StructuresTestCase):

    def test_central_positions(self):
        positions = list(RookPiece.positions(self.board, 2, 2))
        self.assertEqual(len(set(positions)), 8)

    def test_upper_left_positions(self):
        positions = list(RookPiece.positions(self.board, 0, 0))
        self.assertEqual(len(set(positions)), 8)


class TestKnightStructures(StructuresTestCase):

    def test_central_positions(self):
        positions = list(KnightPiece.positions(self.board, 2, 2))
        self.assertEqual(positions, [(0, 1), (0, 3), (1, 0), (1, 4), (3, 0), (3, 4), (4, 1), (4, 3)])

    def test_upper_left_positions(self):
        positions = list(KnightPiece.positions(self.board, 0, 0))
        self.assertEqual(positions, [(1, 2), (2, 1)])


class TestBoard(StructuresTestCase):

    def test_add_piece_and_next_position(self):
        self.assertTrue(self.board.add_piece(KingPiece, 0, 3))
        state = array([
            [0, 0, 1, 2, 1],
            [0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ], dtype=uint8)
        self.assertTrue((self.board.state == state).all())
        self.assertEqual(self.board.next_position(), (0, 0))

        self.assertTrue(self.board.add_piece(QueenPiece, 4, 4))
        state = array([
            [1, 0, 1, 2, 1],
            [0, 1, 1, 1, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 1, 3],
        ], dtype=uint8)
        self.assertTrue((self.board.state == state).all())
        self.assertEqual(self.board.next_position(), (0, 1))

        self.assertTrue(self.board.add_piece(BishopPiece, 1, 0))
        state = array([
            [1, 1, 1, 2, 1],
            [4, 1, 1, 1, 1],
            [0, 1, 1, 0, 1],
            [0, 0, 1, 1, 1],
            [1, 1, 1, 1, 3],
        ], dtype=uint8)
        self.assertTrue((self.board.state == state).all())
        self.assertEqual(self.board.next_position(), (2, 0))

        self.assertTrue(self.board.add_piece(RookPiece, 3, 1))
        state = array([
            [1, 1, 1, 2, 1],
            [4, 1, 1, 1, 1],
            [0, 1, 1, 0, 1],
            [1, 5, 1, 1, 1],
            [1, 1, 1, 1, 3],
        ], dtype=uint8)
        self.assertTrue((self.board.state == state).all())
        self.assertEqual(self.board.next_position(), (2, 0))

        self.assertTrue(self.board.add_piece(KnightPiece, 2, 0))
        state = array([
            [1, 1, 1, 2, 1],
            [4, 1, 1, 1, 1],
            [6, 1, 1, 0, 1],
            [1, 5, 1, 1, 1],
            [1, 1, 1, 1, 3],
        ], dtype=uint8)
        self.assertTrue((self.board.state == state).all())
        self.assertEqual(self.board.next_position(), (2, 3))

        self.assertFalse(self.board.add_piece(KnightPiece, 2, 3))
        self.assertEqual(self.board.next_position(), (2, 3))
        self.assertFalse(self.board.add_piece(RookPiece, 2, 3))
        self.assertEqual(self.board.next_position(), (2, 3))
        self.assertFalse(self.board.add_piece(QueenPiece, 2, 3))
        self.assertEqual(self.board.next_position(), (2, 3))
        self.assertTrue(self.board.add_piece(BishopPiece, 2, 3))
        self.assertEqual(self.board.next_position(), (None, None))
        self.assertFalse(self.board.add_piece(KingPiece, 2, 3))
        self.assertEqual(self.board.next_position(), (None, None))


if __name__ == '__main__':
    unittest.main()