# Question: https://leetcode.com/problems/permutation-sequence/

# simple, but kind of slow

from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return "".join(map(str, list(permutations(list(range(1, n+1))))[k-1]))
