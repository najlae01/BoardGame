#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file                 : pawns.py
@author               : NAJLAE
@time                 : 2022-24-4 17:00:00
@email                : abarghachenajlae@gmail.com
"""

from Board import Board
from RandomPawn import RandomPawn
from LeftRightPawn import LeftRightPawn
from TopBottomPawn import TopBottomPawn


def main():
    """This is the main function of our test program for the Pawn class and its subclasses."""
    board: Board = Board(10, 10)
    pawns: list = [RandomPawn(board), LeftRightPawn(board), TopBottomPawn(board)]
    print(board.__str__())
    stop: str = str(input("Type Q to quit, enter for the next round. "))
    while stop != "Q":
        board.take_turn()
        print(board.__str__())
        stop = str(input("Type Q to quit, enter for the next round. "))


main()
