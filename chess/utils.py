"""
chess.utils
===========

This module contains utility functions used by the rest of the project.
"""


def piece_character_parameter(piece_name: str) -> str:
    """Returns the character which represent a piece

    Args:
        piece_name: Piece name

    Returns:
        Representational character
    """
    for c in piece_name:
        if c.isupper():
            return '-%s' % c


def piece_pluralized(piece_name: str) -> str:
    """Returns the pluralized version of a piece name

    Args:
        piece_name: Piece name

    Returns:
        Pluralized name
    """
    return '%ss' % piece_name.lower()


def capitalize(piece_name: str) -> str:
    """Returns a capitalized version of a piece name

    Args:
        piece_name: Piece name

    Returns:
        Capitalized version
    """
    return '%s%s' % (piece_name[0].upper(), piece_name[1:].lower())


__author__ = 'Roberto Antonio Becerra García <idertator@gmail.com>'
