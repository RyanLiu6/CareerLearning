class Solution:
    def fib(self, n: int) -> int:
        """
        #509
        """
        def _recursive(n: int) -> int:
            if n < 2:
                return n
            else:
                return _recursive(n - 1) + _recursive(n - 2)
        return _recursive(n)

        cache = { 0: 0, 1: 1 }
        def _iterative_with_cache(n: int) -> int:
            for i in range(2, n + 1):
                cache[i] = cache[i - 1] + cache[i - 2]
            return cache[n]
        return _iterative_with_cache(n)

        cache = { 0: 0, 1: 1 }
        def _recursive_with_cache(n: int) -> int:
            if n not in cache:
                cache[n] = _recursive_with_cache(n - 1) + _recursive_with_cache(n - 2)
            return cache[n]
        return _recursive_with_cache(n)


    def climb_stairs(self, n: int) -> int:
        """
        #70
        You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.
        In how many distinct ways can you climb to the top?

        Example 1:
        Input: n = 2
        Output: 2
        Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps
        """
        def _recursive(n: int) -> int:
            if n > 0 and n <= 2:
                return n
            return _recursive(n - 1) + _recursive(n - 2)
        return _recursive(n)

        cache = { 1: 1, 2: 2}
        def _recursive_with_cache(n: int) -> int:
            if n not in cache:
                cache[n] = _recursive_with_cache(n - 1) + _recursive_with_cache(n - 2)
            return cache[n]
        return _recursive_with_cache(n)
