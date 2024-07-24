from pprint import pprint
from typing import List


class PrefixSums:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        #724. Find Pivot Index

        Given an array of integers nums, calculate the pivot index of this array.

        The pivot index is the index where the sum of all the numbers strictly to the left of
        the index is equal to the sum of all the numbers strictly to the index's right.

        If the index is on the left edge of the array, then the left sum is 0 because there are no
        elements to the left. This also applies to the right edge of the array.

        Return the leftmost pivot index. If no such index exists, return -1.

        Example 1:
        Input: nums = [1,7,3,6,5,6]
        Output: 3

        Explanation:
        The pivot index is 3.
        Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
        Right sum = nums[4] + nums[5] = 5 + 6 = 11
        """
        n = len(nums)
        right_sum = [0] * n

        # Backwards
        curr = 0
        for i in range(n - 1, -1, -1):
            right_sum[i] = curr
            curr += nums[i]

        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == right_sum[i]:
                return i

            left_sum += num

        return -1

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        #238. Product of Array Except Self
        """
        n, left, right = len(nums), 1, 1
        result = [1] * n

        for i, num in enumerate(nums):
            result[i] = left
            left *= num

        for i in range(n - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result

    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        #560. Subarray Sum Equals K

        Given an array of integers nums and an integer k, return the
        total number of subarrays whose sum equals to k.

        A subarray is a contiguous non-empty sequence of elements within an array.

        Example 1:
        Input: nums = [1,1,1], k = 2
        Output: 2
        """
        # prefix_sum = []
        # curr_sum = 0

        # # O(n) - sum from 0 -> index
        # for num in nums:
        #     curr_sum += num
        #     prefix_sum.append(curr_sum)

        # result = 0

        # # Get all subarrays -> O(n^2) since runtime would be (n)(n+1)/2 -> n^2
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i, n):
        #         # First case is always the individual element (hence i == j)
        #         if i == j:
        #             sub_sum = nums[i]
        #         else:
        #             left_sum = prefix_sum[i - 1] if i > 0 else 0
        #             sub_sum = prefix_sum[j] - left_sum

        #         if sub_sum == k:
        #             result += 1

        # return result

        # O(n) solution without iterating over all subarrays
        prefix_sums = { 0: 1 }

        """
        O(n) to calculate # of subarrays that sum up to k

        We know that Sum(i, j) = Sum(0, j) - Sum(0, i) = Sum[:j] - Sum[:i] = Sum[i, j]
        If Sum[i, j] == k, ie, sum of subarray is equal to k, then:
        Sum[:j] - Sum[:i] = k -> Sum[:i] = Sum[:j] - k

        In our case, since we're interested in previous sums, we want to find if
        Sum[:j] - k exists in the dictionary
        """
        result, curr_sum = 0, 0
        for num in nums:
            curr_sum += num
            target = curr_sum - k

            if target in prefix_sums:
                result += prefix_sums[target]

            if curr_sum in prefix_sums:
                prefix_sums[curr_sum] += 1
            else:
                prefix_sums[curr_sum] = 1

        return result

class NumArray:
    """
    #303. Range Sum Query - Immutable

    Given an integer array nums, handle multiple queries of the following type:

    Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

    Example 1:
    Input
    [-2, 0, 3, -5, 2, -1]

    [0, 2] -> 1
    [2, 5] -> -1
    [0, 5] -> -3
    """
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        range_sum = 0

        while left <= right:
            curr = self.nums[left]
            range_sum += curr
            left += 1

        return range_sum


class NumArray_2:
    """
    Above, but faster solution by calculating and storing the prefix sum
    """
    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            self.prefix_sum.append(curr_sum)

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix_sum[right]
        left_sum = self.prefix_sum[left  - 1] if left > 0 else 0

        return right_sum - left_sum


class NumMatrix:
    """
    #304. Range Sum Query 2D - Immutable

    Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

    You must design an algorithm where sumRegion works on O(1) time complexity.
    """
    def __init__(self, matrix: List[List[int]]):
        # O(m*n) to create 2D prefix sum
        # Prefix sum is n + 1 by m + 1 to provide padding
        # prefix_sum[i][j] represents sum from (0, 0) to (i-1, j-1)
        n, m = len(matrix[0]), len(matrix)
        self.prefix_sum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                curr = matrix[i][j]
                # Add top sum - since prefix[i][j] = (i-1, j-1) -> then prefix[i][j+1] = sum from (0, 0) to (i-1, j)
                curr += self.prefix_sum[i][j + 1]
                # Add left sum - since prefix[i][j] = (i-1, j-1) -> then prefix[i+1][j] = sum from (0, 0) to (i, j-1)
                curr += self.prefix_sum[i+1][j]
                # Subtract the overlapping region that we added twice -> prefix[i][j] = sum from (0, 0) to (i-1,j-1)
                curr -= self.prefix_sum[i][j]

                self.prefix_sum[i + 1][j + 1] = curr

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region_sum = self.prefix_sum[row2 + 1][col2 + 1]
        # Minus top sum - since prefix[i][j] = (i-1,j-1) -> then prefix[]
        region_sum -= self.prefix_sum[row1][col2 + 1]
        # Minus left sum
        region_sum -= self.prefix_sum[row2 + 1][col1]
        # Add back overlapping region that we subtracted twice
        region_sum += self.prefix_sum[row1][col1]

        return region_sum


class TwoPointers:
    def isPalindrome(self, s: str) -> bool:
        """
        #150. Valid Palindrome
        """
        processed_string = []
        for letter in s:
            if letter.isalnum():
                processed_string.append(letter.lower())

        start, end = 0, len(processed_string) - 1
        while start < end:
            if processed_string[start] != processed_string[end]:
                return False

            start += 1
            end -= 1

        return True

    def twoSumWithSortedInput(self, numbers: List[int], target: int) -> List[int]:
        """
        #167. Two Sum II - Input Array Is Sorted
        """
        start, end = 0, len(numbers) - 1

        # Guaranteed that two of the same element (same index) cannot be the solution
        while start < end:
            current = numbers[start] + numbers[end]
            if current == target:
                return [start + 1, end + 1]
            elif current < target:
                start += 1
            else:
                end -= 1

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        #26. Remove Duplicates from Sorted Array
        """
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[count] = nums[i]
                count += 1
        return count

    def removeDuplicates_2(self, nums: List[int]) -> int:
        """
        #80. Remove Duplicates from Sorted Array II

        Given an integer array nums sorted in non-decreasing order, remove some
        duplicates in-place such that each unique element appears at most twice.
        The relative order of the elements should be kept the same.

        Example 1:
        Input: nums = [1,1,1,2,2,3]
        Output: 5, nums = [1,1,2,2,3,_]
        Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
        It does not matter what you leave beyond the returned k (hence they are underscores).
        """
        # Condition is always true if n <= 2
        if len(nums) <= 2:
            return len(nums)

        # Start j at 2, doesn't matter what nums[0] and nums[1] are - condition is always true
        j = 2

        for i in range(2, len(nums)):
            # Using two pointers, j is our counter -> thus, if current element (nums[i]) isn't the same
            # as j - 2, then we can set it. This satisfies our condition of two duplicates -> j - 2 == j - 1 != j
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1

        return j

    def maxArea(self, height: List[int]) -> int:
        """
        #11. Container With Most Water
        """
        max_water = 0
        start, end = 0, len(height) - 1

        while start < end:
            start_height = height[start]
            end_height = height[end]
            area = min(start_height, end_height)*(end - start)
            max_water = max(max_water, area)

            if start_height < end_height:
                start += 1
            else:
                end -= 1

        return max_water
