# Quetsion: https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        length = len(nums)
        arr = [nums[i] for i in range(k)]
        heapq.heapify(arr)
        for i in range(k, length):
            heapq.heappush(arr, nums[i])
            heapq.heappop(arr)
        return arr[0]
