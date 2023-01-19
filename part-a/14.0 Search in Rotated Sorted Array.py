# Question: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

def test1(i, nums, target):
    if nums[i] == target:
        return 0
    if nums[i] > target:
        return -1
    if nums[i] < target:
        return 1

def test2(i, nums, target):
    if (i == 0):
        return 1
    if nums[i] < nums[i-1]:
        return 0
    if nums[i] < nums[0]:
        return -1
    else:
        return 1

def b_search(i, nums, test, ll, ul, target):
    if ul-ll == 1 or ul == ll:
        a, b = test(ll, nums, target), test(ul, nums, target)
        print(f"i: {i}, ll: {ll}, ul: {ul}, a: {a}, b: {b}")
        if 0 not in (a, b):
            return -1
        else:
            return ll if target == nums[ll] else ul
    res = test(i, nums, target)
    #print(f"i: {i}, ll: {ll}, ul: {ul}, res: {res}")
    if res == 0:
        return i
    elif res == 1:
        ll = i
        return b_search(int((ll+ul)/2), nums, test, ll, ul, target)
    elif res == -1:
        ul = i
        return b_search(int((ll+ul)/2), nums, test, ll, ul, target)

class Solution:
    def search(self, nums, target):
        length = len(nums)
        rot = b_search(0, nums, test2, 0, length-1, target)
        ll = 0
        ul = rot-1 if rot != -1 else length-1
        i = b_search(0, nums, test1, ll, ul, target)
        print(f"i: {i}, ll: {ll}, ul: {ul}, rot: {rot}")
        if i != -1 or rot == -1: return i
        ll = rot
        ul = length-1
        i = b_search(rot, nums, test1, ll, ul, target)
        return i
