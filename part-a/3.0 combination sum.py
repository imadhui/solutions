# Question: https://leetcode.com/problems/combination-sum/

# This is a partial solution. only 121/160 work under time limit

from itertools import product

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ranges = []
        length = len(candidates)
        def is_solution(s):
            sum = 0
            [sum := sum + candidates[i]*s[i]  for i in range(length)]
            return target == sum
        for x in candidates:
            ranges = ranges + [[i for i in range(int(target/x)+1)]]
        permutations = product(*ranges)
        def convert(s):
            arr = []
            [arr := arr + [candidates[i]]*s[i] for i in range(len(candidates)) if (candidates[i]*s[i] != 0)]
            return arr
        answers = [convert(p) for p in permutations if is_solution(p)]
        return answers
