# Complete DSA Program List

This file gives you a simple view of the DSA programs you should prepare for coding interviews.

## Already Created In This Folder

### Arrays and Hashing
- `Two Sum`: find two numbers that add up to a target.
  Example: `[2, 7, 11, 15]`, target `9` → `[0, 1]`
- `Product of Array Except Self`: build result using all numbers except the current one.
  Example: `[1, 2, 3, 4]` → `[24, 12, 8, 6]`
- `Top K Frequent Elements`: return the most repeated values from an array.
  Example: `[1, 1, 1, 2, 2, 3]`, k=2 → `[1, 2]`

Files:
- `python/arrays_hashing.py`
- `javascript/arrays_hashing.js`

### Strings and Sliding Window
- `Valid Anagram`: check whether two strings contain the same letters.
  Example: `"listen"`, `"silent"` → `true`
- `Longest Substring Without Repeating Characters`: find the biggest unique-character substring.
  Example: `"abcabcbb"` → `3`
- `Minimum Window Substring`: find the smallest substring containing all needed characters.
  Example: `"ADOBECODEBANC"`, target `"ABC"` → `"BANC"`
- `Group Anagrams`: collect words that are made from the same letters.
  Example: `["eat","tea","tan","ate","nat","bat"]` → `[["eat","tea","ate"],["tan","nat"],["bat"]]`
- `Longest Palindromic Substring`: find the longest palindrome inside a string.
  Example: `"babad"` → `"bab"`
- `Valid Palindrome`: ignore symbols and check palindrome logic.
  Example: `"A man, a plan, a canal: Panama"` → `true`
- `Longest Common Prefix`: find the common starting part of many strings.
  Example: `["flower","flow","flight"]` → `"fl"`
- `Find All Anagrams in a String`: return all starting indices of anagram matches.
  Example: `"cbaebabacd"`, pattern `"abc"` → `[0, 6]`
- `Permutation in String`: check if one string permutation exists inside another.
  Example: `"ab"` in `"eidbaooo"` → `true`
- `Count Palindromic Substrings`: count all palindrome substrings.
  Example: `"aaa"` → `6`
- `Encode and Decode Strings`: convert list of strings safely to one string and back.
  Example: `["leet","code"]` → encoded `"4#leet4#code"` → decoded `["leet","code"]`
- `Longest Repeating Character Replacement`: expand a window while allowing at most k replacements.
  Example: `"AABABBA"`, k=1 → `4`
- `Zigzag Conversion`: place characters in zigzag rows and read row by row.
  Example: `"PAYPALISHIRING"`, rows=3 → `"PAHNAPLSIIGYIR"`
- `String to Integer (atoi)`: parse a string into an integer carefully.
  Example: `"   -42"` → `-42`
- `Implement strStr()`: find the first position of one string inside another.
  Example: `"sadbutsad"`, needle `"sad"` → `0`
- `Decode String`: decode nested repeated string patterns.
  Example: `"3[a2[c]]"` → `"accaccacc"`
- `Substring with Concatenation of All Words`: find all start positions where all words appear together.
  Example: `"barfoothefoobarman"`, words `["foo","bar"]` → `[0, 9]`

Files:
- `python/strings_sliding_window.py`
- `javascript/strings_sliding_window.js`

### Linked List
- `Reverse Linked List`: reverse node connections.
  Example: `1→2→3→4→5` → `5→4→3→2→1`
- `Merge Two Sorted Lists`: merge two sorted linked lists into one sorted list.
  Example: `1→3→5` and `2→4→6` → `1→2→3→4→5→6`
- `Linked List Cycle`: detect whether a list contains a loop.
  Example: list with tail pointing back to middle → `true`
- `Remove Nth Node From End`: remove the nth node from the end in one pass.
  Example: `1→2→3→4→5`, n=2 → `1→2→3→5`
- `Find Middle of Linked List`: return the middle node using fast/slow pointers.
  Example: `1→2→3→4→5` → node(3)
- `Palindrome Linked List`: check if list values form a palindrome.
  Example: `1→2→2→1` → `true`
- `Intersection of Two Linked Lists`: find the node where two lists share a reference.
  Example: A=`4→1→8→4→5`, B=`5→6→1→8→4→5` → node(8)
- `Add Two Numbers`: add two reversed-digit lists and return the result as a list.
  Example: `2→4→3` and `5→6→4` → `7→0→8` (342+465=807)
- `Reverse Linked List II`: reverse only from position left to right.
  Example: `1→2→3→4→5`, left=2, right=4 → `1→4→3→2→5`
- `Remove Duplicates (keep one)`: remove extra duplicates from a sorted list.
  Example: `1→1→2→3→3` → `1→2→3`
- `Remove All Duplicates`: delete every node whose value appears more than once.
  Example: `1→2→3→3→4→4→5` → `1→2→5`
- `Sort List`: sort a linked list using merge sort.
  Example: `4→2→1→3` → `1→2→3→4`
- `Rotate List`: rotate the list to the right by k positions.
  Example: `1→2→3→4→5`, k=2 → `4→5→1→2→3`
- `Copy List with Random Pointer`: deep clone a list with next and random pointers.
  Example: `[[7,null],[13,0]]` → identical deep copy
- `Reorder List`: interleave first and reversed second half in place.
  Example: `1→2→3→4→5` → `1→5→2→4→3`
- `Swap Nodes in Pairs`: swap every two adjacent nodes.
  Example: `1→2→3→4` → `2→1→4→3`
- `Remove Linked List Elements`: remove all nodes matching a value.
  Example: `1→2→6→3→6`, val=6 → `1→2→3`
- `Odd Even Linked List`: group odd-indexed then even-indexed nodes.
  Example: `1→2→3→4→5` → `1→3→5→2→4`
- `Partition List`: all values < x before values >= x, stable order.
  Example: `1→4→3→2→5→2`, x=3 → `1→2→2→4→3→5`
- `Merge K Sorted Lists`: merge k sorted lists into one.
  Example: `[1→4→5, 1→3→4, 2→6]` → `1→1→2→3→4→4→5→6`
- `Reverse Nodes in k-Group`: reverse every k nodes, leave remainder.
  Example: `1→2→3→4→5`, k=2 → `2→1→4→3→5`
- `Find the Duplicate Number`: find duplicate in n+1 integers using Floyd's.
  Example: `[1,3,4,2,2]` → `2`
- `Convert Binary Linked List to Integer`: binary number MSB-first to decimal.
  Example: `1→0→1` → `5`
- `LRU Cache`: O(1) get/put cache using doubly linked list + hash map.
  Example: capacity=2, put(1,1), put(2,2), get(1)→1, put(3,3), get(2)→-1
- `Linked List Components`: count connected components within a value subset.
  Example: `0→1→2→3`, nums=[0,1,3] → `2`

Files:
- `python/linked_list.py`
- `javascript/linked_list.js`
- `LINKED_LIST_PROBLEMS.md`

### Additional Tuple / Two-Pointer Problems (26–40)
- `Two Sum Less Than K`: max pair sum below k.
  Example: `[34,23,1,24,75,33,54,8]`, k=60 → `58`
- `Count Subarrays Product < K`: multiplicative sliding window.
  Example: `[10,5,2,6]`, k=100 → `8`
- `Max Consecutive Ones III`: max 1s run with k zero flips.
  Example: `[1,1,1,0,0,0,1,1,1,1,0]`, k=2 → `6`
- `Longest Subarray of 1s After Deleting One`: delete one element, max 1s run.
  Example: `[1,1,0,1]` → `3`
- `Fruit Into Baskets`: longest subarray with at most 2 distinct values.
  Example: `[1,2,3,2,2]` → `4`
- `Maximum Points from Cards`: pick k cards from either end, maximize sum.
  Example: `[1,2,3,4,5,6,1]`, k=3 → `12`
- `Longest Subarray Abs Diff ≤ Limit`: two deque sliding window.
  Example: `[10,1,2,4,7,2]`, limit=5 → `4`
- `Squares of Sorted Array`: sorted squares in O(n) with two pointers.
  Example: `[-4,-1,0,3,10]` → `[0,1,9,16,100]`
- `Min Difference Highest and Lowest K Scores`: sort + fixed window.
  Example: `[9,4,1,7]`, k=2 → `2`
- `Subarrays with Bounded Maximum`: count where max in [L,R].
  Example: `[2,1,4,3]`, L=2, R=3 → `3`
- `Find All Anagrams in String`: fixed-size window + char frequency.
  Example: `"cbaebabacd"`, p=`"abc"` → `[0,6]`
- `Partition Array Max Diff ≤ K`: greedy groups after sorting.
  Example: `[3,6,1,2,5]`, k=2 → `2`
- `Longest Turbulent Subarray`: alternating comparison pattern.
  Example: `[9,4,2,10,7,8,8,1,9]` → `5`
- `Maximum Erasure Value`: max sum subarray with all unique elements.
  Example: `[4,2,4,5,6]` → `17`
- `Max Sum Two Non-Overlapping Subarrays`: prefix sums + two-pass window.
  Example: `[0,6,5,2,2,5,1,9,4]`, L=1, M=2 → `20`

### Stack and Queue
- `Valid Parentheses`: check whether brackets are balanced correctly.
  Example: `"()[]{}"` → `true`, `"(]"` → `false`
- `Daily Temperatures`: find the next warmer day for each temperature.
  Example: `[73,74,75,71,69,72,76,73]` → `[1,1,4,2,1,1,0,0]`
- `Queue Using Stacks`: implement queue behavior with two stacks.
  Example: push 1, push 2, peek → `1`, pop → `1`

Files:
- `python/stack_queue.py`
- `javascript/stack_queue.js`

### Trees and Graphs
- `Binary Tree Level Order Traversal`: print tree nodes level by level.
  Example: tree `[3,9,20,null,null,15,7]` → `[[3],[9,20],[15,7]]`
- `Lowest Common Ancestor`: find the nearest common parent of two nodes.
  Example: LCA of nodes `5` and `1` in BST `[6,2,8,0,4,7,9]` → node `6`
- `Number of Islands`: count groups of connected land cells in a grid.
  Example: 3×4 grid with two separate land clusters → `2`

Files:
- `python/trees_graphs.py`
- `javascript/trees_graphs.js`

### Dynamic Programming
- `Climbing Stairs`: count how many ways you can reach the top.
  Example: `n=5` → `8`
- `Coin Change`: find the minimum number of coins for a target amount.
  Example: coins `[1,2,5]`, amount `11` → `3`
- `Longest Increasing Subsequence`: find the length of the longest increasing sequence.
  Example: `[10,9,2,5,3,7,101,18]` → `4`

Files:
- `python/dynamic_programming.py`
- `javascript/dynamic_programming.js`

### Number Problems
- `Palindrome Number`: check whether a number reads the same forward and backward.
  Example: `121` → `true`, `123` → `false`
- `Reverse Integer`: reverse digits carefully while handling sign.
  Example: `123` → `321`, `-456` → `-654`
- `Plus One`: add one to a number represented as digits.
  Example: `[1,2,9]` → `[1,3,0]`
- `Happy Number`: detect repeated digit-square sums.
  Example: `19` → `true`
- `Power of Two`: check whether a number is a valid power of two.
  Example: `16` → `true`, `18` → `false`
- `Sqrt(x)`: find integer square root using binary search.
  Example: `10` → `3`, `25` → `5`
- `Pow(x, n)`: compute power efficiently with fast exponentiation.
  Example: `2.0^10` → `1024.0`
- `GCD and LCM`: find greatest common divisor and least common multiple.
  Example: `12, 18` → GCD `6`, LCM `36`
- `Prime Check and Count Primes`: work with prime-number basics and sieve.
  Example: `countPrimes(10)` → `4`
- `Prime Factorization`: break a number into prime factors.
  Example: `84` → `[2, 2, 3, 7]`
- `Missing Number`: find the missing value from a range.
  Example: `[3,0,1]` → `2`
- `Single Number`: find the non-repeated value using xor.
  Example: `[4,1,2,1,2]` → `4`
- `Add Digits`: keep reducing a number to one digit.
  Example: `38` → `2`
- `Number of 1 Bits`: count set bits in binary form.
  Example: `11` (binary 1011) → `3`
- `Hamming Distance`: count differing bits between two numbers.
  Example: `1, 4` → `2`
- `Power of Three`: check whether a number is `3^k`.
  Example: `27` → `true`, `45` → `false`
- `Perfect Number`: compare a number with sum of its divisors.
  Example: `28` → `true` (1+2+4+7+14 = 28)
- `Ugly Number`: check whether factors are only 2, 3, and 5.
  Example: `6` → `true`, `14` → `false`
- `Divide Two Integers`: build division result using shifts and subtraction.
  Example: `10 ÷ 3` → `3`
- `Fibonacci Number`: compute the nth Fibonacci value.
  Example: `n=6` → `8`
- `Roman to Integer`: convert Roman numeral text into number.
  Example: `"MCMXCIV"` → `1994`
- `Integer to Roman`: convert number into Roman numeral text.
  Example: `1994` → `"MCMXCIV"`
- `Counting Bits`: return set-bit counts from 0 to n.
  Example: `5` → `[0,1,1,2,1,2]`
- `Reverse Bits`: reverse binary bits of a number.
  Example: `43261596` → `964176192`
- `Sum of Two Integers`: add numbers using bit operations.
  Example: `1 + 2` → `3`
- `Power of Four`: check whether a number is `4^k`.
  Example: `16` → `true`, `5` → `false`
- `Number of Steps to Reduce to Zero`: count operations to reach zero.
  Example: `14` → `6`
- `Excel Sheet Column Number`: convert column name to numeric index.
  Example: `"AB"` → `28`
- `Fraction to Recurring Decimal`: detect repeating decimal parts.
  Example: `1/3` → `"0.(3)"`

Files:
- `python/number_problems.py`
- `javascript/number_problems.js`

### Tuple and Two-Pointer Problems
- `Two Sum II (Sorted)`: two pointers from both ends on sorted array.
  Example: `[2,7,11,15]`, target=9 → `[1,2]`
- `3Sum`: fix one element, two pointers for unique triplets summing to zero.
  Example: `[-1,0,1,2,-1,-4]` → `[[-1,-1,2],[-1,0,1]]`
- `3Sum Closest`: find triplet sum nearest to a target.
  Example: `[-1,2,1,-4]`, target=1 → `2`
- `4Sum`: all unique quadruplets summing to target.
  Example: `[1,0,-1,0,-2,2]`, target=0 → `[[-2,-1,1,2],...]`
- `Count Pairs with Given Sum`: count pairs summing to target.
  Example: `[1,5,7,-1,5]`, target=6 → `3`
- `Subarray with Given Sum`: find subarray indices summing to target (positives).
  Example: `[1,4,20,3,10,5]`, target=33 → `[2,4]`
- `Subarray Sum Equals K`: count subarrays summing to k (can have negatives).
  Example: `[1,1,1]`, k=2 → `2`
- `Container with Most Water`: two pointers to maximize trapped area.
  Example: `[1,8,6,2,5,4,8,3,7]` → `49`
- `Trapping Rain Water`: water trapped between walls.
  Example: `[0,1,0,2,1,0,1,3,2,1,2,1]` → `6`
- `Boats to Save People`: greedy two-pointer pairing.
  Example: `[1,2,2,3]`, limit=3 → `3`
- `Valid Triangle Number`: count triplets forming valid triangles.
  Example: `[2,2,3,4]` → `3`
- `Minimum Size Subarray Sum`: smallest subarray with sum >= target.
  Example: `[2,3,1,2,4,3]`, target=7 → `2`
- `Sort Colors`: sort 0s, 1s, 2s in one pass (Dutch flag).
  Example: `[2,0,2,1,1,0]` → `[0,0,1,1,2,2]`
- `Move Zeros`: move zeros to end preserving order.
  Example: `[0,1,0,3,12]` → `[1,3,12,0,0]`
- `Remove Duplicates (keep one)`: unique elements in place.
  Example: `[1,1,2,3,3]` → `3`
- `Remove Duplicates II (allow 2)`: each element at most twice.
  Example: `[1,1,1,2,2,3]` → `5`
- `Merge Intervals`: merge overlapping intervals.
  Example: `[[1,3],[2,6],[8,10]]` → `[[1,6],[8,10]]`
- `Insert Interval`: insert and merge into sorted intervals.
  Example: `[[1,3],[6,9]]`, new=`[2,5]` → `[[1,5],[6,9]]`
- `Non-Overlapping Intervals`: min removals so no overlap.
  Example: `[[1,2],[2,3],[3,4],[1,3]]` → `1`
- `Meeting Rooms`: can attend all meetings?
  Example: `[[0,30],[5,10],[15,20]]` → `false`
- `Meeting Rooms II`: minimum rooms needed.
  Example: `[[0,30],[5,10],[15,20]]` → `2`
- `K-diff Pairs`: count unique pairs with absolute difference = k.
  Example: `[3,1,4,1,5]`, k=2 → `2`
- `Longest Mountain in Array`: longest subarray that rises then falls.
  Example: `[2,1,4,7,3,2,5]` → `5`

Files:
- `python/tuple_problems.py`
- `javascript/tuple_problems.js`
- `TUPLE_PROBLEMS.md`

### Set and HashSet Problems
- `Contains Duplicate`: any duplicate in array?
  Example: `[1,2,3,1]` → `true`
- `Contains Duplicate II`: duplicates within k indices?
  Example: `[1,2,3,1]`, k=3 → `true`
- `Intersection of Two Arrays`: unique common elements.
  Example: `[1,2,2,1]`, `[2,2]` → `[2]`
- `Union of Two Arrays`: all unique combined elements.
  Example: `[1,2,3]`, `[2,3,4,5]` → `[1,2,3,4,5]`
- `Difference of Two Arrays`: elements only in each.
  Example: `[1,2,3]`, `[2,4,6]` → `[[1,3],[4,6]]`
- `Longest Consecutive Sequence`: longest run of consecutive integers.
  Example: `[100,4,200,1,3,2]` → `4`
- `Happy Number`: cycle detection via set.
  Example: `19` → `true`
- `Single Number`: find the non-repeated element.
  Example: `[4,1,2,1,2]` → `4`
- `Two Sum (set)`: any two elements summing to target?
  Example: `[2,7,11,15]`, target=9 → `true`
- `Jewels and Stones`: count stones that are jewels.
  Example: jewels=`"aA"`, stones=`"aAAbbbb"` → `3`
- `Distribute Candies`: maximize candy variety.
  Example: `[1,1,2,2,3,3]` → `3`
- `Unique Email Addresses`: count distinct normalized emails.
  Example: `["test.email+alex@leetcode.com","test.e.mail+bob@leetcode.com","testemail+david@lee.tcode.com"]` → `2`
- `Uncommon Words from Two Sentences`: words appearing exactly once total.
  Example: `"this apple is sweet"`, `"this apple is sour"` → `["sweet","sour"]`
- `Set Mismatch`: find duplicate and missing number.
  Example: `[1,2,2,4]` → `[2,3]`
- `Find All Duplicates in Array`: elements appearing exactly twice.
  Example: `[4,3,2,7,8,2,3,1]` → `[2,3]`
- `First Missing Positive`: smallest missing positive integer.
  Example: `[3,4,-1,1]` → `2`
- `Valid Sudoku`: validate board using row/col/box sets.
  Example: valid 9×9 board → `true`
- `Word Pattern`: check bijection between pattern and words.
  Example: pattern=`"abba"`, s=`"dog cat cat dog"` → `true`
- `Isomorphic Strings`: same character-mapping structure.
  Example: `"egg"`, `"add"` → `true`
- `Palindrome Permutation`: can form a palindrome?
  Example: `"tactcoa"` → `true`
- `Group Anagrams`: cluster anagram strings together.
  Example: `["eat","tea","tan","ate","nat","bat"]` → `[["eat","tea","ate"],["tan","nat"],["bat"]]`
- `Repeated DNA Sequences`: 10-char substrings appearing more than once.
  Example: `"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"` → `["AAAAACCCCC","CCCCCAAAAA"]`
- `Brick Wall`: fewest bricks crossed by a vertical line.
  Example: 6-row wall → `2`
- `Minimum Steps to Make Anagram`: chars to change to make t an anagram of s.
  Example: `"bab"`, `"aba"` → `1`
- `Longest Substring Without Repeating Characters`: set-based sliding window.
  Example: `"abcabcbb"` → `3`
- `Find Duplicate File in System`: group files by content.
  Example: `["root/a 1.txt(abcd)", "root/c 3.txt(abcd)"]` → `[["root/a/1.txt","root/c/3.txt"]]`
- `Minimum Index Sum of Two Lists`: common item with lowest index sum.
  Example: list1+list2 with "Shogun" common → `["Shogun"]`
- `Kth Largest in Stream`: min-heap of size k.
  Example: k=3, init=[4,5,8,2], add(3) → `4`
- `Top K Frequent Elements`: bucket sort by frequency.
  Example: `[1,1,1,2,2,3]`, k=2 → `[1,2]`
- `Subarray Sum Divisible by K`: prefix mod + map.
  Example: `[4,5,0,-2,-3,1]`, k=5 → `7`

Files:
- `python/set_problems.py`
- `javascript/set_problems.js`
- `SET_PROBLEMS.md`

## Complete Interview Program Roadmap

Use this list as your master preparation checklist.

### Arrays
- `Two Sum`: hash map lookup practice.
- `Best Time to Buy and Sell Stock`: keep track of the best profit.
- `Contains Duplicate`: fast duplicate detection using a set.
- `Product of Array Except Self`: prefix and suffix product logic.
- `Maximum Subarray`: Kadane's algorithm for best continuous sum.

### Strings
- `Valid Anagram`: frequency counting.
- `Group Anagrams`: classify strings by normalized key.
- `Longest Substring Without Repeating Characters`: sliding window basics.
- `Longest Palindromic Substring`: expand around center or DP.
- `Minimum Window Substring`: advanced sliding window.
- `Valid Palindrome`: two-pointer filtering of letters and digits.
- `Longest Common Prefix`: prefix comparison across many strings.
- `Find All Anagrams in a String`: fixed-size sliding window plus counts.
- `Permutation in String`: window matching against target frequency.
- `Count Palindromic Substrings`: expand around centers.
- `Encode and Decode Strings`: safe string serialization pattern.
- `Longest Repeating Character Replacement`: window size versus most frequent character.
- `Zigzag Conversion`: row simulation.
- `String to Integer (atoi)`: robust parsing.
- `Implement strStr()`: substring search pattern.
- `Decode String`: stack-based nested pattern decoding.
- `Substring with Concatenation of All Words`: fixed-length chunk windowing.

### Linked List
- `Reverse Linked List`: pointer manipulation.
- `Merge Two Sorted Lists`: sorted merge logic.
- `Remove Nth Node From End`: two pointers.
- `Linked List Cycle`: fast and slow pointer.
- `Reorder List`: split, reverse, merge.

### Stack
- `Valid Parentheses`: stack basics.
- `Min Stack`: track minimum efficiently.
- `Daily Temperatures`: monotonic stack.
- `Largest Rectangle in Histogram`: advanced stack pattern.
- `Evaluate Reverse Polish Notation`: operator stack processing.

### Queue / Heap
- `Implement Queue Using Stacks`: queue behavior design.
- `Kth Largest Element`: heap usage.
- `Top K Frequent Elements`: heap plus frequency map.
- `Task Scheduler`: priority-based greedy logic.
- `Merge K Sorted Lists`: heap-based merging.

### Binary Search
- `Binary Search`: base search pattern.
- `Search in Rotated Sorted Array`: identify sorted half.
- `Find Minimum in Rotated Sorted Array`: binary search variant.
- `Search a 2D Matrix`: flatten thinking with binary search.
- `Median of Two Sorted Arrays`: advanced partition logic.

### Trees
- `Maximum Depth of Binary Tree`: DFS or BFS depth computation.
- `Same Tree`: recursive structure comparison.
- `Invert Binary Tree`: swap left and right children.
- `Level Order Traversal`: BFS by level.
- `Lowest Common Ancestor`: tree recursion.

### Graphs
- `Number of Islands`: DFS or BFS on grid.
- `Clone Graph`: graph traversal plus map.
- `Course Schedule`: cycle detection in directed graph.
- `Pacific Atlantic Water Flow`: reverse graph thinking on matrix.
- `Word Ladder`: shortest path through transformations.

### Backtracking
- `Subsets`: generate all subsets.
- `Permutations`: generate all orderings.
- `Combination Sum`: choose numbers to reach target.
- `Palindrome Partitioning`: partition string into palindromes.
- `N Queens`: classic constraint placement problem.

### Dynamic Programming
- `Climbing Stairs`: beginner DP.
- `House Robber`: include or exclude pattern.
- `Coin Change`: minimum state transition.
- `Longest Increasing Subsequence`: sequence DP.
- `Edit Distance`: string transformation DP.

### Greedy
- `Jump Game`: reachability logic.
- `Gas Station`: restart when tank becomes negative.
- `Merge Intervals`: interval sorting and merging.
- `Partition Labels`: segment greedily.
- `Non-overlapping Intervals`: remove minimum overlaps.

### Intervals
- `Insert Interval`: place and merge a new interval.
- `Merge Intervals`: combine overlaps.
- `Meeting Rooms`: check overlap conflicts.
- `Meeting Rooms II`: count rooms needed.
- `Employee Free Time`: merge busy schedules.

### Bit Manipulation
- `Single Number`: xor trick.
- `Number of 1 Bits`: bit counting.
- `Counting Bits`: reuse previous bit results.
- `Reverse Bits`: shift and build reversed number.
- `Sum of Two Integers`: add without using plus.

### Trie
- `Implement Trie`: prefix tree basics.
- `Word Search II`: trie plus DFS.
- `Replace Words`: fast prefix replacement.

### Number / Math
- `Palindrome Number`: digit reversal logic.
- `Reverse Integer`: overflow-safe digit extraction.
- `Plus One`: carry handling.
- `Happy Number`: cycle detection on number transformation.
- `Power of Two`: division or bitwise check.
- `Sqrt(x)`: binary search on answer space.
- `Pow(x, n)`: exponentiation by squaring.
- `Count Primes`: sieve of Eratosthenes.
- `GCD and LCM`: Euclidean algorithm.
- `Prime Factorization`: repeated division by smallest factors.
- `Missing Number`: sum formula or xor.
- `Single Number`: xor cancellation.
- `Add Digits`: digit root pattern.
- `Number of 1 Bits`: bit count in binary representation.
- `Hamming Distance`: xor plus set-bit count.
- `Power of Three`: repeated division pattern.
- `Perfect Number`: sum of proper divisors.
- `Ugly Number`: repeated factor stripping.
- `Divide Two Integers`: doubling and bit-shift quotient building.
- `Fibonacci Number`: classic recurrence and DP.
- `Roman to Integer`: symbol parsing with subtractive cases.
- `Integer to Roman`: greedy symbol building.
- `Counting Bits`: dp using previous half values.
- `Reverse Bits`: repeated bit shifting.
- `Sum of Two Integers`: xor plus carry.
- `Power of Four`: stronger power validation than power of two.
- `Number of Steps to Reduce to Zero`: branch logic with even/odd.
- `Excel Sheet Column Number`: alphabet-to-number conversion.
- `Fraction to Recurring Decimal`: remainder cycle detection.

## Best Order For Experienced Developers

If you are already working as a Python developer, prepare in this order:

1. Arrays and hashing
2. Strings and sliding window
3. Linked list and two pointers
4. Stack, queue, heap
5. Trees and graphs
6. Dynamic programming
7. Backtracking
8. Intervals and greedy
9. Trie and bit manipulation

---

### Dictionary and HashMap Problems
File: `python/dictionary_problems.py` | `javascript/dictionary_problems.js`
Guide: `DICTIONARY_PROBLEMS.md`

| # | Problem | Input | Output |
|---|---------|-------|--------|
| 1 | Two Sum | `[2,7,11,15]`, target=9 | `[0,1]` |
| 2 | Valid Anagram | `"anagram"`, `"nagaram"` | `true` |
| 3 | Ransom Note | `"aa"`, `"aab"` | `true` |
| 4 | Word Frequency Count | `"the cat sat on the mat"` | `{the:2,cat:1,...}` |
| 5 | First Unique Character | `"leetcode"` | `0` |
| 6 | Top K Frequent Words | `["i","love","i","love","coding"]`, k=2 | `["i","love"]` |
| 7 | Majority Element | `[3,2,3]` | `3` |
| 8 | Majority Element II | `[1,1,1,3,3,2,2,2]` | `[1,2]` |
| 9 | Two Sum III (Data Structure) | add(1),add(3),find(4) | `true` |
| 10 | Subarray Sum Equals K | `[1,1,1]`, k=2 | `2` |
| 11 | Longest Subarray with Sum K | `[1,-1,5,-2,3]`, k=3 | `4` |
| 12 | Binary Subarrays with Sum | `[1,0,1,0,1]`, goal=2 | `4` |
| 13 | Contiguous Array (equal 0s/1s) | `[0,1,0,0,1,1,0]` | `6` |
| 14 | Word Count Engine | `"practice makes perfect..."` | sorted by freq |
| 15 | LRU Cache | capacity=2, put/get ops | O(1) ops |
| 16 | LFU Cache | capacity=2, put/get ops | O(1) ops |
| 17 | Group Shifted Strings | `["abc","bcd","xyz"]` | grouped |
| 18 | Find All Anagrams in a String | `s="cbaebabacd"`, p="abc" | `[0,6]` |
| 19 | Minimum Window Substring | `"ADOBECODEBANC"`, `"ABC"` | `"BANC"` |
| 20 | Longest Repeating Char Replacement | `"AABABBA"`, k=1 | `4` |
| 21 | Decode String | `"3[a2[c]]"` | `"accaccacc"` |
| 22 | Evaluate Division | equations + values + queries | ratios |
| 23 | Task Scheduler | `["A","A","A","B","B","B"]`, n=2 | `8` |
| 24 | Reorganize String | `"aab"` | `"aba"` |
| 25 | Hand of Straights | `[1,2,3,6,2,3,4,7,8]`, size=3 | `true` |
| 26 | Frequency of Most Frequent Element | `[1,2,4]`, k=5 | `3` |
| 27 | Custom Sort String | order=`"cba"`, s=`"abcd"` | `"cbad"` |
| 28 | Number of Atoms | `"Mg(OH)2"` | `"H2MgO2"` |
| 29 | Subarray Sum Divisible by K | `[4,5,0,-2,-3,1]`, k=5 | `7` |
| 30 | Brick Wall | rows of brick widths | min crossings |

---

## How To Study Each Program

For every problem:

1. Understand the brute-force approach first.
2. Write the optimized approach.
3. Note time and space complexity.
4. Dry run with a small example.
5. Debug step by step:
   print pointers, indices, maps, stack, queue, or dp state.
6. Explain why the optimized solution is better.

## Suggested Next Step

If you want, the next upgrade I can do is:

- add all remaining roadmap programs as code files
- create one file per individual problem
- add test cases and sample input/output for each program
