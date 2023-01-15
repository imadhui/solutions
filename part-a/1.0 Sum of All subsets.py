# Question at: https://www.codingninjas.com/codestudio/problems/subset-sum_3843086?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

import copy

def add_to_subset(element, subset):
    def append_func(array):
        array.append(element)
        return array
    return list(map(append_func, subset))

def get_all_subsets(array):
    length = len(array)
    if(length == 1 or length == 0):
        return [array]
    if(length == 2):
        return [[array[0]], [array[1]], array]
    else:
        x = get_all_subsets(array[1:])
        y = copy.deepcopy(x)
        x.append([array[0]])
        x = x + add_to_subset(array[0], y)
        return x

def subsetSum(arr):
    x = get_all_subsets(arr)
    x.append([0])
    return sorted(list(map(sum, x)))
