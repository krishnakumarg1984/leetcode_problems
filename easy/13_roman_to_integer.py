#!/usr/bin/env python3

# 13. Roman to Integer
# Easy
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
#     I can be placed before V (5) and X (10) to make 4 and 9.
#     X can be placed before L (50) and C (100) to make 40 and 90.
#     C can be placed before D (500) and M (1000) to make 400 and 900.
#
# Given a roman numeral, convert it to an integer.
#
#
#
# Example 1:
#
# Input: s = "III"
# Output: 3
#
# Example 2:
#
# Input: s = "IV"
# Output: 4
#
# Example 3:
#
# Input: s = "IX"
# Output: 9
#
# Example 4:
#
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#
# Example 5:
#
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#
#
# Constraints:
#
#     1 <= s.length <= 15
#     s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
#     It is guaranteed that s is a valid roman numeral in the range [1, 3999].
#
# Accepted
# 1,158,859
# Submissions
# 2,010,444

# class Solution:
#     def romanToInt(self, s: str) -> int:


# def romanToInt(s: str) -> int:
#     roman_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
#     integer_equivalent = 0
#
#     # Flags to indicate that the subsequent roman letter could be special requiring subtraction of the relevent current letter from the next letter (instead of the usual addition)
#     flag_I = flag_X = flag_C = False
#     for roman_letter in s:
#         integer_equivalent += roman_dict[roman_letter]
#         if (not flag_I) and roman_letter == "I":
#             flag_I = True
#         elif flag_I and (roman_letter == "V" or roman_letter == "X"):
#             flag_I = False
#             # compensate for addition for the previous I & then subtract the value of 'I' to get the right answer
#             integer_equivalent -= 2 * roman_dict["I"]
#         elif (not flag_X) and roman_letter == "X":
#             flag_X = True
#         elif flag_X and (roman_letter == "L" or roman_letter == "C"):
#             flag_X = False
#             integer_equivalent -= 2 * roman_dict["X"]
#         elif (not flag_C) and roman_letter == "C":
#             flag_C = True
#         elif flag_C and (roman_letter == "D" or roman_letter == "M"):
#             flag_C = False
#             integer_equivalent -= 2 * roman_dict["C"]
#
#     return integer_equivalent


# def romanToInt(s: str) -> int:
#     if not s:
#         return 0
#     roman_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
#     integer_equivalent = roman_dict[s[-1]]
#     for i in reversed(range(len(s) - 1)):
#         if roman_dict[s[i]] < roman_dict[s[i + 1]]:
#             integer_equivalent -= roman_dict[s[i]]
#         else:
#             integer_equivalent += roman_dict[s[i]]
#     return integer_equivalent


def romanToInt(s: str) -> int:
    integer_equivalent = 0
    prev_letter_value = None
    roman_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    for curr_letter in s[::-1]:  # reverse 's'
        if prev_letter_value is None or roman_dict[curr_letter] >= prev_letter_value:
            # add the current letter value if it is equal or higher than the previous value
            integer_equivalent += roman_dict[curr_letter]
        else:
            # subtract the current letter value when it is like "IV" --> 5-1, "IX" --> 10 -1 etc
            integer_equivalent -= roman_dict[curr_letter]
        prev_letter_value = roman_dict[curr_letter]
    return integer_equivalent


print(romanToInt("CMXCIV"))
print(romanToInt("DXCI"))
print(romanToInt("CXVII"))
print(romanToInt("XL"))
print(romanToInt("XC"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
print(romanToInt("I"))
print(romanToInt("II"))
print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("V"))
print(romanToInt("VI"))
print(romanToInt("VII"))
print(romanToInt("VIII"))
print(romanToInt("IX"))
print(romanToInt("X"))
print(romanToInt("XI"))
print(romanToInt("XII"))
print(romanToInt("XIII"))
print(romanToInt("XIV"))
print(romanToInt("XV"))
print(romanToInt("XVI"))
