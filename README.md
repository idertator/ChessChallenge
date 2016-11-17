# ChessChallenge

This package provides an Application Programming Interface (API) and a Command Line Interface (CLI) to
solve the following **challenge**:

    Find all unique configurations of a set of normal chess pieces on a chess board with dimensions MxN
    where none of the pieces is in a position to take any of the others. Assume the colour of the piece
    does not matter, and that there are no pawns among the pieces.

## Installation instructions

Currently we only support installing from sources. A version of the package will be uploaded to
the Python Package Index soon.

### Building from source

#### Prerequisites

Bulding ChessChallenge requires the following software installed:

    1. Python 3.3.x or newer. The official python installer at www.python.org is enough.
    2. NumPy 1.x. You can install it from the Python Package Index using the **pip** command.
    3. Sphinx 1.4.x or newer. This is an optional dependency required only to build de docs.

We encourage to users installing the `Anaconda Distribution <https://www.continuum.io/downloads>`_
from Continuum Analytics to use this package.

#### Installation

To install ChessChallenge run de following command in the root directory of the package::

    python setup.py install

## Basic CLI usage

### Examples

For instance, to solve a 3x3 board with 2 rooks and 4 knights using the default solver you use::

    chess_challenge.py -bs 3 3 -R 2 -N 4

To specify a solver (*recursive* in this example) you add `-s` option::

    chess_challenge.py -bs 3 3 -R 2 -N 4 -s recursive

To print only the solutions count use the `-co` option::

    chess_challenge.py -bs 3 3 -R 2 -N 4 -s recursive -co

To see full command help type::

    chess_challenge.py -h
