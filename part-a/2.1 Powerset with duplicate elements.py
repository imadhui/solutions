# Question: https://leetcode.com/problems/subsets-ii/

# Iterative cascading

import copy

def add_to_subsets(a, arr):
    arr = [[]] if arr == [] else arr
    copy1 = copy.deepcopy(arr)
    copy2 = copy.deepcopy(arr)
    def append_a(subset):
        subset.append(a)
        return subset
    prev = list(map(append_a, copy2))
    return copy1+prev, prev

def cascade(arr):
    prev_el = None
    ans = []
    prev_ans = []
    for element in arr:
        if(prev_el == element):
            ret, prev_ans = add_to_subsets(element, prev_ans)
            ans = ans + prev_ans
        else:
            ret, prev_ans = add_to_subsets(element, ans)
            ans = ret
        prev_el = element
    return ans

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        return cascade(nums)
