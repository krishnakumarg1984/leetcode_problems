#!/usr/bin/env python3

# 7. Reverse Integer
#
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
#
#
# Example 1:
#
# Input: x = 123
# Output: 321
#
# Example 2:
#
# Input: x = -123
# Output: -321
#
# Example 3:
#
# Input: x = 120
# Output: 21
#
# Example 4:
#
# Input: x = 0
# Output: 0
#
#
#
# Constraints:
#
#     -231 <= x <= 231 - 1

# class Solution:
#     def reverse(self, x: int) -> int:


def myreverse(x):
    digits = []
    mag_x = abs(x)
    while mag_x > 0:
        digits.insert(0, mag_x % 10)
        mag_x = mag_x // 10
    reversed_num = 0
    for place, digit in enumerate(digits):
        reversed_num += digit * (10 ** place)
    if reversed_num > (2 ** 31 - 1) or reversed_num < -(2 ** 31):
        return 0
    if x >= 0:
        return reversed_num
    else:
        return -reversed_num


x = 123
print(myreverse(x))
# Output: 321

x = -123
print(myreverse(x))
# Output: -321

x = 120
print(myreverse(x))
# Output: 21

x = 0
print(myreverse(x))
# Output: 0

x = 1534236469
print(myreverse(x))
# Expected: 0

# Approach 1: Pop and Push Digits & Check before Overflow
#
# Intuition
#
# We can build up the reverse integer one digit at a time. While doing so, we can check beforehand whether or not appending another digit would cause overflow.
#
# Algorithm
#
# Reversing an integer can be done similarly to reversing a string.
#
# We want to repeatedly "pop" the last digit off of xxx and "push" it to the back of the rev\text{rev}rev. In the end, rev\text{rev}rev will be the reverse of the xxx.
#
# To "pop" and "push" digits without the help of some auxiliary stack/array, we can use math.
#
# //pop operation:
# pop = x % 10;
# x /= 10;
#
# //push operation:
# temp = rev * 10 + pop;
# rev = temp;
#
# However, this approach is dangerous, because the statement temp=rev⋅10+pop\text{temp} = \text{rev} \cdot 10 + \text{pop}temp=rev⋅10+pop can cause overflow.
#
# Luckily, it is easy to check beforehand whether or this statement would cause an overflow.
#
# To explain, lets assume that rev\text{rev}rev is positive.
#
#     If temp=rev⋅10+poptemp = \text{rev} \cdot 10 + \text{pop}temp=rev⋅10+pop causes overflow, then it must be that rev≥INTMAX10\text{rev} \geq \frac{INTMAX}{10}rev≥10INTMAX​
#     If rev>INTMAX10\text{rev} > \frac{INTMAX}{10}rev>10INTMAX​, then temp=rev⋅10+poptemp = \text{rev} \cdot 10 + \text{pop}temp=rev⋅10+pop is guaranteed to overflow.
#     If rev==INTMAX10\text{rev} == \frac{INTMAX}{10}rev==10INTMAX​, then temp=rev⋅10+poptemp = \text{rev} \cdot 10 + \text{pop}temp=rev⋅10+pop will overflow if and only if pop>7\text{pop} > 7pop>7
#
# Similar logic can be applied when rev\text{rev}rev is negative.

# Get the sign, get the reversed absolute integer, and return their product if r didn't "overflow".
#
# def reverse(self, x):
#     s = cmp(x, 0)
#     r = int(`s*x`[::-1])
#     return s*r * (r < 2**31)
#
# As compressed one-liner, for potential comparison:
#
# def reverse(self, x):
#     s=cmp(x,0);r=int(`s*x`[::-1]);return(r<2**31)*s*r
#
