from typing import List


class Hash:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        #217. Contains Duplicate

        Given an integer array nums, return true if any value appears at least
        twice in the array, and return false if every element is distinct.
        """
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        #1. Two Sum

        Given an array of integers nums and an integer target, return indices
        of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution,
        and you may not use the same element twice.

        You can return the answer in any order.
        """
        nums_dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_dict:
                return (i, nums_dict[diff])
            nums_dict[num] = i


class LRUCache:
    """
    #146. LRU Cache

    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

    Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

    int get(int key) Return the value of the key if the key exists, otherwise return -1.

    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the
    key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

    The functions get and put must each run in O(1) average time complexity.
    """

    def __init__(self, capacity: int):


    def get(self, key: int) -> int:


    def put(self, key: int, value: int) -> None:
