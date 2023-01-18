# Question: https://leetcode.com/problems/single-element-in-a-sorted-array/description/

# This is my solution. too large for the problem, imo. But the performance is above the median

def limit(i, length):
    if i > length-1:
        return length-1
    elif i < 0:
        return 0
    else:
        return i

def test(i, nums, length):
    if i == 0:
        if (length == 1): return 0
        return 0 if nums[i] != nums[i+1] else 1
    if i == length-1:
        return 0 if nums[i-1] != nums[i] else -1
    if nums[i-1] != nums[i] and nums[i] != nums[i+1]: return 0
    if i%2 == 0:
        return 1 if  nums[i] == nums[i+1] else -1
    else:
        return 1 if nums[i-1] == nums[i] else -1

def b_search(guess, ll, ul, nums, length):
    res = test(guess, nums, length)
    if res == 0:
        return guess
    elif res == 1:
        ll = guess
        return b_search(limit(guess*2, length) if guess != 0 else 1, ll, ul, nums, length)
    elif res == -1:
        ul = guess
        return b_search(ll+int((ul-ll)/2), ll, ul, nums, length)

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        length = len(nums)
        return nums[b_search(0, 0, length-1, nums, length)]
