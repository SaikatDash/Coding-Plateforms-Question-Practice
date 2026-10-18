class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        def fib(n):
            if n <= 1:
                return n

            if n in memo:
                return memo[n]

            memo[n] = fib(n - 1) + fib(n - 2)
            return memo[n]

        return fib(n)

