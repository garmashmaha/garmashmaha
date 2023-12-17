import numpy as np

def is_valid(board, row, col, num):
    """Sprawdź, czy liczba jest ważna dla danego miejsca na planszy."""
    # Sprawdź wiersz
    for x in range(9):
        if board[row][x] == num and x != col:
            return False

    # Sprawdź kolumnę
    for x in range(9):
        if board[x][col] == num and x != row:
            return False

    # Sprawdź kwadrat
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i+start_row][j+start_col] == num and (i+start_row != row or j+start_col != col):
                return False
    return True


def is_valid_board(board):
    """Sprawdź, czy początkowa plansza Sudoku jest prawidłowa."""
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0 and not is_valid(board, i, j, board[i][j]):
                return False
    return True


def solve_sudoku(board):
    """Rozwiąż problem Sudoku za pomocą algorytmu backtracking."""
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


def print_board(board):
    """Wydrukuj planszę Sudoku w ładny sposób."""
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
            if (j+1) % 3 == 0 and j < 8:
                print("|", end=' ')
        print()
        if (i+1) % 3 == 0 and i < 8:
            print("-"*21)

# Twoja plansza Sudoku
board = np.array([[0, 0, 0, 4, 0, 0, 1, 9, 0],
                 [0, 3, 0, 0, 0, 0, 8, 6, 0],
                 [0, 0, 7, 0, 8, 3, 5, 0, 0],
                 [0, 0, 0, 0, 0, 8, 6, 0, 0],
                 [8, 0, 5, 1, 0, 8, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0, 3, 5, 0],
                 [0, 8, 1, 0, 4, 0, 0, 0, 0],
                 [0, 0, 0, 0, 7, 0, 0, 0, 0],
                 [0, 4, 0, 2, 5, 0, 0, 0, 0]])
if is_valid_board(board):
    if solve_sudoku(board):
        print("Rozwiązanie Sudoku:")
        print_board(board)
    else:
        print("Brak rozwiązania")
else:
    print("Początkowa plansza Sudoku jest nieprawidłowa")