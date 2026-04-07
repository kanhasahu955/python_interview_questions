# String Related DSA Problems

This file focuses only on string-based DSA and interview questions.

String questions are very common because they test:

- hashing and frequency counting
- two pointers
- sliding window
- substring handling
- palindrome logic
- serialization thinking

## Core String Problems

### 1. Valid Anagram
Check whether two strings contain the same characters with the same frequencies.

Input:
- `s = "listen"`
- `t = "silent"`

Output:
- `true`

### 2. Group Anagrams
Group together strings that are anagrams of each other.

Input:
- `["eat", "tea", "tan", "ate", "nat", "bat"]`

Output:
- `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`

### 3. Longest Substring Without Repeating Characters
Find the longest substring where every character is unique.

Input:
- `"abcabcbb"`

Output:
- `3`

### 4. Minimum Window Substring
Find the smallest substring that contains all characters of another string.

Input:
- `source = "ADOBECODEBANC"`
- `target = "ABC"`

Output:
- `"BANC"`

### 5. Longest Palindromic Substring
Find the longest substring that reads the same forward and backward.

Input:
- `"babad"`

Output:
- `"bab"` or `"aba"`

### 6. Valid Palindrome
Ignore symbols and case, then check whether the string is a palindrome.

Input:
- `"A man, a plan, a canal: Panama"`

Output:
- `true`

### 7. Longest Common Prefix
Find the common prefix shared by all strings in a list.

Input:
- `["flower", "flow", "flight"]`

Output:
- `"fl"`

### 8. Find All Anagrams in a String
Return all starting positions where an anagram of a target string appears.

Input:
- `source = "cbaebabacd"`
- `target = "abc"`

Output:
- `[0, 6]`

### 9. Permutation in String
Check whether one string contains any permutation of another string.

Input:
- `pattern = "ab"`
- `text = "eidbaooo"`

Output:
- `true`

### 10. Count Palindromic Substrings
Count every palindromic substring in a string.

Input:
- `"aaa"`

Output:
- `6`

### 11. Encode and Decode Strings
Turn a list of strings into one string and recover it safely.

Input:
- `["leet", "code", "python"]`

Output:
- encoded example: `"4#leet4#code6#python"`
- decoded output: `["leet", "code", "python"]`

### 12. Longest Repeating Character Replacement
Find the longest substring that can be turned into one repeating character after at most `k` replacements.

Input:
- `text = "AABABBA"`
- `k = 1`

Output:
- `4`

### 13. Zigzag Conversion
Write characters in zigzag pattern and then read row by row.

Input:
- `text = "PAYPALISHIRING"`
- `numRows = 3`

Output:
- `"PAHNAPLSIIGYIR"`

### 14. String to Integer (atoi)
Convert a string to integer while handling spaces, signs, and overflow-style boundaries.

Input:
- `"   -42"`

Output:
- `-42`

### 15. Implement strStr()
Find the first index of one string inside another.

Input:
- `haystack = "sadbutsad"`
- `needle = "sad"`

Output:
- `0`

### 16. Decode String
Decode nested patterns like `3[a2[c]]`.

Input:
- `"3[a2[c]]"`

Output:
- `"accaccacc"`

### 17. Substring with Concatenation of All Words
Find starting positions where all given words appear exactly once and continuously.

Input:
- `text = "barfoothefoobarman"`
- `words = ["foo", "bar"]`

Output:
- `[0, 9]`

## Good Study Order

1. Valid Anagram
2. Valid Palindrome
3. Longest Common Prefix
4. Group Anagrams
5. Longest Substring Without Repeating Characters
6. Find All Anagrams in a String
7. Permutation in String
8. Minimum Window Substring
9. Longest Palindromic Substring
10. Count Palindromic Substrings
11. Encode and Decode Strings
12. Longest Repeating Character Replacement
13. Zigzag Conversion
14. String to Integer (atoi)
15. Implement strStr()
16. Decode String
17. Substring with Concatenation of All Words

## Debugging Pattern For String Problems

1. Print current characters and indices.
2. Print frequency maps after updates.
3. Print left and right pointers for window problems.
4. Print substring candidates when answer changes.
5. For palindrome problems, print the current center and expansion range.
6. For encode/decode, print delimiter positions and parsed lengths.

## Code Files

- `python/strings_sliding_window.py`
- `javascript/strings_sliding_window.js`
