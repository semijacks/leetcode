from typing import List

"""
https://leetcode.com/problems/two-sum/description/
Problem ID: 1
Problem Name: Two Sum
Problem Type: Arrays and Hashing
Difficulty: Easy
"""

"""
Problem Description:
Given a list of numbers and a target number, return the indices of two numbers that add up to the target number.
input - nums = [2, 7, 11, 15], target = 9
output - [0, 1]
"""

"""
Approach 1
Create a hashmap maps an item's index to its value
Iterate over the list and check if the difference between the target and the current number exists in the hashmap
If it does, return the index of the diff in the hashmap in the current iteration index
If it does not, add the item and its index to the hashmap
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {} # val : index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in diff_map:
                return [diff_map[diff], i]
            diff_map[num] = i

"""
Approach 2 - Brute Force
Iterate over the list and check if the sum of the current number and any other number in the list is equal to the target
"""