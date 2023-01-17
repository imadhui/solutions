# Question: https://leetcode.com/problems/n-queens/

# Beats 98.22% of the submissions on leetcode!!

from copy import copy

def convert(cols):
    length = len(cols)
    s = "."*length
    arr = []
    for col in cols:
        x = s[:col-1]+"Q"+s[col:]
        arr.append(x)
        s = "."*length
    return arr

def place_queen(n, cur_row, cols, pos, neg, ans):
    for col in range(1, n+1):
        if((cur_row <= n) and (col not in cols) and (cur_row-col not in neg) and (cur_row+col not in pos)):
            cols.append(col)
            pos.append(cur_row+col)
            neg.append(cur_row-col)
            #print(f"cur_row: {cur_row}, cur_col: {col}")
            if(len(cols) == n):
                ans.append(copy(cols))
            place_queen(n, cur_row+1, cols, pos, neg, ans)
            neg.pop()
            pos.pop()
            cols.pop()

class Solution:
    def solveNQueens(self, n):
        answers = []
        place_queen(n, 1, [], [], [], answers)
        return list(map(convert, answers))
