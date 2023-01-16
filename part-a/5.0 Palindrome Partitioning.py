# Question: https://leetcode.com/problems/palindrome-partitioning/

# Beats 91.5% on leetcode!!

import copy

def is_palindrome(s):
    return s == s[::-1]

def get_partitions(s, ds, ans):
    if(s == ""):
        ans.append(copy.copy(ds))
        return
    for i in range(len(s)):
        if(is_palindrome(s[:i+1])):
            ds.append(s[:i+1])
            get_partitions(s[i+1:], ds, ans)
            ds.pop()

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        answers = []
        get_partitions(s, [], answers)
        return answers
