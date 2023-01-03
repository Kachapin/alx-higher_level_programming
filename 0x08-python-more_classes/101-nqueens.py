#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check for attacks from queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check for attacks from queens in the top-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Check for attacks from queens in the top-right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True

def solve_nqueens(board, row, N):
    # Base case: if all rows have been placed, print the solution
    if row == N:
        for i in range(N):
            for j in range(N):
                print(board[i][j], end=' ')
            print()
        return
    
    # Try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, row+1, N)
            # Backtrack and try a different column
            board[row][col] = 0

def main():
    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # Check if N is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Initialize the board with all zeros
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    # Solve the N queens problem
    solve_nqueens(board, 0, N)

if __name__ == '__main__':
    main()
