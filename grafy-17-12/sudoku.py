def is_valid(board, row, col, num):
    # Sprawdź wiersz
    for x in range(9):
        if board[row][x] == num:
            return False

    # Sprawdź kolumnę
    for x in range(9):
        if board[x][col] == num:
            return False

    # Sprawdź kwadrat
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
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

def divide_into_squares(board):
    squares = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = []
            for x in range(3):
                for y in range(3):
                    square.append(board[i+x][j+y])
            squares.append(square)
    return squares

# Przykładowa plansza Sudoku
board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

if solve_sudoku(board):
    print("Rozwiązanie Sudoku:")
    for i in range(9):
        print(board[i])
else:
    print("Brak rozwiązania")

squares = divide_into_squares(board)
print("\nPodział na kwadraty 3x3:")
for i, square in enumerate(squares):
    print(f"Kwadrat {i+1}: {square}")
