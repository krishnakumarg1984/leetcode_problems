#!/usr/bin/env python3

# 20. Valid Parentheses
# Easy
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
#
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
#
# Input: s = "(]"
# Output: false
#
# Example 4:
#
# Input: s = "([)]"
# Output: false
#
# Example 5:
#
# Input: s = "{[]}"
# Output: true
#
# Constraints:
#
#     1 <= s.length <= 104
#     s consists of parentheses only '()[]{}'.

#     if not s:
#         return False

# class Solution:
#     def isValid(self, s: str) -> bool:


# def isValid(s: str) -> bool:
#     parens_stack = []
#     # open_parens = ["(", "{", "["]
#     close_parens = [")", "}", "]"]
#     for current_char in s:
#         if current_char not in close_parens:
#             parens_stack.append(current_char)
#             continue
#         if not parens_stack:
#             return False
#         last_open_char = parens_stack.pop()
#         if (
#             (last_open_char == "(" and current_char != ")")
#             or (last_open_char == "{" and current_char != "}")
#             or (last_open_char == "[" and current_char != "]")
#         ):
#             return False
#
#     if not parens_stack:
#         return True
#     else:
#         return False


def isValid(s: str) -> bool:
    parens_stack = []
    valid_parens = {"(": ")", "{": "}", "[": "]"}
    for current_char in s:
        if current_char in valid_parens.keys():
            parens_stack.append(current_char)
            continue
        if not parens_stack:
            return False
        last_opening_paren = parens_stack.pop()
        if valid_parens[last_opening_paren] != current_char:
            return False

    # At this stage, the stack must be empty (since all matching opening brackets would have been popped). If not empty, it means that an unmatched set of opening parens are present in the stack. Hence, invalid matching (return False)
    return False if parens_stack else True


s = "()"
print(isValid(s))
# Output: true

s = "()[]{}"
print(isValid(s))
# Output: true

s = "(]"
print(isValid(s))
# Output: false

s = "([)]"
print(isValid(s))
# Output: false

s = "{[]}"
print(isValid(s))
# Output: true
