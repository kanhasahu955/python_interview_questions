# Set and HashSet DSA Problems

This file covers all common interview problems that use **Set**, **HashSet**, or **Set theory** operations.

Sets are tested because they provide:
- O(1) average lookup, insert, delete
- Deduplication
- Membership testing
- Intersection, union, difference operations
- Cycle and duplicate detection
- Efficient range/sequence queries

---

## Core Set Problems

### 1. Contains Duplicate
Check whether any value appears more than once.

Input:
- `[1, 2, 3, 1]`

Output:
- `true`

Input:
- `[1, 2, 3, 4]`

Output:
- `false`

What it tests:
- basic set insertion + membership check

---

### 2. Contains Duplicate II
Return true if any two equal elements are within k indices of each other.

Input:
- `nums = [1, 2, 3, 1]`, `k = 3`

Output:
- `true`

Input:
- `nums = [1, 0, 1, 1]`, `k = 1`

Output:
- `true`

What it tests:
- sliding window set of size k

---

### 3. Intersection of Two Arrays
Return unique elements present in both arrays.

Input:
- `nums1 = [1, 2, 2, 1]`, `nums2 = [2, 2]`

Output:
- `[2]`

Input:
- `nums1 = [4, 9, 5]`, `nums2 = [9, 4, 9, 8, 4]`

Output:
- `[9, 4]`

What it tests:
- set intersection operation

---

### 4. Union of Two Arrays
Return all unique elements from both arrays combined.

Input:
- `[1, 2, 3]` and `[2, 3, 4, 5]`

Output:
- `[1, 2, 3, 4, 5]`

What it tests:
- set union operation

---

### 5. Difference of Two Arrays
Return elements in nums1 that are not in nums2, and vice versa.

Input:
- `nums1 = [1, 2, 3]`, `nums2 = [2, 4, 6]`

Output:
- `[[1, 3], [4, 6]]`

What it tests:
- set difference operation

---

### 6. Longest Consecutive Sequence
Find the length of the longest consecutive integer sequence.

Input:
- `[100, 4, 200, 1, 3, 2]`

Output:
- `4`  (sequence: 1, 2, 3, 4)

Input:
- `[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]`

Output:
- `9`

What it tests:
- building set for O(1) lookup
- starting sequence only at the smallest element

---

### 7. Happy Number
Use a set to detect whether digit-square sum cycles back to 1.

Input:
- `19`

Output:
- `true`

Input:
- `2`

Output:
- `false`

What it tests:
- cycle detection using a visited set

---

### 8. Single Number
Find the element that appears only once (all others appear twice).

Input:
- `[4, 1, 2, 1, 2]`

Output:
- `4`

Approaches:
- XOR: O(1) space
- Set toggle: O(n) space

What it tests:
- set toggle or XOR cancellation

---

### 9. Two Sum (using set)
Find if any two elements sum to the target.

Input:
- `[2, 7, 11, 15]`, target = `9`

Output:
- `true`  (2 + 7 = 9)

What it tests:
- complement lookup in a set

---

### 10. Jewels and Stones
Count how many stones are jewels.

Input:
- `jewels = "aA"`, `stones = "aAAbbbb"`

Output:
- `3`

What it tests:
- membership testing with a character set

---

### 11. Distribute Candies
Given candy types, a person can eat n/2 candies. Maximize the variety.

Input:
- `[1, 1, 2, 2, 3, 3]`

Output:
- `3`

Input:
- `[1, 1, 2, 3]`

Output:
- `2`

What it tests:
- min(distinct types, n/2)

---

### 12. Unique Email Addresses
Count unique email addresses after applying Gmail-style rules (dots before @, + prefix).

Input:
- `["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]`

Output:
- `2`

What it tests:
- string normalization then set deduplication

---

### 13. Uncommon Words from Two Sentences
Return words that appear exactly once in one sentence and not in the other.

Input:
- `s1 = "this apple is sweet"`, `s2 = "this apple is sour"`

Output:
- `["sweet", "sour"]`

What it tests:
- word frequency counting then uniqueness filter

---

### 14. Set Mismatch
Find the number that appears twice and the number that is missing.

Input:
- `[1, 2, 2, 4]`

Output:
- `[2, 3]`

What it tests:
- set difference against expected range

---

### 15. Find All Duplicates in an Array
Return all elements that appear exactly twice.

Input:
- `[4, 3, 2, 7, 8, 2, 3, 1]`

Output:
- `[2, 3]`

Approaches:
- Set: O(n) space
- In-place sign marking: O(1) space

What it tests:
- in-place duplicate detection

---

### 16. First Missing Positive
Find the smallest missing positive integer.

Input:
- `[3, 4, -1, 1]`

Output:
- `2`

Input:
- `[1, 2, 0]`

Output:
- `3`

Approaches:
- Set: O(n) space — add all to set, scan from 1
- In-place bucket sort: O(1) space

What it tests:
- set membership scan
- placing numbers in their natural index

---

### 17. Valid Sudoku
Check if a 9×9 board is valid using row, column, and box sets.

Input:
- 9×9 board with some cells filled

Output:
- `true` or `false`

What it tests:
- three separate set groups for rows, columns, and 3×3 boxes

---

### 18. Word Pattern
Check whether a string follows the same pattern as a given pattern string.

Input:
- `pattern = "abba"`, `s = "dog cat cat dog"`

Output:
- `true`

Input:
- `pattern = "abba"`, `s = "dog cat cat fish"`

Output:
- `false`

What it tests:
- bijection checking using two maps / sets

---

### 19. Isomorphic Strings
Check if two strings have the same character-mapping structure.

Input:
- `s = "egg"`, `t = "add"`

Output:
- `true`

Input:
- `s = "foo"`, `t = "bar"`

Output:
- `false`

What it tests:
- bijection checking with two maps

---

### 20. Palindrome Permutation
Check if any permutation of a string is a palindrome.

Input:
- `"tactcoa"`

Output:
- `true`  (can form "tacocat")

What it tests:
- at most one character can have an odd frequency

---

### 21. Group Anagrams (using frozenset / sorted key)
Group strings that are anagrams of each other.

Input:
- `["eat","tea","tan","ate","nat","bat"]`

Output:
- `[["eat","tea","ate"],["tan","nat"],["bat"]]`

What it tests:
- hash map with normalized set key

---

### 22. Repeated DNA Sequences
Find all 10-letter-long DNA substrings that appear more than once.

Input:
- `"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"`

Output:
- `["AAAAACCCCC","CCCCCAAAAA"]`

What it tests:
- sliding window with a seen set and a repeated set

---

### 23. Brick Wall
Find the row where the fewest bricks are crossed. Track edge positions using a set/map.

Input:
- `[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]`

Output:
- `2`

What it tests:
- frequency map of edge positions (exclude last edge of each row)

---

### 24. Minimum Number of Steps to Make Two Strings Anagram
Count minimum character swaps to make s an anagram of t.

Input:
- `s = "bab"`, `t = "aba"`

Output:
- `1`

What it tests:
- character frequency difference

---

### 25. Longest Substring Without Repeating Characters (Set approach)
Find the longest substring with all unique characters.

Input:
- `"abcabcbb"`

Output:
- `3`

What it tests:
- sliding window using a character set for uniqueness tracking

---

### 26. Find Duplicate File in System
Group file paths by their content.

Input:
- `["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]`

Output:
- `[["root/a/1.txt","root/c/3.txt"],["root/a/2.txt","root/c/d/4.txt","root/4.txt"]]`

What it tests:
- hash map keyed by content string

---

### 27. Minimum Index Sum of Two Lists
Find common restaurant preferred most by two friends (minimum index sum).

Input:
- `list1=["Shogun","Tapioca Express","Burger King","KFC"]`
- `list2=["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]`

Output:
- `["Shogun"]`

What it tests:
- hash map for index lookup then set intersection

---

### 28. Kth Largest Element in a Stream (Set/Heap)
Design a class that finds the kth largest element in a stream.

Input:
- `k=3`, initial `[4,5,8,2]`
- Add `3` → return `4`
- Add `5` → return `5`

What it tests:
- min-heap of size k (keep largest k elements)

---

### 29. Top K Frequent Elements
Return the k most frequent elements.

Input:
- `[1,1,1,2,2,3]`, k=2

Output:
- `[1,2]`

What it tests:
- frequency map + heap or bucket sort

---

### 30. Subarray Sum Divisible by K
Count subarrays whose sum is divisible by k.

Input:
- `nums=[4,5,0,-2,-3,1]`, `k=5`

Output:
- `7`

What it tests:
- prefix sum mod k stored in a set/map

---

## Best Study Order

1. Contains Duplicate
2. Single Number
3. Two Sum (set)
4. Jewels and Stones
5. Intersection of Two Arrays
6. Union of Two Arrays
7. Difference of Two Arrays
8. Happy Number
9. Contains Duplicate II
10. Distribute Candies
11. Palindrome Permutation
12. Isomorphic Strings
13. Word Pattern
14. Unique Email Addresses
15. Uncommon Words from Two Sentences
16. Set Mismatch
17. Find All Duplicates
18. First Missing Positive
19. Longest Consecutive Sequence
20. Longest Substring Without Repeating Characters
21. Group Anagrams
22. Repeated DNA Sequences
23. Valid Sudoku
24. Minimum Anagram Steps
25. Brick Wall
26. Find Duplicate File in System
27. Minimum Index Sum of Two Lists
28. Kth Largest in Stream
29. Top K Frequent Elements
30. Subarray Sum Divisible by K

---

## Debugging Pattern for Set Problems

1. Print the set contents after each insert/remove operation.
2. For sliding window sets, print what is added and removed at each step.
3. For two-map bijection problems, print both maps after each character.
4. For frequency problems, print the frequency map before filtering.
5. For consecutive sequence problems, print which numbers are sequence starts.
6. For prefix sum mod problems, print the running mod and map lookup at each step.

---

## Code Files

- `python/set_problems.py`
- `javascript/set_problems.js`
