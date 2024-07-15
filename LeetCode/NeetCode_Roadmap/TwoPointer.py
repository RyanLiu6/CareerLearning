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

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        #15
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
        i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.

        Example 1:
        Input: nums = [-1,0,1,2,-1,-4] -> [-4, -1, -1, 0, 1, 2]
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

        Since we only need to return the distinct elements and not the positions, we can use Set or Dict.

        Hint received: Split into Negatives, Positives, and Zeroes
        """
        # # Not using 2 pointers
        # def check_pairs(to_check, check_against):
        #     n = len(to_check)
        #     for i in range(n):
        #         for j in range(i+1,n):
        #             target = -1*(to_check[i] + to_check[j])
        #             if target in check_against:
        #                 results.add(tuple(sorted((to_check[i], to_check[j], target))))

        # negatives, positives, zeroes = [], [], 0

        # for num in nums:
        #     if num < 0:
        #         negatives.append(num)
        #     elif num > 0:
        #         positives.append(num)
        #     else:
        #         zeroes += 1

        # neg_set, pos_set = set(negatives), set(positives)
        # results = set()

        # # If we have 3 zeroes, then (0, 0, 0)
        # if zeroes >= 3:
        #     results.add((0, 0, 0))

        # # If we have at least one zero, find cases of (-X, 0, X)
        # if zeroes:
        #     for num in negatives:
        #         if -1*num in positives:
        #             results.add((num, 0, -1*num))

        # # Check every pair of negative numbers
        # check_pairs(negatives, pos_set)

        # # Check every pair of positive numbers
        # check_pairs(positives, neg_set)

        # return results

        # 2 pointer solution
        # Sort - O(n logn)
        nums.sort()
        results = []

        # For each x, find y + z such that x + y + z = 0
        for i, x in enumerate(nums):
            # Ignore duplicates
            if i > 0 and x == nums[i - 1]:
                continue

            target = -x
            left, right = i + 1, len(nums) - 1

            while left < right:
                y = nums[left]
                z = nums[right]
                if y + z == target:
                    # If we found one solution, add it
                    results.append((x, y, z))

                    # Find the next unique integer to consider
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif y + z < target:
                    left += 1
                else:
                    right -= 1

        return results

    def maxArea(self, height: List[int]) -> int:
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

    def trap(self, height: List[int]) -> int:
        """
        #42. Trapping Rain Water

        Given n non-negative integers representing an elevation map where the width of each bar is 1, compute
        how much water it can trap after raining.

        Example 1:
        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
        In this case, 6 units of rain water (blue section) are being trapped.

        Example 2:
        Input: height = [4,2,0,3,2,5]
        Output: 9
        """
