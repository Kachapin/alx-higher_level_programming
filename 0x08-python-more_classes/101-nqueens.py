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
    Read the value of N from user input and solve the N queens problem.
    '''
    # Read the value of N from user input
    N = int(input("Enter the value of N: "))
    
    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        return
    
    # Initialize the board with all zeros
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    # Solve the N queens problem
    solve_nqueens(board, 0, N)

if __name__ == '__main__':
    main()
