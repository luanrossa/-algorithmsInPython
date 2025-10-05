"""
Backtracking Algorithm - N Queens Problem
Author: Luan Rossa

Description:
    Solves the N-Queens problem by placing N queens on an N x N chessboard
    such that no two queens threaten each other.

How it works:
    - Uses backtracking to explore possible queen placements row by row.
    - For each row, attempts to place a queen in every column.
    - Checks if the position is safe (no conflicts in column, upper-left, or upper-right diagonals).
    - If safe, places the queen and recurses to the next row.
    - If a dead end is reached, backtracks by removing the queen and trying the next column.
    - Prints each valid solution when all N queens are successfully placed.

Notes:
    - Recursive approach ensures all solutions are explored efficiently.
    - Board is represented as a 2D list, with 'Q' for queens and '.' for empty spaces.
"""


def print_board(board):
    """
    Helper function to print the chessboard.
    Represents a queen with 'Q' and empty spaces with '.'
    """
    for row in board:
        print(" ".join(row))
    print("\n")


def is_safe(board, row, col, n):
    """
    Check if it is safe to place a queen at position (row, col).
    Rules:
    - No other queen in the same column
    - No other queen in the upper-left diagonal
    - No other queen in the upper-right diagonal
    """

    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, n):
    """
    Recursive function that tries to place queens row by row.
    - If all rows are filled, we found a solution.
    - Otherwise, it tries all columns and backtracks when needed.
    """

    # Base case: all queens are placed
    if row == n:
        print_board(board)
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place queen
            board[row][col] = "Q"

            # Recurse for the next row
            solve_nqueens(board, row + 1, n)

            # If no solution, remove the queen (backtracking step)
            board[row][col] = "."


def nqueens(n):
    """
    Main function to initialize the board and start solving.
    """
    # Create an empty board (n x n matrix filled with ".")
    board = [["." for _ in range(n)] for _ in range(n)]

    # Start backtracking from the first row
    solve_nqueens(board, 0, n)


# ---------------------------------------------
# Example of usage
# ---------------------------------------------
if __name__ == "__main__":
    n = 4  # You can change this value (e.g., 5, 6, 8...)
    print(f"Solutions for {n}-Queens:\n")
    nqueens(n)
