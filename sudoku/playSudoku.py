from sudoku import SudokuGame
from smallSquare import Square



#inputString = '2,0,0,0,0,0,1,0,0,2,0,0,0,0,0,4'
##inputString = '2,1,4,3,3,4,1,0,0,2,0,0,0,0,2,4'
#gridSize = 2
#
#sudokuGame = SudokuGame( gridSize, inputString )


#--------------------
# |  2  1  |  4  3  |
# |  3  4  |  1  2  |
#--------------------
# |  4  2  |  3  1  |
# |  1  3  |  2  4  |
#--------------------


inputString = '9,0,0,6,4,0,0,0,3,2,7,0,0,9,0,5,8,0,0,1,0,5,8,0,0,0,0,0,9,0,0,0,0,7,0,0,0,0,7,9,6,5,8,0,0,0,0,2,0,0,0,0,4,0,0,0,0,0,5,3,0,6,0,0,5,1,0,7,0,0,2,8,4,0,0,0,1,6,0,0,5'
gridSize = 3

sudokuGame = SudokuGame( gridSize, inputString )

# ---------------------------
# |  9  8  5  |  6  4  7  |  2  1  3  |
# |  2  7  6  |  3  9  1  |  5  8  4  |
# |  3  1  4  |  5  8  2  |  6  9  7  |
# ---------------------------
# |  8  9  3  |  1  2  4  |  7  5  6  |
# |  1  4  7  |  9  6  5  |  8  3  2  |
# |  5  6  2  |  7  3  8  |  1  4  9  |
# ---------------------------
# |  7  2  9  |  8  5  3  |  4  6  1  |
# |  6  5  1  |  4  7  9  |  3  2  8  |
# |  4  3  8  |  2  1  6  |  9  7  5  |
# ---------------------------




