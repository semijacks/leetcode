'''
https://leetcode.com/problems/valid-anagram/description/
Problem ID: 242
Problem Name: Valid Anagram
Problem Type: Arrays and Hashing
Difficulty: Easy
'''

"""
Problem Description:
Given two strings s and t , write a function to determine if t is an anagram of s ( return true if anagram and else if not).
input - s = "anagram", t = "nagaram"
output - boolean
"""


"""
Approach
Create a map that will track characters and their frequency (key will be the character and value will be the frequency of that character)
Iterate over the first string and increase the count
Iterate over the second string and decrease the count (if char count is 0, return False)
Return True
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if the length of the strings are equal
        if len(s) != len(t):
            return False
        
        # create mapping of characters and their occurences
        LETTERS = 'abcdefghijklmnopqrstuvwxyz'
        occurences_map = {}
        for letter in LETTERS:
            occurences_map[letter] = 0

        # increase the count of each letter in the first string
        for letter in s:
            occurences_map[letter] += 1
        
        # return False if letter doesn't exist in first string, decrease the count of other letters in the map
        for letter in t:
            if occurences_map[letter] == 0:
                return False
            occurences_map[letter] -= 1

        return True
    
solution = Solution()
s = "anagram"
t = "nagaram"
print(solution.isAnagram(s, t)) # True
s = "rat"
t = "car"
print(solution.isAnagram(s, t)) # False
s = "jar"
t = "jam"
print(solution.isAnagram(s, t)) # False
