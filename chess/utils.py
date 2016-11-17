def piece_character_parameter(piece_name: str) -> str:
    for c in piece_name:
        if c.isupper():
            return '-%s' % c


def piece_pluralized(piece_name: str) -> str:
    return '%ss' % piece_name.lower()


def first_uppercase(piece_name: str) -> str:
    return '%s%s' % (piece_name[0].upper(), piece_name[1:].lower())
