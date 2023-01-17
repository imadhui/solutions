# Question: https://leetcode.com/problems/sudoku-solver/

# using deepcopy costs in space AND time!!

import itertools
from copy import copy, deepcopy

def convert(board, row, col, n):
    "return elements in row, col and 3x3 grid"
    x, y = int(row/3)*3, int(col/3)*3
    a = board[x][y:y+3] + board[x+1][y:y+3] + board[x+2][y:y+3]
    rows = [int(x) for x in board[row] if x.isdigit()]
    cols = [int(y[col]) for y in board if y[col].isdigit()]
    grid = [int(g) for g in a if g.isdigit()]
    return rows, cols, grid
    
def next_pos(row, col, n):
    return (row, col+1) if col < n-1 else (row+1, 0)

def find_solution(board, row, col, n, ans):
    if row >= n: 
        ans.append(board)
        return
    next_row, next_col = next_pos(row, col, n)
    if board[row][col] != ".":
        find_solution(board, next_row, next_col, n, ans)
        return
    rows, cols, grid = convert(board, row, col, n)
    space = list(range(1, 10))
    space = [x for x in space if x not in rows+cols+grid]
    if space == []:
        return
    for x in space:
        board[row][col] = str(x)
        find_solution(board, next_row, next_col, n, ans)
        if ans != []: break
        board[row][col] = "."

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        answer = []
        find_solution(board, 0, 0, len(board), answer)
        return
