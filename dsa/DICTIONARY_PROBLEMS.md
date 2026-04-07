# Dictionary and HashMap DSA Problems

This file covers all common interview problems that use **Dictionary**, **HashMap**, or **Counter** as the core data structure.

Dictionaries are tested because they provide:
- O(1) average insert, lookup, delete
- Frequency counting
- Index mapping
- Grouping / bucketing
- Memoization
- Graph adjacency representation
- Prefix / suffix sum tracking

---

## Core Dictionary Problems

### 1. Two Sum
Return indices of two numbers that sum to target.

Input:
- `nums = [2, 7, 11, 15]`, target = 9

Output:
- `[0, 1]`

What it tests:
- complement lookup in a dictionary

---

### 2. Valid Anagram
Check if two strings contain the same characters with the same frequencies.

Input:
- `s = "anagram"`, `t = "nagaram"`

Output:
- `true`

What it tests:
- character frequency counting using Counter

---

### 3. Ransom Note
Check if a ransom note can be built from characters in a magazine.

Input:
- `ransomNote = "aa"`, `magazine = "aab"`

Output:
- `true`

What it tests:
- frequency subtraction between two maps

---

### 4. Word Frequency Count
Count how many times each word appears in a text.

Input:
- `"the cat sat on the mat"`

Output:
- `{"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}`

What it tests:
- basic frequency map building

---

### 5. First Unique Character in a String
Return the index of the first character that appears only once.

Input:
- `"leetcode"`

Output:
- `0`

Input:
- `"aabb"`

Output:
- `-1`

What it tests:
- frequency map then linear scan

---

### 6. Top K Frequent Words
Return the k most frequent words, sorted by frequency then lexicographically.

Input:
- `words = ["i","love","leetcode","i","love","coding"]`, k = 2

Output:
- `["i","love"]`

What it tests:
- frequency map + custom sort

---

### 7. Majority Element
Find the element that appears more than n/2 times.

Input:
- `[3, 2, 3]`

Output:
- `3`

Approaches:
- Counter: O(n) space
- Boyer-Moore voting: O(1) space

What it tests:
- majority frequency from a map

---

### 8. Majority Element II
Find all elements appearing more than n/3 times.

Input:
- `[3, 2, 3]`

Output:
- `[3]`

Input:
- `[1, 1, 1, 3, 3, 2, 2, 2]`

Output:
- `[1, 2]`

What it tests:
- at most 2 candidates can appear > n/3 times

---

### 9. Two Sum III – Data Structure Design
Design a class that supports add and find (pair summing to value).

Example:
- `add(1)`, `add(3)`, `add(5)`, `find(4)` → `true` (1+3=4)
- `find(7)` → `false`

What it tests:
- dictionary-based two-sum lookup over dynamic stream

---

### 10. Subarray Sum Equals K
Count subarrays whose sum equals k.

Input:
- `nums = [1, 1, 1]`, k = 2

Output:
- `2`

What it tests:
- prefix sum + frequency map

---

### 11. Longest Subarray with Sum K
Find the length of the longest subarray that sums to k.

Input:
- `nums = [1, -1, 5, -2, 3]`, k = 3

Output:
- `4`

What it tests:
- prefix sum map storing first occurrence index

---

### 12. Binary Subarrays with Sum
Count subarrays of 0s and 1s with a sum equal to goal.

Input:
- `nums = [1, 0, 1, 0, 1]`, goal = 2

Output:
- `4`

What it tests:
- prefix sum map on binary array

---

### 13. Contiguous Array
Find the longest subarray with equal numbers of 0s and 1s.

Input:
- `[0, 1, 0, 0, 1, 1, 0]`

Output:
- `6`

What it tests:
- transform 0 → -1 then use prefix sum map for balance

---

### 14. Word Count Engine
Count word occurrences and return sorted by frequency.

Input:
- `"practice makes perfect and perfect practice makes perfect"`

Output:
- `[["perfect","3"],["practice","2"],["makes","2"],["and","1"]]`

What it tests:
- frequency map + stable sort

---

### 15. LRU Cache
Design a cache with O(1) get and put using dict + doubly linked list.

Example:
- capacity=2, put(1,1), put(2,2), get(1)→1, put(3,3) evicts 2, get(2)→-1

What it tests:
- OrderedDict or manual linked list + dict

---

### 16. LFU Cache
Design a cache that evicts the least frequently used item.

Example:
- capacity=2, put(1,1), put(2,2), get(1)→1, put(3,3) evicts 2, get(2)→-1

What it tests:
- multiple dicts: key→value, key→freq, freq→OrderedDict of keys

---

### 17. Group Shifted Strings
Group strings that belong to the same shift sequence.

Input:
- `["abc","bcd","acef","xyz","az","ba","a","z"]`

Output:
- `[["abc","bcd","xyz"],["az","ba"],["acef"],["a","z"]]`

What it tests:
- normalize shift pattern as dict key

---

### 18. Find All Anagrams in a String
Return starting indices of all anagrams of p in s.

Input:
- `s = "cbaebabacd"`, `p = "abc"`

Output:
- `[0, 6]`

What it tests:
- sliding window frequency map comparison

---

### 19. Minimum Window Substring
Find the smallest window in s that contains all chars of t.

Input:
- `s = "ADOBECODEBANC"`, `t = "ABC"`

Output:
- `"BANC"`

What it tests:
- two-pointer + frequency map with need/have counters

---

### 20. Longest Repeating Character Replacement
Longest substring you can make uniform after at most k replacements.

Input:
- `s = "AABABBA"`, k = 1

Output:
- `4`

What it tests:
- frequency map inside a sliding window + max-frequency tracking

---

### 21. Decode String
Decode nested patterns like `3[a2[c]]`.

Input:
- `"3[a2[c]]"`

Output:
- `"accaccacc"`

What it tests:
- stack + current string building

---

### 22. Evaluate Division
Given equation ratios, answer queries about derived ratios.

Input:
- `equations=[["a","b"],["b","c"]]`, values=[2.0,3.0], queries=[["a","c"],["b","a"]]`

Output:
- `[6.0, 0.5]`

What it tests:
- adjacency dict + DFS/BFS for path product

---

### 23. Word Pattern II (backtracking with dict)
Check if a pattern can map to words in a string (each char maps to a unique word).

Input:
- `pattern = "aabb"`, `s = "dogdogcatcat"`

Output:
- `true`

What it tests:
- bijection backtracking with char→word and word→char maps

---

### 24. Number of Atoms
Parse a chemical formula and return element counts in sorted order.

Input:
- `"H2O"`

Output:
- `"H2O"`

Input:
- `"Mg(OH)2"`

Output:
- `"H2MgO2"`

What it tests:
- stack + dict for nested formula parsing

---

### 25. Brick Wall
Draw a vertical line crossing the fewest bricks.

Input:
- `[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]`

Output:
- `2`

What it tests:
- edge position frequency map

---

### 26. Task Scheduler
Return minimum time to execute all tasks with a cooldown n.

Input:
- `tasks = ["A","A","A","B","B","B"]`, n = 2

Output:
- `8`

What it tests:
- frequency map + greedy slot filling

---

### 27. Reorganize String
Rearrange so no two adjacent characters are the same.

Input:
- `"aab"`

Output:
- `"aba"`

Input:
- `"aaab"`

Output:
- `""`  (not possible)

What it tests:
- frequency map + max-heap interleaving

---

### 28. Hand of Straights
Determine if cards can be grouped into sets of consecutive values of size groupSize.

Input:
- `hand = [1,2,3,6,2,3,4,7,8]`, groupSize = 3

Output:
- `true`

What it tests:
- sorted key iteration on frequency map

---

### 29. Frequency of Most Frequent Element
Find the maximum frequency reachable for any element after at most k increments.

Input:
- `nums = [1, 2, 4]`, k = 5

Output:
- `3`

What it tests:
- sorting + sliding window with increment budget tracking

---

### 30. Custom Sort String
Sort string s according to the order defined by string order.

Input:
- `order = "cba"`, `s = "abcd"`

Output:
- `"cbad"`

What it tests:
- frequency map + priority-ordered reconstruction

---

## Best Study Order

1. Two Sum
2. Valid Anagram
3. Word Frequency Count
4. First Unique Character
5. Ransom Note
6. Majority Element
7. Majority Element II
8. Top K Frequent Words
9. Subarray Sum Equals K
10. Longest Subarray with Sum K
11. Binary Subarrays with Sum
12. Contiguous Array
13. Group Anagrams (shifted)
14. Find All Anagrams in String
15. Minimum Window Substring
16. Longest Repeating Character Replacement
17. Two Sum III – Data Structure
18. Custom Sort String
19. Task Scheduler
20. Reorganize String
21. Hand of Straights
22. Frequency of Most Frequent Element
23. LRU Cache
24. LFU Cache
25. Word Count Engine
26. Decode String
27. Evaluate Division
28. Number of Atoms
29. Word Pattern II
30. Brick Wall

---

## Debugging Pattern for Dictionary Problems

1. Print the dictionary after each insert/update to track state.
2. For prefix sum problems, print the running sum and map lookup at each step.
3. For sliding window problems, print the window frequency map after each shrink/expand.
4. For LRU/LFU, print cache contents and eviction decisions after each operation.
5. For grouping problems, print the normalized key used for grouping each element.
6. For graph problems, print the adjacency dict before traversal.

---

## Code Files

- `python/dictionary_problems.py`
- `javascript/dictionary_problems.js`
