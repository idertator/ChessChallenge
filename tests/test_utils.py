import unittest

from chess.utils import piece_character, piece_pluralized, capitalized
from chess.structures import KingPiece, QueenPiece, BishopPiece, RookPiece, KnightPiece


class TestUtils(unittest.TestCase):

    def test_piece_character(self):
        self.assertEqual(piece_character(KingPiece.name()), 'K')
        self.assertEqual(piece_character(QueenPiece.name()), 'Q')
        self.assertEqual(piece_character(BishopPiece.name()), 'B')
        self.assertEqual(piece_character(RookPiece.name()), 'R')
        self.assertEqual(piece_character(KnightPiece.name()), 'N')

    def test_piece_pluralized(self):
        self.assertEqual(piece_pluralized(KingPiece.name()), 'kings')
        self.assertEqual(piece_pluralized(QueenPiece.name()), 'queens')
        self.assertEqual(piece_pluralized(BishopPiece.name()), 'bishops')
        self.assertEqual(piece_pluralized(RookPiece.name()), 'rooks')
        self.assertEqual(piece_pluralized(KnightPiece.name()), 'knights')

    def test_capitalized(self):
        self.assertEqual(capitalized(KingPiece.name()), 'King')
        self.assertEqual(capitalized(QueenPiece.name()), 'Queen')
        self.assertEqual(capitalized(BishopPiece.name()), 'Bishop')
        self.assertEqual(capitalized(RookPiece.name()), 'Rook')
        self.assertEqual(capitalized(KnightPiece.name()), 'Knight')