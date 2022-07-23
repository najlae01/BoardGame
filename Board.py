from typing import Dict, Tuple
"""
@file                 : Board.py
@author               : NAJLAE
@time                 : 2022-24-4 17:00:00
@email                : abarghachenajlae@gmail.com
"""

class Board():
    """Represent a game board for the game.

       Public methods: __init__, get_num_rows, get_num_cols,
       add_pawn, delete_pawn, take_turn, pawn_at, __str__
    """

    # Annotate fields
    _rows: int          # The number of rows 
    _cols: int          # The number of columns
    _pawns: Dict[Tuple, "Pawn"]

    def __init__(self, rows: int, cols: int) -> None:
        """Initialize rows and cols to values passed and
           create an empty dict for pawns."""
        self._rows = rows
        self._cols = cols
        self._pawns = {}

    def get_num_rows(self) -> int:
        """Return the number of rows (int)."""
        return self._rows

    def get_num_cols(self) -> int:
        """Return the number of columns (int)."""
        return self._cols
    
    def add_pawn(self, pawn: "Pawn", row: int, col: int) -> bool:
        """Return True and add the pawn if there isn't already a pawn there
           and (row,col) is within bounds."""
        result = False
        if row < self._rows and row >= 0 and col < self._cols and col >= 0:
            if not (row, col) in self._pawns:
                self._pawns[(row, col)] = pawn
                result = True
        return result

    def delete_pawn(self, pawn: "Pawn", row: int, col: int) -> None:
        """Remove the pawn from the board."""
        if (row, col) in self._pawns:
            del self._pawns[(row, col)]

    def take_turn(self) -> None:
        """Allow each pawn to take a turn."""
        safe_pawns = self._pawns.copy()
        for pawn in safe_pawns:
            safe_pawns[pawn].take_turn()

    def pawn_at(self, row: int, col: int) -> bool:
        """Return True if there is a pawn at row, col."""
        return (row, col) in self._pawns

    def __str__(self) -> str:
        """Return a string version of the board."""
        result = " |0|1|2|3|4|5|6|7|8|9|\n"
        count = 0
        for row in range(self._rows):
            result += str(count) + "|"
            for col in range(self._cols):
                if (row, col) in self._pawns:
                    result += str(self._pawns[(row, col)]) + "|"
                else:
                    result += " |"
            result += "\n"
            count += 1
        return result
