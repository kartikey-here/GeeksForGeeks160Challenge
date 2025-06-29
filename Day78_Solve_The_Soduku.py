#Given an incomplete Sudoku configuration in terms of a 9x9  2-D interger square matrix, mat[][], the task is to solve the Sudoku. It is guaranteed that the input Sudoku will have exactly one solution.

#A sudoku solution must satisfy all of the following rules:

#Each of the digits 1-9 must occur exactly once in each row.
#Each of the digits 1-9 must occur exactly once in each column.
#Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
#Note: Zeros represent blanks to be filled with numbers 1-9, while non-zero cells are fixed and cannot be changed.\\

class Solution:
    
    # Function to check if a value can be placed at (row, col)
    def isPossible(self, grid, row, col, val):
        for i in range(9):
            if grid[row][i] == val:  # Check row
                return False
            if grid[i][col] == val:  # Check column
                return False
        
        # Check 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == val:
                    return False
        
        return True
    
    # Recursive helper function to solve the Sudoku
    def solveSudokuHelper(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:  # Empty cell found
                    for num in range(1, 10):
                        if self.isPossible(grid, i, j, num):
                            grid[i][j] = num
                            if self.solveSudokuHelper(grid):  # Recursive call
                                return True
                            grid[i][j] = 0  # Backtrack
                    return False  # No valid number found, trigger backtracking
        return True  # Sudoku is solved
    
    # Function to solve the Sudoku
    def solveSudoku(self, mat):
        return self.solveSudokuHelper(mat)
    
    # Function to print the solved Sudoku grid
    def printGrid(self, grid):
        for i in range(9):
            for j in range(9):
                print(grid[i][j], end=" ")
        print()
