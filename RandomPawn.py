#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file                 : RandomPawn.py
@author               : NAJLAE
@time                 : 2022-24-4 17:00:00
@email                : abarghachenajlae@gmail.com
"""

from Board import Board
from Pawn import Pawn
import random


class RandomPawn(Pawn):
    """Represent a RandomPawn in the Board (a subclass of Pawn).

       Public methods: __init__, take_turn
    """

    def __init__(self, board: Board) -> None:
        """ This method generates randomly a row and a column
        to start with, this Pawn's symbol is R.
        This constructor calls the superclass Pawn's constructor
        to create this new RandomPawn object."""
        self._board = board
        row = random.randint(0, self._board.get_num_rows()-1)
        col = random.randint(0, self._board.get_num_cols()-1)
        symbol = "R"
        super().__init__(row, col, self._board, symbol)

    def take_turn(self) -> None:
        """ This method generates randomly a row and a column,
         a new location to move to, checks if there is no Pawn
         at this new location, if not this RandomPawn moves there,
         otherwise it prints a message and does not move there. """
        super().take_turn()
        print("I am R and I am at (", self.get_row(), ", ", self.get_col(), ").")
        new_row: int = random.randint(0, self._board.get_num_rows()-1)
        new_col: int = random.randint(0, self._board.get_num_cols()-1)
        if not self._board.pawn_at(new_row, new_col):
            self.move_to(new_row, new_col)
            print("Moving to (", new_row, ", ", new_col, ").")
        else:
            print("Can't move, (", new_row, ", ", new_col, ") is blocked.")
