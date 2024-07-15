from collections import defaultdict
from typing import List


class Solutions:
    def search(self, nums: List[int], target: int) -> int:
        """
        #704. Binary Search
        Given an array of integers nums which is sorted in ascending order, and an integer target,
        write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

        You must write an algorithm with O(log n) runtime complexity.

        Example 1:
        Input: nums = [-1,0,3,5,9,12], target = 9
        Output: 4
        Explanation: 9 exists in nums and its index is 4

        Example 2:
        Input: nums = [-1,0,3,5,9,12], target = 2
        Output: -1
        Explanation: 2 does not exist in nums so return -1
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

        You are given an m x n integer matrix matrix with the following two properties:

        Each row is sorted in non-decreasing order.
        The first integer of each row is greater than the last integer of the previous row.
        Given an integer target, return true if target is in matrix or false otherwise.

        You must write a solution in O(log(m * n)) time complexity.

        O(log(m * n)) = O(logm + logn)

        Example 1:
        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
        Output: true

        Example 2:
        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
        Output: false
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

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        #875. Koko Eating Bananas

        Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
        The guards have gone and will come back in h hours.

        Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas
        and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead
        and will not eat any more bananas during this hour.

        Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
        Return the minimum integer k such that she can eat all the bananas within h hours.

        Example 1:
        Input: piles = [3,6,7,11], h = 8
        Output: 4

        Example 2:
        Input: piles = [30,11,23,4,20], h = 5
        Output: 30

        Example 3:
        Input: piles = [30,11,23,4,20], h = 6
        Output: 23
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

    def findMin(self, nums: List[int]) -> int:
        """
        #153. Find Minimum in Rotated Sorted Array

        Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
        For example, the array nums = [0,1,2,4,5,6,7] might become:

        [4,5,6,7,0,1,2] if it was rotated 4 times.
        [0,1,2,4,5,6,7] if it was rotated 7 times.

        Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array
        [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

        Given the sorted rotated array nums of unique elements, return the minimum element of this array.

        You must write an algorithm that runs in O(log n) time.

        Example 1:
        Input: nums = [3,4,5,1,2]
        Output: 1
        Explanation: The original array was [1,2,3,4,5] rotated 3 times.

        Example 2:
        Input: nums = [4,5,6,7,0,1,2]
        Output: 0
        Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

        Example 3:
        Input: nums = [11,13,15,17]
        Output: 11
        Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
        """
        # result = nums[0]
        # left, right = 0, len(nums) - 1

        # while left <= right:
        #     # If nums[left] < nums[right], then we're in a sorted array, so we return
        #     # the minimum of this current section (left) and the stored minimum
        #     if nums[left] < nums[right]:
        #         result = min(result, nums[left])
        #         break

        #     # Else we binary search
        #     center = (left + right) // 2
        #     M = nums[center]
        #     result = min(result, M)

        #     # If nums[center] >= nums[left], then left -> center is one sorted section,
        #     # So we should search the right side (given our knowledge of rotations)
        #     # Else (nums[center] < nums[left]), then we should search the left side because
        #     # all numbers to the right will only be incrementing
        #     if M >= nums[left]:
        #         left = center + 1
        #     else:
        #         right = center - 1

        # return result

        # Cleaner solution
        left, right = 0, len(nums) - 1

        # We use < instead of <= because we want to break when left == right
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # If nums[mid] > nums[right] then pivot must be to the right
                # We don't consider nums[mid] to be the minimum because it was
                # greater than at least one other number (nums[right]) in this case
                left = mid + 1
            else:
                # We need to search the left side since there may be smaller numbers to the left
                # However we do consider mid in this case as it can be the minimum!
                right = mid

        # When the while loop terminates, left should equal right
        return nums[left]

    def findMin_2(self, nums: List[int]) -> int:
        """
        #154. Find Minimum in Rotated Sorted Array II

        This is 153, but the restriction of distinct and unique elements is no longer true.
        """
        left, right = 0, len(nums) - 1

        # We use < instead of <= because we want to break when left == right
        while left < right:
            mid = (left + right) // 2
            R, M = nums[right], nums[mid]

            if M > R:
                # If nums[mid] > nums[right] then pivot must be to the right
                # We don't consider nums[mid] to be the minimum because it was
                # greater than at least one other number (nums[right]) in this case
                left = mid + 1
            elif M < R:
                # We need to search the left side since there may be smaller numbers to the left
                # However we do consider mid in this case as it can be the minimum!
                right = mid
            else:
                # When nums[mid] == nums[right]
                # Checking for the first minimum
                if (nums[right] < nums[right - 1]):
                    left = right
                    break
                right -= 1

        # When the while loop terminates, left should equal right
        return nums[left]

    def search(self, nums: List[int], target: int) -> int:
        """
        #33. Search in Rotated Sorted Array

        There is an integer array nums sorted in ascending order (with distinct values).

        Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k
        (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1],
        nums[0], nums[1], ..., nums[k-1]] (0-indexed).

        For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

        Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

        You must write an algorithm with O(log n) runtime complexity.

        Example 1:
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4

        Example 2:
        Input: nums = [4,5,6,7,0,1,2], target = 3
        Output: -1

        Example 3:
        Input: nums = [1], target = 0
        Output: -1
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            L, R, M = nums[left], nums[right], nums[mid]

            if M == target:
                return mid

            # Check if L -> M is sorted
            if L <= M:
                # L -> M is ascending only
                if target > M or target < L:
                    left = mid + 1
                else:
                    # L < target < M
                    right = mid - 1
            else:
                # Rotated array
                if target < M or target > R:
                    # Since we know nothing about the array here, we must rely on M and R
                    # If target > R, based on rotation it must be on left side
                    # IF target < M, based on ascending it must be on left side
                    right = mid - 1
                else:
                    # If target > M and target < R then it must be on the right side
                    left = mid + 1

        return -1

    def search_2(self, nums: List[int], target: int) -> bool:
        """
        #81. Search in Rotated Sorted Array II

        This is 33, but the restriction of distinct and unique elements is no longer true.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            L, R, M = nums[left], nums[right], nums[mid]

            if M == target:
                return True

            # Dealing with duplicates
            if L == M and R == M:
                left += 1
                right -= 1
            elif L <= M:
                # L -> M is ascending only
                if target > M or target < L:
                    left = mid + 1
                else:
                    # L < target < M
                    right = mid - 1
            else:
                # Rotated
                if target < M or target > R:
                    # If target > R, based on rotation it must be on left side
                    # IF target < M, based on ascending it must be on left side
                    right = mid - 1
                else:
                    # If target > M and target < R then it must be on the right side
                    left = mid + 1
        return False


class TimeMap:
    def __init__(self):
        self.key_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_store:
            return ""

        # values should be already sorted, given that timestamp is always increasing
        values = self.key_store[key]
        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            value = values[mid][1]
            if value <= timestamp:
                # If value <= timestamp, we can try bigger timestamps
                # Since we want the closest timestamp
                left = mid + 1
            else:
                # If value > timestamp, we need to try smaller timestamps
                right = mid - 1

        # At this point left > right
        # If right == -1, that means that we kept on trying smaller timestamps
        # until we ran out -> no timestamp that works for our restraints
        if right == -1:
            return ""

        # We use right as index here, given that left should be right + 1
        return values[right][0]
