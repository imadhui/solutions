# Question at: https://www.codingninjas.com/codestudio/problems/subset-sum_3843086?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

def subsetSum(num: List[int]) -> List[int]:

    n = len(num)
    
    # Ans vector contains all the subset sums.
    ans = []

    for i in range(2 ** n):
    
        sum = 0
        for j in range(n):
        
            # Checking wheather the element is present the subset or not.
            if (2 **  j) & i:
                sum += num[j]
    
        ans.append(sum)
    
    # Sort the vector and finally return it.
    ans.sort()
    return ans
