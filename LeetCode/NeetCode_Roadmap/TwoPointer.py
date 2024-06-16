from collections import defaultdict
from typing import List


class Solutions:
    def isPalindrome(self, s: str) -> bool:
        """
        #150

        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
        it reads the same forward and backward. Alphanumeric characters include letters and numbers.

        Given a string s, return true if it is a palindrome, or false otherwise.
        """
        cleaned_string = []
        for letter in s:
            if letter.isalnum():
                cleaned_string.append(letter.lower())

        n = len(cleaned_string)
        start, end = 0, n - 1
        while start < end:
            start_letter = cleaned_string[start]
            end_letter = cleaned_string[end]

            if start_letter != end_letter:
                return False

            start += 1
            end -= 1

        return True

    def two_sum_with_sorted_input(self, numbers: List[int], target: int) -> List[int]:
        """
        #167
        Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers
        such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

        Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

        The tests are generated such that there is exactly one solution. You may not use the same element twice.

        Your solution must use only constant extra space.

        Notes:
        * numbers is sorted in non-decreasing order.
        * The tests are generated such that there is exactly one solution.

        Example 1:
        Input: numbers = [2,7,11,15], target = 9
        Output: [1,2]
        Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

        Example 2:
        Input: numbers = [2,3,4], target = 6
        Output: [1,3]
        Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

        Example 3:
        Input: numbers = [-1,0], target = -1
        Output: [1,2]
        Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
        """
        n = len(numbers)
        start, end = 0, n - 1

        # Guaranteed that two of the same element (same index) cannot be the solution
        while start < end:
            start_num = numbers[start]
            end_num = numbers[end]

            total = start_num + end_num
            if total == target:
                return [start+1, end+1]
            elif total < target:
                start += 1
            else:
                end -= 1

    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        #15
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
        i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.

        Example 1:
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        Explanation:
        nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        The distinct triplets are [-1,0,1] and [-1,-1,2].
        Notice that the order of the output and the order of the triplets does not matter.

        Example 2:
        Input: nums = [0,1,1]
        Output: []
        Explanation: The only possible triplet does not sum up to 0.

        Example 3:
        Input: nums = [0,0,0]
        Output: [[0,0,0]]
        Explanation: The only possible triplet sums up to 0.

        First approach is to implement two_sum and turn three_sum into a two_sum problem. This solution
        works but has a pretty bad time complexity of O(n^2) since for each element of nums, we have to
        iterate through nums to try two_sum.

        Still want to turn 3sum into 2sum by isolating the first element to be each element of nums.
        Now we're faced with 2sum for an array where elements can repeat - let's sort the array and deal with it
        """
        ...

    def max_area(self, height: List[int]) -> int:
        """
        #11. Container With Most Water

        You are given an integer array height of length n. There are n vertical lines drawn such that the two
        endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a
        container, such that the container contains the most water. Return the maximum amount of water a container can store.
        Notice that you may not slant the container.

        Example 1:
        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water
            (blue section) the container can contain is 49.

        We need to make some sort of container with left and right lines, so we need two pointers. Area is calculated as the
        container where height = min(height[left], height[right]) and width = (right - left).
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
