# 执行不通过,递归太深
"""
class Solution:
    def fib(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
"""


class Solution:
    def fib(self, n: int) -> int:
        pass


fib = Solution()
print(fib.fib(20))
