import numpy as np

def is_valid(board, row, col, num):
    # Sprawdź wiersz
    if num in board[row]:
        return False

    # Sprawdź kolumnę
    if num in board[:, col]:
        return False

    # Sprawdź kwadrat
    start_row, start_col = row - row % 3, col - col % 3
    if num in board[start_row:start_row+3, start_col:start_col+3]:
        return False
    return True

def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True

# Przykładowa plansza Sudoku
board = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                  [6, 0, 0, 1, 9, 5, 0, 0, 0],
                  [0, 9, 8, 0, 0, 0, 0, 6, 0],
                  [8, 0, 0, 0, 6, 0, 0, 0, 3],
                  [4, 0, 0, 8, 0, 3, 0, 0, 1],
                  [7, 0, 0, 0, 2, 0, 0, 0, 6],
                  [0, 6, 0, 0, 0, 0, 2, 8, 0],
                  [0, 0, 0, 4, 1, 9, 0, 0, 5],
                  [0, 0, 0, 0, 8, 0, 0, 7, 9]])

if solve_sudoku(board):
    print("Rozwiązanie Sudoku:")
    print(board)
else:
    print("Brak rozwiązania")
