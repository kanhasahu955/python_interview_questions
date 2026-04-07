# Tuple and Two-Pointer DSA Problems

This file covers all common interview problems that return tuples (pairs, triplets, quadruplets)
or that use two-pointer / multi-pointer techniques on sorted arrays and intervals.

These problems test:

- two-pointer traversal on sorted arrays
- avoiding duplicates in combination results
- reducing time from O(n³) or O(n²) to O(n²) or O(n)
- coordinate pair and interval manipulation
- sliding window with pair tracking

---

## Core Tuple and Two-Pointer Problems

### 1. Two Sum
Find two indices whose values sum to target.

Input:
- `nums = [2, 7, 11, 15]`, `target = 9`

Output:
- `[0, 1]`

Approaches:
- Brute force: O(n²) time, O(1) space
- Hash map: O(n) time, O(n) space

What it tests:
- hash map complement lookup

---

### 2. Two Sum II – Input Array Is Sorted
Array is already sorted. Return 1-indexed result.

Input:
- `numbers = [2, 7, 11, 15]`, `target = 9`

Output:
- `[1, 2]`

Approach:
- Two pointers: left at start, right at end
- Move left up if sum is too small, right down if too large

What it tests:
- two-pointer on sorted array

---

### 3. 3Sum
Find all unique triplets that sum to zero.

Input:
- `[-1, 0, 1, 2, -1, -4]`

Output:
- `[[-1, -1, 2], [-1, 0, 1]]`

Approach:
- Sort array
- Fix one element, use two pointers for the remaining pair
- Skip duplicates carefully

Complexity:
- Time: O(n²)
- Space: O(1) extra (output not counted)

What it tests:
- deduplication while finding pairs
- fixed + two-pointer pattern

---

### 4. 3Sum Closest
Find the triplet sum closest to a given target.

Input:
- `nums = [-1, 2, 1, -4]`, `target = 1`

Output:
- `2`  (triplet -1+2+1 = 2)

Approach:
- Sort, fix one, use two pointers
- Track the closest sum seen so far

Complexity:
- Time: O(n²)
- Space: O(1)

What it tests:
- closest-value tracking
- stopping condition refinement

---

### 5. 4Sum
Find all unique quadruplets that sum to a target.

Input:
- `nums = [1, 0, -1, 0, -2, 2]`, `target = 0`

Output:
- `[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]`

Approach:
- Sort array
- Fix two elements with two outer loops
- Use two pointers for the remaining pair
- Skip duplicates at every level

Complexity:
- Time: O(n³)
- Space: O(1) extra

What it tests:
- multi-level deduplication
- generalizing k-sum pattern

---

### 6. Pair with Target Sum (Two Pointer)
Given a sorted array, find one pair that sums to target.

Input:
- `arr = [1, 2, 3, 4, 6]`, `target = 6`

Output:
- `[1, 3]`  (indices)

Approach:
- Start left=0, right=end
- Adjust based on current sum

What it tests:
- core two-pointer mechanics

---

### 7. Count Pairs with Given Sum
Count all pairs whose sum equals a target.

Input:
- `arr = [1, 5, 7, -1, 5]`, `target = 6`

Output:
- `3`  (pairs: (1,5), (7,-1), (1,5))

Approach:
- Hash map: count frequency of each number
- For each element, check if (target - element) exists

What it tests:
- frequency map pair counting

---

### 8. Subarray with Given Sum
Find start and end index of a contiguous subarray that sums to target (all positive numbers).

Input:
- `arr = [1, 4, 20, 3, 10, 5]`, `target = 33`

Output:
- `[2, 4]`  (20+3+10 = 33)

Approach:
- Sliding window: expand right, shrink left when sum exceeds target

What it tests:
- sliding window on positive arrays

---

### 9. Subarray Sum Equals K
Count the number of subarrays whose sum equals k (can contain negatives).

Input:
- `nums = [1, 1, 1]`, `k = 2`

Output:
- `2`

Approach:
- Prefix sum + hash map
- If (prefix_sum - k) was seen before, those subarrays contribute

Complexity:
- Time: O(n)
- Space: O(n)

What it tests:
- prefix sum with hash map
- handles negative values

---

### 10. Maximum Sum of Pairs (Two Pointer on Sorted)
Given a sorted array, pair elements from start and end.
Find the max sum pair where sum ≤ target.

Input:
- `arr = [1, 2, 3, 4, 5]`, `target = 7`

Output:
- `[2, 5]`  (2+5=7)

What it tests:
- two-pointer greedy pair selection

---

### 11. Boats to Save People
Given weights and a limit, find minimum boats needed (each boat holds at most 2 people).

Input:
- `people = [1, 2, 2, 3]`, `limit = 3`

Output:
- `3`

Approach:
- Sort, use two pointers
- If heaviest + lightest fits, send both; otherwise send heaviest alone

What it tests:
- greedy two-pointer pairing

---

### 12. Valid Triangle Number
Count the number of triplets that can form a valid triangle.

Input:
- `nums = [2, 2, 3, 4]`

Output:
- `3`

Approach:
- Sort, fix the largest element
- Use two pointers on the left portion: count pairs where left+mid > largest

Complexity:
- Time: O(n²)
- Space: O(1)

What it tests:
- triangle inequality with two pointers

---

### 13. Minimum Size Subarray Sum
Find the smallest contiguous subarray with sum ≥ target.

Input:
- `nums = [2, 3, 1, 2, 4, 3]`, `target = 7`

Output:
- `2`  (subarray [4,3])

Approach:
- Sliding window: grow right, shrink left as long as sum ≥ target

Complexity:
- Time: O(n)
- Space: O(1)

What it tests:
- shrinking sliding window

---

### 14. Container with Most Water
Find two lines that together with the x-axis form a container holding the most water.

Input:
- `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`

Output:
- `49`

Approach:
- Two pointers from both ends
- Move the pointer at the shorter line inward

Complexity:
- Time: O(n)
- Space: O(1)

What it tests:
- greedy two-pointer area maximization

---

### 15. Trapping Rain Water
Calculate how much water can be trapped between walls.

Input:
- `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`

Output:
- `6`

Approaches:
- Prefix max arrays: O(n) time, O(n) space
- Two pointers (optimal): O(n) time, O(1) space

What it tests:
- prefix max thinking
- two-pointer with local max tracking

---

### 16. Sort Colors (Dutch National Flag)
Sort an array of 0s, 1s, and 2s in place.

Input:
- `nums = [2, 0, 2, 1, 1, 0]`

Output:
- `[0, 0, 1, 1, 2, 2]`

Approach:
- Three pointers: low, mid, high
- Partition into three regions in one pass

Complexity:
- Time: O(n)
- Space: O(1)

What it tests:
- three-pointer partition (Dutch flag)

---

### 17. Move Zeros
Move all zeros to the end while keeping non-zero elements in their relative order.

Input:
- `[0, 1, 0, 3, 12]`

Output:
- `[1, 3, 12, 0, 0]`

Approach:
- Two pointers: write pointer tracks next non-zero position

What it tests:
- in-place partitioning with a write pointer

---

### 18. Remove Duplicates from Sorted Array
Remove duplicates in place; return the count of unique elements.

Input:
- `nums = [1, 1, 2, 3, 3]`

Output:
- `3`, array modified to `[1, 2, 3, ...]`

Approach:
- Slow pointer tracks position for next unique value
- Fast pointer scans forward

What it tests:
- two-pointer write pattern on sorted array

---

### 19. Remove Duplicates II (allow at most 2)
Each value may appear at most twice.

Input:
- `nums = [1, 1, 1, 2, 2, 3]`

Output:
- `5`, array modified to `[1, 1, 2, 2, 3, ...]`

Approach:
- Write pointer k starts at 2
- Allow element if it differs from nums[k-2]

What it tests:
- generalized duplicate removal

---

### 20. Interval-Based Tuple: Merge Intervals
Merge all overlapping intervals.

Input:
- `[[1,3],[2,6],[8,10],[15,18]]`

Output:
- `[[1,6],[8,10],[15,18]]`

Approach:
- Sort by start time
- Merge if current start ≤ previous end

Complexity:
- Time: O(n log n)
- Space: O(n)

What it tests:
- interval tuple processing
- greedy merging

---

### 21. Insert Interval
Insert a new interval into a sorted non-overlapping list and merge if necessary.

Input:
- `intervals = [[1,3],[6,9]]`, `newInterval = [2,5]`

Output:
- `[[1,5],[6,9]]`

Approach:
- Add all intervals that end before new interval starts
- Merge all overlapping intervals with new interval
- Add remaining intervals

What it tests:
- three-phase interval insertion

---

### 22. Non-Overlapping Intervals
Find the minimum number of intervals to remove so no two overlap.

Input:
- `[[1,2],[2,3],[3,4],[1,3]]`

Output:
- `1`

Approach:
- Sort by end time (greedy)
- Keep track of last non-overlapping end
- Count intervals that must be removed

What it tests:
- greedy interval selection

---

### 23. Meeting Rooms
Determine if a person can attend all meetings (no overlapping intervals).

Input:
- `[[0,30],[5,10],[15,20]]`

Output:
- `false`

Approach:
- Sort by start time
- Check if any interval starts before the previous ends

What it tests:
- simple overlap detection

---

### 24. Meeting Rooms II
Find the minimum number of meeting rooms required.

Input:
- `[[0,30],[5,10],[15,20]]`

Output:
- `2`

Approach:
- Min-heap tracking end times of active meetings
- For each meeting, if earliest end ≤ current start, reuse that room

What it tests:
- heap-based room allocation

---

### 25. K-diff Pairs in an Array
Count the number of unique k-diff pairs (i, j) where |nums[i] - nums[j]| = k.

Input:
- `nums = [3, 1, 4, 1, 5]`, `k = 2`

Output:
- `2`  (pairs: (1,3) and (3,5))

Approach:
- Use a hash map to count frequencies
- For k > 0: check if num + k exists
- For k = 0: check if frequency > 1

What it tests:
- frequency map pair lookup
- k=0 edge case

---

---

### 26. Two Sum Less Than K
Find maximum pair sum where sum < k.

Input:
- `[34,23,1,24,75,33,54,8]`, k=60

Output:
- `58`

What it tests:
- two pointers with upper-bound constraint

---

### 27. Count Subarrays with Product Less Than K
Count contiguous subarrays whose product is strictly less than k.

Input:
- `[10,5,2,6]`, k=100

Output:
- `8`

What it tests:
- multiplicative sliding window
- counting valid sub-windows at each right pointer

---

### 28. Max Consecutive Ones III
Find maximum consecutive 1s after flipping at most k zeros.

Input:
- `[1,1,1,0,0,0,1,1,1,1,0]`, k=2

Output:
- `6`

What it tests:
- sliding window with allowed-violation count

---

### 29. Longest Subarray of 1s After Deleting One Element
Delete exactly one element and return the longest subarray of 1s.

Input:
- `[1,1,0,1]`

Output:
- `3`

What it tests:
- sliding window with one deletion (same pattern as k=1 zeros)

---

### 30. Fruit Into Baskets
Maximum fruits picked in one pass with at most two fruit types.

Input:
- `[1,2,3,2,2]`

Output:
- `4`

What it tests:
- sliding window with at-most-2-distinct constraint
- frequency map shrinking

---

### 31. Maximum Points from Cards
Pick k cards from either end to maximize total.

Input:
- `[1,2,3,4,5,6,1]`, k=3

Output:
- `12`

What it tests:
- complementary window (total - min subarray of size n-k)

---

### 32. Longest Subarray with Absolute Diff ≤ Limit
Longest subarray where max - min ≤ limit.

Input:
- `[10,1,2,4,7,2]`, limit=5

Output:
- `4`

What it tests:
- two monotonic deques inside a sliding window

---

### 33. Squares of a Sorted Array
Return sorted squares of a sorted array in O(n).

Input:
- `[-4,-1,0,3,10]`

Output:
- `[0,1,9,16,100]`

What it tests:
- two pointers filling result from largest to smallest

---

### 34. Minimum Difference Between Highest and Lowest of K Scores
Choose k elements; minimize the range.

Input:
- `[9,4,1,7]`, k=2

Output:
- `2`

What it tests:
- fixed-size sliding window after sorting

---

### 35. Number of Subarrays with Bounded Maximum
Count subarrays where max element is in [L, R].

Input:
- `[2,1,4,3]`, L=2, R=3

Output:
- `3`

What it tests:
- complementary counting (at-most R minus at-most L-1)

---

### 36. Find All Anagrams in a String
Return all start indices where an anagram of p begins in s.

Input:
- `s="cbaebabacd"`, `p="abc"`

Output:
- `[0,6]`

What it tests:
- fixed-size sliding window with character frequency comparison

---

### 37. Partition Array Such That Maximum Difference ≤ K
Minimum subsequences where each has max - min ≤ k.

Input:
- `[3,6,1,2,5]`, k=2

Output:
- `2`

What it tests:
- greedy grouping after sorting

---

### 38. Longest Turbulent Subarray
Longest subarray with strictly alternating comparisons.

Input:
- `[9,4,2,10,7,8,8,1,9]`

Output:
- `5`

What it tests:
- sign-alternation two-pointer tracking

---

### 39. Maximum Erasure Value
Maximum sum of a subarray with all unique elements.

Input:
- `[4,2,4,5,6]`

Output:
- `17`

What it tests:
- sliding window with Set for uniqueness + running sum

---

### 40. Maximum Sum of Two Non-Overlapping Subarrays
Find two non-overlapping subarrays of fixed lengths with maximum combined sum.

Input:
- `[0,6,5,2,2,5,1,9,4]`, firstLen=1, secondLen=2

Output:
- `20`

What it tests:
- prefix sums + two-pass window maximization

---

## Best Study Order

1. Two Sum (hash map)
2. Two Sum II (two pointer on sorted)
3. Pair with Target Sum
4. Count Pairs with Given Sum
5. Remove Duplicates from Sorted Array
6. Move Zeros
7. Container with Most Water
8. Trapping Rain Water
9. 3Sum
10. 3Sum Closest
11. Minimum Size Subarray Sum
12. Subarray with Given Sum
13. Subarray Sum Equals K
14. Boats to Save People
15. Sort Colors
16. Valid Triangle Number
17. Remove Duplicates II
18. Maximum Sum of Pairs
19. K-diff Pairs
20. 4Sum
21. Merge Intervals
22. Insert Interval
23. Non-Overlapping Intervals
24. Meeting Rooms
25. Meeting Rooms II
26. Two Sum Less Than K
27. Count Subarrays with Product Less Than K
28. Max Consecutive Ones III
29. Longest Subarray of 1s After Deleting One Element
30. Fruit Into Baskets
31. Maximum Points from Cards
32. Longest Subarray with Absolute Diff ≤ Limit
33. Squares of a Sorted Array
34. Minimum Difference Between Highest and Lowest of K Scores
35. Number of Subarrays with Bounded Maximum
36. Find All Anagrams in a String
37. Partition Array Such That Maximum Difference ≤ K
38. Longest Turbulent Subarray
39. Maximum Erasure Value
40. Maximum Sum of Two Non-Overlapping Subarrays

---

## Debugging Pattern for Tuple/Two-Pointer Problems

1. Always sort the array first if using two pointers (unless stated otherwise).
2. Print left and right pointer values at each step.
3. For 3Sum/4Sum, print the fixed element and pointer pair at each outer loop.
4. When skipping duplicates, print the value being skipped and new pointer position.
5. For interval problems, print start and end of current and previous interval when checking overlap.
6. For prefix sum problems, print the running sum and the map after each update.

---

## Code Files

- `python/tuple_problems.py`
- `javascript/tuple_problems.js`
