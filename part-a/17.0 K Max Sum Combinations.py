# Question: https://www.codingninjas.com/codestudio/problems/k-max-sum-combinations_975322
# submission doesn't work. platform problem.

import heapq

def kMaxSumCombination(a, b, n, k):
    a_k_largest = a[0:k]
    b_k_largest = b[0:k]
    heapq.heapify(a_k_largest)
    heapq.heapify(b_k_largest)
    #print(f"k: {k}, len(a_k_largest): {len(a_k_largest)}, a_k_largest: {a_k_largest}")
    for i in range(k, n):
        heapq.heappush(a_k_largest, a[i])
        heapq.heappop(a_k_largest)
        heapq.heappush(b_k_largest, b[i])
        heapq.heappop(b_k_largest)
    a_max, b_max = max(a_k_largest), max(b_k_largest)
    a_k_plus_b_max = [a_k_largest[i]+b_max for i in range(k)]
    b_k_plus_a_max = [b_k_largest[i]+a_max for i in range(k)]
    for i in range(k):
        if b_k_plus_a_max[i] not in a_k_plus_b_max:
            heapq.heappush(a_k_plus_b_max, b_k_plus_a_max[i])
            heapq.heappop(a_k_plus_b_max)
    return sorted(a_k_plus_b_max, reverse=True)

#n = 3
#k = 2
#a = [1,3,5]
#b = [6,4,2]
#n, k, a, b=1,1,[3],[4]
n, k, a, b=8,8,[9,15,20,20,11,0,18,7],[16,5,3,16,13,17,7,7]
#8 8
#11 4 11 1 17 2 12 7
#17 16 18 4 15 13 1 7
print(kMaxSumCombination(a, b, n, k))
