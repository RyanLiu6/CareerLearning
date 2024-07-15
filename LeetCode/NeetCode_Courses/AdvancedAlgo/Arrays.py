from typing import List


class PrefixSums:
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
