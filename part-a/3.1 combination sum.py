# Question: https://leetcode.com/problems/combination-sum/

import copy

def get_solutions(arr, index, sum, ds, ans, target):
    if(sum == target):
        ans.append(copy.copy(ds))
        return
    if(index == len(arr) or sum > target):
        return
    ds.append(arr[index])
    get_solutions(arr, index, sum+arr[index], ds, ans, target)
    ds.pop()
    get_solutions(arr, index+1, sum, ds, ans, target)

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        answers = []
        get_solutions(candidates, 0, 0, [], answers, target)
        return answers

x = Solution()
print(x.combinationSum([2,3,5], 8))

