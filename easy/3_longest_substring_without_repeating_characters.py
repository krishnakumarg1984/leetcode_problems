#!/usr/bin/env python3

# 3. Longest Substring Without Repeating Characters
#
# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Example 4:
#
# Input: s = ""
# Output: 0
#
# Constraints:
#
#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:

# Solution Article
# Approach 1: Brute Force
#
# Intuition
#
# Check all the substring one by one to see if it has no duplicate character.
#
# Algorithm
#
# Suppose we have a function boolean allUnique(String substring) which will return true if the characters in the substring are all unique, otherwise false. We can iterate through all the possible substrings of the given string s and call the function allUnique. If it turns out to be true, then we update our answer of the maximum length of substring without duplicate characters.
#
# Now let's fill the missing parts:
#
#     To enumerate all substrings of a given string, we enumerate the start and end indices of them. Suppose the start and end indices are iii and jjj, respectively. Then we have 0≤i<j≤n0 \leq i \lt j \leq n0≤i<j≤n (here end index jjj is exclusive by convention). Thus, using two nested loops with iii from 0 to n−1n - 1n−1 and jjj from i+1i+1i+1 to nnn, we can enumerate all the substrings of s.
#
#     To check if one string has duplicate characters, we can use a set. We iterate through all the characters in the string and put them into the set one by one. Before putting one character, we check if the set already contains it. If so, we return false. After the loop, we return true.
#
# Complexity Analysis
#
#     Time complexity : O(n3)O(n^3)O(n3).
#
#     To verify if characters within index range [i,j)[i, j)[i,j) are all unique, we need to scan all of them. Thus, it costs O(j−i)O(j - i)O(j−i) time.
#
#     For a given i, the sum of time costed by each j∈[i+1,n]j \in [i+1, n]j∈[i+1,n] is
#
#     ∑i+1nO(j−i) \sum_{i+1}^{n}O(j - i) ∑i+1n​O(j−i)
#
#     Thus, the sum of all the time consumption is:
#
#     O(∑i=0n−1(∑j=i+1n(j−i)))=O(∑i=0n−1(1+n−i)(n−i)2)=O(n3) O\left(\sum_{i = 0}^{n - 1}\left(\sum_{j = i + 1}^{n}(j - i)\right)\right) = O\left(\sum_{i = 0}^{n - 1}\frac{(1 + n - i)(n - i)}{2}\right) = O(n^3) O(∑i=0n−1​(∑j=i+1n​(j−i)))=O(∑i=0n−1​2(1+n−i)(n−i)​)=O(n3)
#
#     Space complexity : O(min(n,m))O(min(n, m))O(min(n,m)). We need O(k)O(k)O(k) space for checking a substring has no duplicate characters, where kkk is the size of the Set. The size of the Set is upper bounded by the size of the string nnn and the size of the charset/alphabet mmm.
#
# Approach 2: Sliding Window
#
# Algorithm
#
# The naive approach is very straightforward. But it is too slow. So how can we optimize it?
#
# In the naive approaches, we repeatedly check a substring to see if it has duplicate character. But it is unnecessary. If a substring sijs_{ij}sij​ from index iii to j−1j - 1j−1 is already checked to have no duplicate characters. We only need to check if s[j]s[j]s[j] is already in the substring sijs_{ij}sij​.
#
# To check if a character is already in the substring, we can scan the substring, which leads to an O(n2)O(n^2)O(n2) algorithm. But we can do better.
#
# By using HashSet as a sliding window, checking if a character in the current can be done in O(1)O(1)O(1).
#
# A sliding window is an abstract concept commonly used in array/string problems. A window is a range of elements in the array/string which usually defined by the start and end indices, i.e. [i,j)[i, j)[i,j) (left-closed, right-open). A sliding window is a window "slides" its two boundaries to the certain direction. For example, if we slide [i,j)[i, j)[i,j) to the right by 111 element, then it becomes [i+1,j+1)[i+1, j+1)[i+1,j+1) (left-closed, right-open).
#
# Back to our problem. We use HashSet to store the characters in current window [i,j)[i, j)[i,j) (j=ij = ij=i initially). Then we slide the index jjj to the right. If it is not in the HashSet, we slide jjj further. Doing so until s[j] is already in the HashSet. At this point, we found the maximum size of substrings without duplicate characters start with index iii. If we do this for all iii, we get our answer.
#
# Complexity Analysis
#
#     Time complexity : O(2n)=O(n)O(2n) = O(n)O(2n)=O(n). In the worst case each character will be visited twice by iii and jjj.
#
#     Space complexity : O(min(m,n))O(min(m, n))O(min(m,n)). Same as the previous approach. We need O(k)O(k)O(k) space for the sliding window, where kkk is the size of the Set. The size of the Set is upper bounded by the size of the string nnn and the size of the charset/alphabet mmm.
#
# Approach 3: Sliding Window Optimized
#
# The above solution requires at most 2n steps. In fact, it could be optimized to require only n steps. Instead of using a set to tell if a character exists or not, we could define a mapping of the characters to its index. Then we can skip the characters immediately when we found a repeated character.
#
# The reason is that if s[j]s[j]s[j] have a duplicate in the range [i,j)[i, j)[i,j) with index j′j'j′, we don't need to increase iii little by little. We can skip all the elements in the range [i,j′][i, j'][i,j′] and let iii to be j′+1j' + 1j′+1 directly.
#
# Java (Using HashMap)
#
# Here is a visualization of the above code.

# Java (Assuming ASCII 128)
#
# The previous implements all have no assumption on the charset of the string s.
#
# If we know that the charset is rather small, we can replace the Map with an integer array as direct access table.
#
# Commonly used tables are:
#
#     int[26] for Letters 'a' - 'z' or 'A' - 'Z'
#     int[128] for ASCII
#     int[256] for Extended ASCII
#

# Complexity Analysis
#
#     Time complexity : O(n)O(n)O(n). Index jjj will iterate nnn times.
#
#     Space complexity (HashMap) : O(min(m,n))O(min(m, n))O(min(m,n)). Same as the previous approach.
#
#     Space complexity (Table): O(m)O(m)O(m). mmm is the size of the charset.


# def lengthOfLongestSubstring(s: str) -> int:
#     max_len = None
#     left = 0
#     right = 0
#     curr_substr = ""
#     while right < len(s):
#         print("Next char: ", s[right])
#         if s[right] not in curr_substr:
#             curr_substr += s[right]
#         else:
#             if max_len is None:
#                 max_len = right - left
#             elif max_len < (right - left):
#                 max_len = right - left
#             left += curr_substr.rfind(s[right]) + 1
#             curr_substr = s[left : (right + 1)]
#         right += 1
#         print("curr_substr", curr_substr)


def lengthOfLongestSubstring(s):
    max_count = 0
    if not s:
        return max_count
    # create a window with left and right
    # keep a hash table of characters already added
    left = 0
    right = 0
    last_seen_idx = {}  # keeps track of seen characters

    for idx, character in enumerate(s):
        # notice this logic
        if character not in last_seen_idx or last_seen_idx[character] < left:
            last_seen_idx[character] = idx
            right = idx
            if (right - left + 1) > max_count:  # update the largest count
                max_count = right - left + 1
        else:
            # we move start to one element after we found the character
            left = last_seen_idx[character] + 1
            # update index of last time we saw the character
            last_seen_idx[character] = idx

    return max_count


s = "abcabcbb"
print(lengthOfLongestSubstring(s))
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

s = "bbbbb"
print(lengthOfLongestSubstring(s))
# Output: 1
# Explanation: The answer is "b", with the length of 1.

s = "pwwkew"
print(lengthOfLongestSubstring(s))
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

s = ""
print(lengthOfLongestSubstring(s))
# Output: 0


# class Solution:
#     # @return an integer
#     def lengthOfLongestSubstring(self, s):
#         start = maxLength = 0
#         usedChar = {}
#
#         for i in range(len(s)):
#             if s[i] in usedChar and start <= usedChar[s[i]]:
#                 start = usedChar[s[i]] + 1
#             else:
#                 maxLength = max(maxLength, i - start + 1)
#
#             usedChar[s[i]] = i
#
#         return maxLength


# def lengthOfLongestSubstring(self, s):
#     dic, res, start, = (
#         {},
#         0,
#         0,
#     )
#     for i, ch in enumerate(s):
#         if ch in dic:
#             res = max(res, i - start)  # update the res
#             start = max(start, dic[ch] + 1)  # here should be careful, like "abba"
#         dic[ch] = i
#     return max(
#         res, len(s) - start
#     )  # return should consider the last non-repeated substring


# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         last, res, st = {}, 0, 0
#         for i, v in enumerate(string):
#             if v not in last or last[v] < st:
#                 res = max(res, i - st + 1)
#             else:
#                 st = last[v] + 1
#             last[v] = i
#         return res
