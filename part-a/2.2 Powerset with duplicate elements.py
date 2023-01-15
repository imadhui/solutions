# Question: https://leetcode.com/problems/subsets-ii/

# Bit Masking

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return {tuple(nums[i] for i in range(len(nums)+1) if mask & 1<<i) for mask in range(1<<len(nums))}
