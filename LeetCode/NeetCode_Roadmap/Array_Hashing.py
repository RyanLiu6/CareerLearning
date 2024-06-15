import heapq
from typing import List
from collections import defaultdict


class Solutions:
    def contains_duplicate(self, nums: List[int]) -> bool:
        """
        #217
        Given an integer array nums, return true if any value appears at least
        twice in the array, and return false if every element is distinct.
        """
        existence_map = {}
        for num in nums:
            if num in existence_map:
                return True
            else:
                existence_map[num] = True
        return False

    def is_anagram(self, s: str, t: str) -> bool:
        """
        #242
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        An Anagram is a word or phrase formed by rearranging the letters of a different word
        or phrase, typically using all the original letters exactly once.

        First solution is with a Dictionary (Map) -> O(s+t) time and O(s) space
        Can also use sorted but not sure if available during interview.
        """
        if len(s) != len(t):
            return False

        s_freq_map = defaultdict(int)
        for letter in s:
            s_freq_map[letter] += 1

        for letter in t:
            if letter not in s_freq_map:
                return False
            s_freq_map[letter] -= 1

        for freq in s_freq_map.values():
            if freq != 0:
                return False

        return True

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        #1
        Given an array of integers nums and an integer target, return indices of the two
        numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may not
        use the same element twice.

        You can return the answer in any order.
        """
        nums_dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_dict:
                return (i, nums_dict[diff])
            nums_dict[num] = i

    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """
        #49
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
        typically using all the original letters exactly once.

        Example 1:
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

        Example 2:
        Input: strs = [""]
        Output: [[""]]

        Constraints:
            1 <= strs.length <= 104
            0 <= strs[i].length <= 100
            strs[i] consists of lowercase English letters.

        Using sorted would have runtime complexity of O(m*nlogn) where m is len(strs) and n is average length
        of individual strings.

        Using ORD method would have runtime complexity of O(m*n) where m is len(strs) and n is average length
        of individual strings.
        """
        buckets = defaultdict(list)
        for string in strs:
            buckets["".join(sorted(string))].append(string)

        return buckets.values()

        # buckets = defaultdict(list)

        # for string in strs:
        #     string_count = [0] * 26
        #     for letter in string:
        #         string_count[ord(letter) - ord("a")] += 1
        #     buckets[tuple(string_count)].append(string)

        # return buckets.values()

    def top_k_frequent(self, nums: List[int], k:int) -> List[int]:
        """
        #347
        Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

        Example 1:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]

        Example 2:
        Input: nums = [1], k = 1
        Output: [1]

        Constraints:
            1 <= nums.length <= 105
            -104 <= nums[i] <= 104
            k is in the range [1, the number of unique elements in the array].
            It is guaranteed that the answer is unique.

        Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

        Using sorted, the solution has a time complexity of O(n + mlogm) where n is len(nums) and m is len(freq_map),
        but since m <= n, worst case, we can assume then time complexity is O(n + nlogn) -> O(nlogn)

        If we can't use sorted, we can use a maxHeap instead - heaps take a tuple, where first item is the priority
        to be sorted on, and the second can be the value
        """
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        count = 0
        results = []
        for item in sorted(freq_map, key=freq_map.get, reverse=True):
            if count >= k:
                continue
            results.append(item)
            count += 1

        return results

        # freq_map = defaultdict(int)
        # for num in nums:
        #     freq_map[num] += 1

        # maxHeap = [(-value, key) for key, value in freq_map.items()]
        # heapq.heapify(maxHeap)

        # results = []
        # for i in range(k):
        #     results.append(heapq.heappop(maxHeap)[1])

        # return results

    def encode(self, strs: List[str]) -> str:
        """
        #271
        Design an algorithm to encode a list of strings to a string. The encoded string is then
        sent over the network and is decoded back to the original list of strings.

        Because the string may contain any of the 256 legal ASCII characters, your algorithm must
        be able to handle any character that may appear.

        Example 1
        Input: ["we", "say", ":", "yes"]
        Output: ["we", "say", ":", "yes"]
        Explanation:
        One possible encode method is: "we:;say:;:::;yes"
        """
        encoded_string = ""
        for string in strs:
            encoded_string += f"{len(string)},{string}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []

        i = 0
        while i < len(s):
            # Find our own delimiter of "," then get length of string
            j = i
            while s[j] != ",":
                j += 1
            length = int(s[i:j])
            decoded_strings.append(s[j+1:j+length + 1])
            i = j + length + 1

        return decoded_strings

    def product_except_self(self, nums: List[int]) -> List[int]:
        """
        #238
        Given an integer array nums, return an array answer such that answer[i] is equal to the
        product of all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        You must write an algorithm that runs in O(n) time and without using the division operation.

        Example 1:
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]

        Example 2:
        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]

        Constraints:
            2 <= nums.length <= 105
            -30 <= nums[i] <= 30
            The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        Follow up: Can you solve the problem in O(1) extra space complexity?
        (The output array does not count as extra space for space complexity analysis.)
        """
        # Left and Right products
        n = len(nums)

        left_product = [1] * n
        for i in range(1,n):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        right_product = [1] * n
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        result = []
        for i in range(n):
            result.append(left_product[i] * right_product[i])

        return result

        # Single array
        n, left, right = len(nums), 1, 1
        products = [1] * n

        for i in range(n):
            products[i] = left
            left *= nums[i]

        for i in range(n - 1, -1, -1):
            products[i] *= right
            right *= nums[i]

        return products

    def valid_sudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
        validated according to the following rules:

        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

        Note:
        A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        Only the filled cells need to be validated according to the mentioned rules.
        """
        def _validate_rows() -> bool:
            for row in board:
                nums = {}
                for num in row:
                    if num in nums and num != ".":
                        return False
                    else:
                        nums[num] = True
            return True

        def _validate_columns() -> bool:
            for i in range(9):
                nums = {}
                for j in range(9):
                    num = board[j][i]
                    if num in nums and num != ".":
                        return False
                    else:
                        nums[num] = True
            return True

        def _validate_3x3s() -> bool:
            for i in range(3):
                for j in range(3):
                    nums = {}
                    square_nums = [board[x][y] for x in range(i*3, (i+1)*3) for y in range(j*3, (j+1)*3)]
                    for num in square_nums:
                        if num in nums and num != ".":
                            return False
                        else:
                            nums[num] = True
            return True

        return _validate_rows() and _validate_columns() and _validate_3x3s()

    def longest_consecutive(self, nums: List[int]) -> int:
        """
        #128
        Given an unsorted array of integers nums, return the length of the longest
        consecutive elements sequence. You must write an algorithm that runs in O(n) time.

        Example 1:
        Input: nums = [100,4,200,1,3,2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

        Example 2:
        Input: nums = [0,3,7,2,5,8,4,6,0,1]
        Output: 9

        Constraints:
            0 <= nums.length <= 105
            -109 <= nums[i] <= 109

        Cannot use .sort as it would break constraint of being O(n) time.

        Original solution uses dictionary to emulate a LinkedList.

        Optimal solution checks for existence, ie:
        1. For each num, check if num - 1 exists. If it does not, then we know num is the start
            of a sequence
        2. Then we can check if num + 1, num + 2, num + 3, ... and so on exists

        """
        max_value = float("inf")
        nums_dict = defaultdict(lambda: {"prev": max_value, "next": max_value})

        for num in nums:
            _ = nums_dict[num]
            plus, minus = num + 1, num - 1

            if plus in nums_dict:
                nums_dict[plus]["prev"] = num
                nums_dict[num]["next"] = plus

            if minus in nums_dict:
                nums_dict[minus]["next"] = num
                nums_dict[num]["prev"] = minus

        longest = 0
        for num in nums_dict:
            if nums_dict[num]["prev"] == max_value:
                length = 1
                inner = nums_dict[num]["next"]
                while inner != max_value:
                    length += 1
                    inner = nums_dict[inner]["next"]
                longest = max(longest, length)

        return longest

        # nums_set = set(nums)
        # max_length = 0
        # for num in nums:
        #     if (num - 1) not in nums_set:
        #         count = 1
        #         while (num + count) in nums_set:
        #             count += 1
        #         max_length = max(count, max_length)
        # return max_length
