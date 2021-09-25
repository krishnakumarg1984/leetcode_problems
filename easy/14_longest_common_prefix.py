#!/usr/bin/env python3

# 14. Longest Common Prefix
# Easy
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
#
# Constraints:
#
#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lower-case English letters.


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:


def longestCommonPrefix(strs: list[str]) -> str:
    zipped_list = list(zip(*strs))
    # prefix = []
    prefix = ""
    for char_tuple in zipped_list:
        if len(set(char_tuple)) > 1:
            break
        prefix += char_tuple[0]
    # return "".join(prefix)
    return prefix


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
# Output: "fl"
