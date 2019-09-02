import operator as op
from functools import reduce
import numpy

#At every level of the tree there will be two options,
#K nodes can go in left subtree and others in right subtree
#One node will be left out as root so n-1-k can be in right subtree
#We can select this k node in left subtree in (n-1)Ck ways
#For each of this ways, no of subtree is (n - 1)Ck * dp[k] * dp[n - 1 - k] ways.
#This problem satisfies overlapping subproblem property
#Hence can be solved using DP.

MOD = 10 ** 9 + 7
def ncr(n, r):
        r = min(r, n-r)
        numer = reduce(op.mul, range(n, n-r, -1), 1)
        denom = reduce(op.mul, range(1, r+1), 1)
        return numer / denom

class Solution:
    # @param A : integer
    # @return an integer
    
    
    def solve(self, A):
        dp = []
        dp.append(0);
        dp.append(1);
        dp.append(1);
        dp.append(2);
        if A < 4 :
            return dp[A]
        for i in range(4, A + 1):
            maxi = - numpy.inf
            for j in range (1, i - 1) :
                maxi = max(maxi, ncr(i - 1, j) * dp[j] * dp[i - 1 - j])
            dp.append(maxi)
        return dp[A] % MOD
