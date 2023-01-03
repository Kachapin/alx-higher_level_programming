#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    '''
    Check if it is safe to place a queen at the given position.
    '''
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
    '''
    Recursively solve the N queens problem by placing queens in each column of the current row.
    '''
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
    '''
    Check the number of arguments and read the value of N from the command line. Solve the N queens problem if N is valid.
    '''
    # Check for the correct number of arguments
    if len(sys.argv)
