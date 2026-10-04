class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(x):
            if x<=1:
                return 1
            return x*factorial(x-1)
        
        if m==1 or n==1:
            return 1
        
        if m<n:
            m,n = n,m
        
        return int(factorial(m+n-2)/(factorial(n-1)*factorial(m-1)))