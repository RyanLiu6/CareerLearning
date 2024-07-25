from collections import defaultdict
from pprint import pprint
from typing import List


class Solutions:
    def maxProfit(self, prices: List[int]) -> int:
        """
        #121: Best Time to Buy and Sell Stock

        You are given an array prices where prices[i] is the price of a given stock on the ith day.
        You want to maximize your profit by choosing a single day to buy one stock and choosing a
        different day in the future to sell that stock. Return the maximum profit you can achieve
        from this transaction. If you cannot achieve any profit, return 0.

        Example 1:
        Input: prices = [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        Note that buying on day 2 and selling on day 1 is not allowed because you must buy
        before you sell.

        Example 2:
        Input: prices = [7,6,4,3,1]
        Output: 0
        Explanation: In this case, no transactions are done and the max profit = 0.
        """
        max_profit, min_price = 0, 0

        for i, price in enumerate(prices):
            # First element can only be buy and not sell - set min_price here
            if i == 0:
                min_price = price

            # If current price is smaller than minimum price, then we buy -> can't sell
            if price < min_price:
                min_price = price
            # Since we're not buying -> set max_profit here
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)

        return max_profit

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        #3. Longest Substring Without Repeating Characters

        Given a string s, find the length of the longest substring without repeating characters.

        Example 1:
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
        """
        freq_set = set()
        left = max_length = 0

        for right in range(len(s)):
            letter = s[right]

            # Once we find a duplicate, we need to calculate the length of the subarray
            # And where we skip next to
            while letter in freq_set:
                left_letter = s[left]
                freq_set.remove(left_letter)
                left += 1

            freq_set.add(letter)
            max_length = max(max_length, right - left + 1)

        return max_length

    def characterReplacement(self, s: str, k: int) -> int:
        """
        #424. Longest Repeating Character Replacement

        You are given a string s and an integer k. You can choose any character of the
        string and change it to any other uppercase English character. You can perform this
        operation at most k times.

        Return the length of the longest substring containing the same letter you can get
        after performing the above operations.

        Example 1:
        Input: s = "ABAB", k = 2
        Output: 4
        Explanation: Replace the two 'A's with two 'B's or vice versa.

        Example 2:
        Input: s = "AABABBA", k = 1
        Output: 4
        Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
        The substring "BBBB" has the longest repeating letters, which is 4.
        There may exists other ways to achieve this answer too.
        """
        ...

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        #567. Permutation in String

        Given two strings s1 and s2, return true if s2 contains a permutation of s1,
        or false otherwise.

        In other words, return true if one of s1's permutations is the substring of s2.

        Example 1:
        Input: s1 = "ab", s2 = "eidbaooo"
        Output: true
        Explanation: s2 contains one permutation of s1 ("ba").

        Example 2:
        Input: s1 = "ab", s2 = "eidboaoo"
        Output: false
        """
        def compare(first, second):
            for key, value in second.items():
                if key not in first:
                    return False
                if first[key] != value:
                    return False
            return True

        window_size = len(s1)
        s1_dict = defaultdict(int)
        for letter in s1:
            s1_dict[letter] += 1

        s2_dict = defaultdict(int)
        for letter in s2[:window_size - 1]:
            s2_dict[letter] += 1

        left = 0
        for i in range(len(s2) - window_size + 1):
            s2_dict[s2[i + window_size - 1]] += 1

            # Compare the two dicts
            if compare(s1_dict, s2_dict):
                return True

            # Comparison done, now we need to remove from the left side
            value = s2[left]
            if s2_dict[value] - 1 == 0:
                del s2_dict[value]
            else:
                s2_dict[value] -= 1
            left += 1

        return False
