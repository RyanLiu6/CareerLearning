from typing import List


class Solutions:
    def maxProfit(self, prices: List[int]) -> int:
        """
        #121: Best Time to Buy and Sell Stock

        You are given an array prices where prices[i] is the price of a given stock on the ith day.
        You want to maximize your profit by choosing a single day to buy one stock and choosing a
        different day in the future to sell that stock. Return the maximum profit you can achieve from
        this transaction. If you cannot achieve any profit, return 0.

        Example 1:
        Input: prices = [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

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

        Example 2:
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

        Example 3:
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
        """
        substring = []

