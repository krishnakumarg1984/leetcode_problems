#!/usr/bin/env python3

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
#
#
# Constraints:
#
#     The number of nodes in each linked list is in the range [1, 100].
#     0 <= Node.val <= 9
#     It is guaranteed that the list represents a number that does not have leading zeros.
#

# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

# Solution
# Approach 1: Elementary Math
#
# Intuition
#
# Keep track of the carry using a variable and simulate digits-by-digits sum starting from the head of list, which contains the least-significant digit.
#
# Illustration of Adding two numbers
#
# Figure 1. Visualization of the addition of two numbers: 342+465=807342 + 465 = 807342+465=807.
# Each node contains a single digit and the digits are stored in reverse order.
#
# Algorithm
#
# Just like how you would sum two numbers on a piece of paper, we begin by summing the least-significant digits, which is the head of l1l1l1 and l2l2l2. Since each digit is in the range of 0…90 \ldots 90…9, summing two digits may "overflow". For example 5+7=125 + 7 = 125+7=12. In this case, we set the current digit to 222 and bring over the carry=1carry = 1carry=1 to the next iteration. carrycarrycarry must be either 000 or 111 because the largest possible sum of two digits (including the carry) is 9+9+1=199 + 9 + 1 = 199+9+1=19.
#
# The pseudocode is as following:
#
#     Initialize current node to dummy head of the returning list.
#     Initialize carry to 000.
#     Initialize ppp and qqq to head of l1l1l1 and l2l2l2 respectively.
#     Loop through lists l1l1l1 and l2l2l2 until you reach both ends.
#         Set xxx to node ppp's value. If ppp has reached the end of l1l1l1, set to 000.
#         Set yyy to node qqq's value. If qqq has reached the end of l2l2l2, set to 000.
#         Set sum=x+y+carrysum = x + y + carrysum=x+y+carry.
#         Update carry=sum/10carry = sum / 10carry=sum/10.
#         Create a new node with the digit value of (sum mod 10)(sum \bmod 10)(summod10) and set it to current node's next, then advance current node to next.
#         Advance both ppp and qqq.
#     Check if carry=1carry = 1carry=1, if so append a new node with digit 111 to the returning list.
#     Return dummy head's next node.
#
# Note that we use a dummy head to simplify the code. Without a dummy head, you would have to write extra conditional statements to initialize the head's value.
#
# Take extra caution of the following cases:
# Test case 	Explanation
# l1=[0,1]l1=[0,1]l1=[0,1]
# l2=[0,1,2]l2=[0,1,2]l2=[0,1,2] 	When one list is longer than the other.
# l1=[]l1=[]l1=[]
# l2=[0,1]l2=[0,1]l2=[0,1] 	When one list is null, which means an empty list.
# l1=[9,9]l1=[9,9]l1=[9,9]
# l2=[1]l2=[1]l2=[1] 	The sum could have an extra carry of one at the end, which is easy to forget.
#
# Complexity Analysis
#
#     Time complexity : O(max⁡(m,n))O(\max(m, n))O(max(m,n)). Assume that mmm and nnn represents the length of l1l1l1 and l2l2l2 respectively, the algorithm above iterates at most max⁡(m,n)\max(m, n)max(m,n) times.
#
#     Space complexity : O(max⁡(m,n))O(\max(m, n))O(max(m,n)). The length of the new list is at most max⁡(m,n)+1\max(m,n) + 1max(m,n)+1.
#
# Follow up
#
# What if the the digits in the linked list are stored in non-reversed order? For example:
#
# (3→4→2)+(4→6→5)=8→0→7 (3 \to 4 \to 2) + (4 \to 6 \to 5) = 8 \to 0 \to 7 (3→4→2)+(4→6→5)=8→0→7

# class Solution:
# # @return a ListNode
# def addTwoNumbers(self, l1, l2):
#     carry = 0
#     root = n = ListNode(0)
#     while l1 or l2 or carry:
#         v1 = v2 = 0
#         if l1:
#             v1 = l1.val
#             l1 = l1.next
#         if l2:
#             v2 = l2.val
#             l2 = l2.next
#         carry, val = divmod(v1+v2+carry, 10)
#         n.next = ListNode(val)
#         n = n.next
#     return root.next

# def addTwoNumbers(self, l1, l2):
#     dummy = cur = ListNode(0)
#     carry = 0
#     while l1 or l2 or carry:
#         if l1:
#             carry += l1.val
#             l1 = l1.next
#         if l2:
#             carry += l2.val
#             l2 = l2.next
#         cur.next = ListNode(carry%10)
#         cur = cur.next
#         carry //= 10
#     return dummy.next

# Python supports arbitrarily large integers, so I can safely turn the two lists into ints, add them, and turn the sum into a list.
#
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         def toint(node):
#             return node.val + 10 * toint(node.next) if node else 0
#         def tolist(n):
#             node = ListNode(n % 10)
#             if n > 9:
#                 node.next = tolist(n / 10)
#             return node
#         return tolist(toint(l1) + toint(l2))
#
# Iterative tolist instead of recursive:
#
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         def toint(node):
#             return node.val + 10 * toint(node.next) if node else 0
#         n = toint(l1) + toint(l2)
#         first = last = ListNode(n % 10)
#         while n > 9:
#             n /= 10
#             last.next = last = ListNode(n % 10)
#         return first
#
# And a very different solution that could sum arbitrarily many addends, not just two:
#
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         addends = l1, l2
#         dummy = end = ListNode(0)
#         carry = 0
#         while addends or carry:
#             carry += sum(a.val for a in addends)
#             addends = [a.next for a in addends if a.next]
#             end.next = end = ListNode(carry % 10)
#             carry /= 10
#         return dummy.next
