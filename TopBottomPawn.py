#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file                 : TopBottomPawn.py
@author               : NAJLAE
@time                 : 2022-24-4 17:00:00
@email                : abarghachenajlae@gmail.com
"""
from Board import Board
from Pawn import Pawn
import random


class TopBottomPawn(Pawn):
    """Represent a TopBottomPawn in the Board (a subclass a Pawn).

       Public methods: __init__, take_turn
    """
    # Annotate fields
    __top_boundary: bool  # determines whether if the TopBottomPawn reached the top boundary or not
    __bottom_boundary: bool  # determines whether if the TopBottomPawn reached the bottom boundary or not

    def __init__(self, board: Board) -> None:
        """ This method generates randomly a row and a column
        to start with, this Pawn's symbol is T.
        This constructor calls the superclass Pawn's constructor
        to create this new TopBottomPawn object."""
        self._board = board
        self.__top_boundary = True
        self.__bottom_boundary = False
        row = random.randint(0, self._board.get_num_rows()-1)
        col = random.randint(0, self._board.get_num_cols()-1)
        symbol = "T"
        super().__init__(row, col, self._board, symbol)

    def take_turn(self) -> None:
        """ This method moves this LeftRightPawn if there is
         no Pawn at this new location from top to bottom until
         it reaches the board's bottom boundary then it starts
         moving from bottom to top until it reaches the board's
         top boundary to start again moving from top to bottom.
         If there is already a Pawn there, it prints a message
         and does not move there. """
        super().take_turn()
        row: int = self.get_row()
        col: int = self.get_col()
        print("I am T and I am at (", row, ", ", col, ").")
        if row == 0:
            self.__top_boundary = True
            self.__bottom_boundary = False
        if row == self._board.get_num_rows() - 1:
            self.__top_boundary = False
            self.__bottom_boundary = True
        if self.__bottom_boundary:
            new_row: int = row - 1
            if new_row < self._board.get_num_rows():
                if not self._board.pawn_at(new_row, col):
                    self.move_to(new_row, col)
                    print("Moving to (", new_row, ", ", col, ").")
                else:
                    print("Can't move, (", new_row, ", ", col, ") is blocked.")
        if self.__top_boundary:
            new_row: int = row + 1
            if not self._board.pawn_at(new_row, col):
                self.move_to(new_row, col)
                print("Moving to (", new_row, ", ", col, ").")
            else:
                print("Can't move, (", new_row, ", ", col, ") is blocked.")


