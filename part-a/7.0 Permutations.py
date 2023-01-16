# Question: https://leetcode.com/problems/permutations/

# ok , but worse than python's **permutations** from itertools

from copy import copy

def get_all_permutations(nums, ds, ans):
    if(nums == []):
        ans.append(copy(ds))
        return
    for i in range(len(nums)):
        ds.append(nums[i])
        get_all_permutations(nums[:i]+nums[i+1:], ds, ans)
        ds.pop()

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        answers = []
        get_all_permutations(nums, [], answers)
        return answers
