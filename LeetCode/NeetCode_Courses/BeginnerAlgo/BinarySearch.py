from typing import List


class SearchArray:
    def search(self, nums: List[int], target: int) -> int:
        """
        #704. Binary Search
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            center = (left + right) // 2
            current = nums[center]
            if current == target:
                return center
            elif current < target:
                left = center + 1
            else:
                right = center - 1

        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        #74. Search a 2D Matrix
        """
        def binary_search(nums: List[int], to_find: int):
            left, right = 0, len(nums) - 1

            while left <= right:
                center = (left + right) // 2
                current = nums[center]
                if current == to_find:
                    return True
                elif current < to_find:
                    left = center + 1
                else:
                    right = center - 1

            return False

        # Approach #1: This would be O(m + logn) where m = # rows and n = len(rows)
        # Find the first row where the last element of that row is greater than target
        # This means that target is within this row
        to_search = -1
        for i, row in enumerate(matrix):
            if row[-1] >= target:
                to_search = i
                break

        # If to_search is -1, that means it was never set, thus, no rows where the last
        # element is greater than target -> target does not exist in matrix
        if to_search == -1:
            return False

        return binary_search(matrix[to_search], target)

        # Approach #2: This would be O(logn + logm) = O(log(n * m)) where m = # rows and
        # n = len(rows)
        m, n = len(matrix), len(matrix[0])
        top, bot = 0, m - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if top > bot:
            return False

        row = (top + bot) // 2

        return binary_search(matrix[row], target)


class SearchRange:
    def guess(num: int) -> int:
        """
        Part of #374
        """
        pass

    def guessNumber(self, n: int) -> int:
        """
        #374. Guess Number Higher or Lower

        We are playing the Guess Game. The game is as follows:

        I pick a number from 1 to n. You have to guess which number I picked.

        Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

        You call a pre-defined API int guess(int num), which returns three possible results:

        -1: Your guess is higher than the number I picked (i.e. num > pick).
        1: Your guess is lower than the number I picked (i.e. num < pick).
        0: your guess is equal to the number I picked (i.e. num == pick).
        Return the number that I picked.
        """
        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2

            result = self.guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1

    def isBadVersion(version: int) -> bool:
        pass

    def firstBadVersion(self, n: int) -> int:
        """
        #278. First Bad Version

        You are a product manager and currently leading a team to develop a new product.
        Unfortunately, the latest version of your product fails the quality check.
        Since each version is developed based on the previous version, all the versions after a bad version are also bad.

        Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

        You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a
        function to find the first bad version. You should minimize the number of calls to the API.
        """
        left, right = 0, n
        first_bad = n

        while left <= right:
            mid = (left + right) // 2
            result = self.isBadVersion(mid)

            if result:
                first_bad = min(first_bad, mid)
                right = mid - 1
            else:
                left = mid + 1

        return first_bad

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        #875. Koko Eating Bananas
        """
        # O(n*log(max of piles)) where n = len(piles)
        k = max(piles)
        left, right = 1, max(piles)
        while left <= right:
            center = (left + right) // 2
            hours = 0
            for num in piles:
                if num % center == 0:
                    hours += num / center
                else:
                    hours += num // center + 1

            if hours <= h:
                k = min(center, k)
                right = center - 1
            else:
                left = center + 1

        return k

