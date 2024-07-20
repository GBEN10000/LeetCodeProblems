class Solution(object):
    def fib(self, n):
        if n==0 or n==1:
            return n
        elif n==2 or n==3:
            return n-1
        else:
            return (self.fib(n-1)+self.fib(n-2))
        
