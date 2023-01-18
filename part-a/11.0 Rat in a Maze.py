# Question: https://takeuforward.org/data-structure/rat-in-a-maze/

# longer than i want it to be

from copy import deepcopy

def convert(solutions):
    ans = []
    for path in solutions:
        x = [[1 if (j, i) in path else 0 for i in range(n)] for j in range(n)]
        ans.append([el for row in x for el in row])
    return ans

def next_paths(maze, n , row, col, sol):
    paths = {(row-1 if row > 0 else row, col),
    (row, col-1 if col > 0 else col),
    (row, col+1 if col < n-1 else col),
    (row+1 if row < n-1 else row, col)}
    return [p for p in paths if p != (row, col) and maze[p[0]][p[1]] and p not in sol]

def find_paths(maze, n, row, col, sol, ans):
    if row == n-1 and col == n-1:
        ans.append(deepcopy(sol))
        return
    next = next_paths(maze, n, row, col, sol)
    prev = (row, col)
    for path in next:
        sol.append(path)
        find_paths(maze, n, path[0], path[1], sol, ans)
        sol.pop()

def ratInAMaze(maze, n):
    answer = []
    find_paths(maze, n, 0, 0, [(0, 0)], answer)
    for sol in convert(answer):
        print(" ".join(list(map(str, sol))))
