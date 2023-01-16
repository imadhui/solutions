# Question: https://leetcode.com/problems/combination-sum-ii/
# Video Solution: https://www.youtube.com/watch?v=G1fRTGRxXU8&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=50

import copy

def get_solutions(arr, index, sum, ds, ans, target):
    if(sum == target):
        ans.append(copy.copy(ds))
        return
    if(index == len(arr) or sum > target):
        return
    for i in range(index, len(arr)):
        if(i > index and arr[i] == arr[i-1]):
            continue
        ds.append(arr[i])
        get_solutions(arr, i+1, sum+arr[i], ds, ans, target)
        ds.pop()

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        answers = []
        candidates.sort()
        get_solutions(candidates, 0, 0, [], answers, target)
        return list(answers)
