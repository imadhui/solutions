# Question: https://www.codingninjas.com/codestudio/problems/subset-sum_3843086?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
# Video: https://youtu.be/aHyFllZSOIc

def subset_sums(i, sum, arr, len, ans):
    if(i == len):
        ans.append(sum)
    else:
        subset_sums(i+1, sum+arr[i], arr, len, ans)
        subset_sums(i+1, sum, arr, len, ans)

def subsetSum(arr):
    answer = []
    subset_sums(0, 0, arr, len(arr), answer)
    return sorted(answer)
