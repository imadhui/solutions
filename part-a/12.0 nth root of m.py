# Question: https://www.codingninjas.com/codestudio/problems/1062679

# see how to format decimal places in python. The answer has to be accurate upto 6 decimal places

def b_search(guess, prev, ll, ul, n, m):
    res = guess**n
    if res == m or abs(prev - guess) < 0.00000001:
        return guess
    elif res > m:
        ul = guess
        return b_search(ll+(ul-ll)/2, guess, ll, ul, n, m)
    else:
        ll = guess
        return b_search(guess*2, guess, ll, ul, n, m)

def findNthRootOfM(n,m):
    return "{0:.6f}".format(b_search(1.000, 0, 1.0, m, n, m))
