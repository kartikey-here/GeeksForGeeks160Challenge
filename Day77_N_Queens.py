#The n-queens puzzle is the problem of placing n queens on a (n × n) chessboard such that no two queens can attack each other. Note that two queens attack each other if they are placed on the same row, the same column, or the same diagonal.

#Given an integer n, find all distinct solutions to the n-queens puzzle.
#You can return your answer in any order but each solution should represent a distinct board configuration of the queen placements, where the solutions are represented as permutations of [1, 2, 3, ..., n]. In this representation, the number in the ith position denotes the row in which the queen is placed in the ith column.
#For eg. below figure represents a chessboard [3 1 4 2].

#User function Template for python3

class Solution:
    def nQueen(self, n):
        
        
        def isSafe(board, n, r, c):
            dupRow = r
            dupCol = c

            while (r >= 0 and c >= 0):
                # print(r, c, "1")
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1

            r = dupRow
            c = dupCol

            while (c >= 0):
                # print(r, c, "2")

                if board[r][c] == 'Q':
                    return False
                c -= 1

            r = dupRow
            c = dupCol
            while (r < n and c >= 0):
                # print(r, c, "3")

                if board[r][c] == 'Q':
                    return False
                r += 1
                c -= 1

            return True

        def recursion(ans, n, board, col):

            if col == n:
                dupBoard = [0 for i in range(n)]
                for i in range(n):
                    for j in range(n):
                        if board[i][j]=='Q':
                            dupBoard[j]=i+1

                ans.append(dupBoard)
                return


            for row in range(n):
                if isSafe(board, n, row, col):
                    # print(row, col)
                    board[row][col] = 'Q'
                    recursion(ans, n, board, col+1)
                    board[row][col] = '.'

            return

 

        ans = []

        # s=""
        # for i in range(n):
        #     s+='.'

        board = [['.' for i in range(n)] for j in range(n)]
        recursion(ans, n, board, 0)
        return ans
        # code here
