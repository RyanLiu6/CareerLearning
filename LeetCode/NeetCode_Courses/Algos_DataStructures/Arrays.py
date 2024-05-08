from collections import deque
from typing import List


class StaticArrays:
    def remove_duplicates(self, nums: List[int]) -> int:
        """
        #26
        Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
        such that each unique element appears only once. The relative order of the elements should
        be kept the same. Then return the number of unique elements in nums.

        Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
            Change the array nums such that the first k elements of nums contain the unique elements in the order
                they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
            Return k.

        Example 1:
        Input: nums = [1,1,2]
        Output: 2, nums = [1,2,_]
        Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
        It does not matter what you leave beyond the returned k (hence they are underscores).\

        Example 2:
        Input: nums = [0,0,1,1,1,2,2,3,3,4]
        Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
        Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
        It does not matter what you leave beyond the returned k (hence they are underscores).
        """
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[count] = nums[i]
                count += 1
        return count

    def remove_element(self, nums: List[int], val: int) -> int:
        """
        #27
        Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
        The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

        Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
            Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
            The remaining elements of nums are not important as well as the size of nums.
            Return k.

        Example 1:
        Input: nums = [3,2,2,3], val = 3
        Output: 2, nums = [2,2,_,_]
        Explanation: Your function should return k = 2, with the first two elements of nums being 2.
        It does not matter what you leave beyond the returned k (hence they are underscores).
        """
        count = 0
        for num in nums:
            if num != val:
                nums[count] = num
                count += 1
        return count

class DynamicArrays:
    def get_concatenation(self, nums: List[int]) -> List[int]:
        """
        #1929
        Given an integer array nums of length n, you want to create an array ans of length 2n where
        ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

        Specifically, ans is the concatenation of two nums arrays.

        Example 1:
        Input: nums = [1,2,1]
        Output: [1,2,1,1,2,1]
        Explanation: The array ans is formed as follows:
        - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
        - ans = [1,2,1,1,2,1]
        """
        n = len(nums)
        ans = [0] * 2 * n

        for i, num in enumerate(nums):
            ans[i] = num
            ans[i + n] = num

        return ans

        # return nums + nums

class Stacks:
    def cal_points(self, operations: List[str]) -> int:
        """
        #682 Baseball Game

        You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

        You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
            An integer x.
                Record a new score of x.
            '+'.
                Record a new score that is the sum of the previous two scores.
            'D'.
                Record a new score that is the double of the previous score.
            'C'.
                Invalidate the previous score, removing it from the record.

        Return the sum of all the scores on the record after applying all the operations.

        Input: ops = ["5","2","C","D","+"]
        Output: 30
        Explanation:
        "5" - Add 5 to the record, record is now [5].
        "2" - Add 2 to the record, record is now [5, 2].
        "C" - Invalidate and remove the previous score, record is now [5].
        "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
        "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
        The total sum is 5 + 10 + 15 = 30.
        """
        stack = deque()

        for op in operations:
            match op:
                case "C": # Assume there'll be at least one element if C is called
                    stack.pop()
                case "D": # Assume there'll be at least one element if D is called
                    top = stack[-1]
                    stack.append(2 * top)
                case "+": # Assume there'll be at least two elements if + is called
                    first, second = stack[-1], stack[-2]
                    stack.append(first + second)
                case _: # Assume that if not CD+ it must be integer
                    stack.append(int(op))

        return sum(stack)
