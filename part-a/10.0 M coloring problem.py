# Question: https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1#

# use backtracking template: https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2793/
"""
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
"""

def backtrack(mat, k, clist, n, colors, ans):
    if k == n:
        ans.append("YES")
        return
    if ans != []: return
    neighbouring_colors = [clist[i] for i in range(n) if mat[k][i] == 1 and clist[i] != None]
    valid_colors = [c for c in colors if c not in neighbouring_colors]
    for c in valid_colors:
        clist[k] = c
        backtrack(mat, k+1, clist, n, colors, ans)
        if ans != []: return
        clist[k] = None

def graphColoring(mat,m):
    length, colors = len(mat), list(range(m))
    clist = [None for i in mat]
    answer = []
    backtrack(mat, 0, clist, length, colors, answer)
    return "NO" if answer == [] else "YES"
