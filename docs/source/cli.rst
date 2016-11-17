CLI basic usage
===============

Examples
^^^^^^^^

For instance, to solve a 3x3 board with 2 rooks and 4 knights using the default solver you use::

    chess_challenge.py -bs 3 3 -R 2 -N 4

To specify a solver (*recursive* in this example) you add `-s` option::

    chess_challenge.py -bs 3 3 -R 2 -N 4 -s recursive

To print only the solutions count use the `-co` option::

    chess_challenge.py -bs 3 3 -R 2 -N 4 -s recursive -co

To see full command help type::

    chess_challenge.py -h


