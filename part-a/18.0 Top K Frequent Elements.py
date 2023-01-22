# Question: https://leetcode.com/problems/top-k-frequent-elements/description/
# Beats about 40% of solutions. So not good enough!

from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        values, counts = zip(*Counter(nums).most_common(k))
        return values
