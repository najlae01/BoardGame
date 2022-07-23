#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file                 : Pawn.py
@author               : NAJLAE
@time                 : 2022-24-4 17:00:00
@email                : abarghachenajlae@gmail.com
"""

from Board import Board


class Pawn:
    """Represent a Pawn in the Board.

       Public methods: __init__, get_row, get_col,
       move_to, take_turn, __str__
    """

    # Annotate fields
    __row: int  # The row that a Pawn is at
    __col: int  # The column that a Pawn is at
    __symbol: str  # A character to represent a Pawn
    _board: Board   # A board that a Pawn is at

    def __init__(self, row: int, col: int, board: Board, symbol: str) -> None:
        """Initialize __row, __col, __symbol and _board to the values passed and
           add this Pawn instance to the _board object."""
        self.__row = row
        self.__col = col
        self._board = board
        self.__symbol = symbol
        self._board.add_pawn(self, self.__row, self.__col)

    def get_row(self) -> int:
        """Return the row that this Pawn is at (int)."""
        return self.__row

    def get_col(self) -> int:
        """Return the column that this Pawn is at (int). """
        return self.__col

    def move_to(self, new_row: int, new_col: int) -> bool:
        """Used by the subclasses to move the Pawn to a new
         location (new row and column) when they take turn.
         It deletes this Pawn from its current location and
         adds it in a new location within the board. """
        self._board.delete_pawn(self, self.__row, self.__col)
        self.__row = new_row
        self.__col = new_col
        return self._board.add_pawn(self, new_row, new_col)

    def take_turn(self) -> None:
        """Will be implemented in the subclasses.
         It when the Pawn take a turn."""

    def __str__(self) -> str:
        """Return the symbol of this Pawn."""
        return self.__symbol

