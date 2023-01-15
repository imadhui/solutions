# Question: https://leetcode.com/problems/subsets-ii/

def get_all_subsets(i, subset, arr, length, ans):
    if(i == length):
        s = " ".join(list(map(str, subset)))
        if (s not in ans):
            ans[s] = subset
    else:
        get_all_subsets(i+1, subset+[arr[i]], arr, length, ans)
        get_all_subsets(i+1, subset, arr, length, ans)

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer = {}
        get_all_subsets(0, [], nums, len(nums), answer)
        return list(answer.values())
