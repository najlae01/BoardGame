#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file                 : LeftRightPawn.py
@author               : NAJLAE
@time                 : 2022-24-4 17:00:00
@email                : abarghachenajlae@gmail.com
"""

from Board import Board
from Pawn import Pawn
import random


class LeftRightPawn(Pawn):
    """Represent a LeftRightPawn in the Board (a subclass a Pawn).

       Public methods: __init__, take_turn
    """
    # Annotate fields
    __left_boundary: bool  # determines whether if the LeftRightPawn reached the left boundary or not
    __right_boundary: bool  # determines whether if the LeftRightPawn reached the right boundary or not

    def __init__(self, board: Board) -> None:
        """ This method generates randomly a row and a column
        to start with, this Pawn's symbol is L.
        This constructor calls the superclass Pawn's constructor
        to create this new LeftRightPawn object."""
        self._board = board
        self.__left_boundary = True
        self.__right_boundary = False
        row = random.randint(0, self._board.get_num_rows()-1)
        col = random.randint(0, self._board.get_num_cols()-1)
        symbol = "L"
        super().__init__(row, col, self._board, symbol)

    def take_turn(self) -> None:
        """ This method moves this LeftRightPawn if there is
         no Pawn at this new location from left to right until
         it reaches the board's right boundary then it starts
         moving from right to left until it reaches the board's
         left boundary to start again moving from left to right.
         If there is already a Pawn there, it prints a message
         and does not move there. """
        super().take_turn()
        row: int = self.get_row()
        col: int = self.get_col()
        print("I am L and I am at (", row, ", ", col, ").")
        if col == 0:
            self.__left_boundary = True
            self.__right_boundary = False
        if col == self._board.get_num_cols() - 1:
            self.__left_boundary = False
            self.__right_boundary = True
        if self.__right_boundary:
            new_col: int = col - 1
            if new_col < self._board.get_num_cols():
                if not self._board.pawn_at(row, new_col):
                    self.move_to(row, new_col)
                    print("Moving to (", row, ", ", new_col, ").")
                else:
                    print("Can't move, (", row, ", ", new_col, ") is blocked.")
        if self.__left_boundary:
            new_col: int = col + 1
            if not self._board.pawn_at(row, new_col):
                self.move_to(row, new_col)
                print("Moving to (", row, ", ", new_col, ").")
            else:
                print("Can't move, (", row, ", ", new_col, ") is blocked.")
