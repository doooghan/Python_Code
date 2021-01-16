# 执行通过
"""
class Solution:
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
"""

# 执行通过
"""
class Solution:
    memo = list()

    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        Solution.memo = [0 for i in range(n + 1)]
        return self.helper(n)

    def helper(self, n):
        if n == 1 or n == 2:
            return 1

        if Solution.memo[n] != 0:
            return Solution.memo[n]
        Solution.memo[n] = self.helper(n-1) + self.helper(n-2)
        return Solution.memo[n]
"""


class Solution:
    def fib(self, n: int) -> int:
        pass


fib = Solution()
print(fib.fib(20))
