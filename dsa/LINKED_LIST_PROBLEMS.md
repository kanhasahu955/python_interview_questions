# Linked List DSA Problems

This file covers the complete set of linked list interview questions asked in major companies.

Linked list questions test:

- pointer manipulation
- two-pointer techniques (fast/slow)
- dummy node pattern
- in-place reversal
- recursion on nodes
- cycle and intersection detection
- merge logic

---

## Core Linked List Problems

### 1. Reverse Linked List
Reverse a singly linked list.

Input:
- `1 → 2 → 3 → 4 → 5`

Output:
- `5 → 4 → 3 → 2 → 1`

Approaches:
- Iterative: track prev, curr, next — O(n) time, O(1) space
- Recursive: reverse the rest, point next node back — O(n) time, O(n) stack space

What it tests:
- pointer rewiring
- iterative vs recursive thinking

---

### 2. Merge Two Sorted Lists
Merge two sorted linked lists into one sorted list.

Input:
- `1 → 3 → 5` and `2 → 4 → 6`

Output:
- `1 → 2 → 3 → 4 → 5 → 6`

Approaches:
- Iterative with dummy node — O(n + m) time, O(1) space
- Recursive — O(n + m) time, O(n + m) stack space

What it tests:
- sorted merge logic
- dummy node pattern

---

### 3. Linked List Cycle
Detect whether a linked list contains a cycle.

Input:
- list where tail points back to node at index 1

Output:
- `true`

Approaches:
- Hash set: store seen nodes — O(n) time, O(n) space
- Fast/slow pointers (Floyd's): if they meet, cycle exists — O(n) time, O(1) space

What it tests:
- cycle detection
- two-pointer technique

---

### 4. Remove Nth Node From End of List
Remove the nth node from the end without finding the length first.

Input:
- `1 → 2 → 3 → 4 → 5`, n = 2

Output:
- `1 → 2 → 3 → 5`

Approach:
- Use two pointers n steps apart
- When fast reaches end, slow is at the node before the target

What it tests:
- two-pointer gap technique
- dummy node to handle edge case (remove head)

---

### 5. Reorder List
Given `L0 → L1 → ... → Ln`, reorder to `L0 → Ln → L1 → Ln-1 → ...`

Input:
- `1 → 2 → 3 → 4 → 5`

Output:
- `1 → 5 → 2 → 4 → 3`

Approach:
1. Find middle (fast/slow pointers)
2. Reverse second half
3. Merge two halves alternately

What it tests:
- combining three sub-techniques in one problem
- in-place rearrangement

---

### 6. Find Middle of Linked List
Return the middle node. If two middles, return the second one.

Input:
- `1 → 2 → 3 → 4 → 5`

Output:
- node with value `3`

Input:
- `1 → 2 → 3 → 4 → 5 → 6`

Output:
- node with value `4`

Approach:
- Fast pointer moves 2 steps, slow moves 1 step
- When fast reaches end, slow is at the middle

What it tests:
- fast/slow pointer fundamentals

---

### 7. Palindrome Linked List
Check whether the linked list values form a palindrome.

Input:
- `1 → 2 → 2 → 1`

Output:
- `true`

Input:
- `1 → 2 → 3`

Output:
- `false`

Approach:
1. Find middle
2. Reverse second half
3. Compare both halves

What it tests:
- combining multiple techniques
- in-place comparison without extra space

---

### 8. Intersection of Two Linked Lists
Find the node where two lists intersect (same reference, not same value).

Input:
- List A: `4 → 1 → 8 → 4 → 5`
- List B: `5 → 6 → 1 → 8 → 4 → 5` (both share tail `8 → 4 → 5`)

Output:
- node with value `8`

Approach:
- Two pointers: when one reaches end, redirect to the other list's head
- They will meet at intersection after traversing equal total lengths

What it tests:
- clever pointer redirection
- no extra memory needed

---

### 9. Copy List with Random Pointer
Clone a linked list where each node has `next` and `random` pointers.

Input:
- `[[7,null],[13,0],[11,4],[10,2],[1,0]]`

Output:
- deep copy with identical structure and random pointer mapping

Approach:
- Use a hash map: original node → cloned node
- First pass: create all clones
- Second pass: assign next and random pointers

What it tests:
- hash map with node references
- deep copy logic

---

### 10. Add Two Numbers
Two non-empty linked lists represent non-negative integers in reverse order. Add them.

Input:
- `2 → 4 → 3` and `5 → 6 → 4`

Output:
- `7 → 0 → 8`  (342 + 465 = 807)

Approach:
- Traverse both lists simultaneously
- Handle carry at each step
- Append remaining nodes when one list is longer

What it tests:
- carry logic on nodes
- list building

---

### 11. Reverse Linked List II
Reverse only the nodes from position `left` to `right`.

Input:
- `1 → 2 → 3 → 4 → 5`, left = 2, right = 4

Output:
- `1 → 4 → 3 → 2 → 5`

Approach:
- Traverse to node before `left`
- Reverse the sublist between left and right in place
- Reconnect the segments

What it tests:
- partial reversal
- careful pointer bookkeeping

---

### 12. Remove Duplicates from Sorted List
Remove all duplicate values so each element appears only once.

Input:
- `1 → 1 → 2 → 3 → 3`

Output:
- `1 → 2 → 3`

Approach:
- Compare current with current.next
- Skip duplicates by adjusting next pointer

What it tests:
- in-place node removal
- sorted list property usage

---

### 13. Remove All Duplicates from Sorted List II
Remove all nodes that have duplicate values (not just extras — remove the value entirely).

Input:
- `1 → 2 → 3 → 3 → 4 → 4 → 5`

Output:
- `1 → 2 → 5`

Approach:
- Use dummy node
- Skip all nodes matching a repeated value

What it tests:
- full group deletion
- dummy head pattern

---

### 14. Sort List
Sort a linked list using merge sort.

Input:
- `4 → 2 → 1 → 3`

Output:
- `1 → 2 → 3 → 4`

Approach:
- Find the middle, split
- Recursively sort both halves
- Merge sorted halves

What it tests:
- merge sort adapted for linked lists
- recursion with pointer splitting

---

### 15. Rotate List
Rotate the list to the right by `k` places.

Input:
- `1 → 2 → 3 → 4 → 5`, k = 2

Output:
- `4 → 5 → 1 → 2 → 3`

Approach:
1. Compute length, make the list circular
2. Find new tail at position `length - k % length - 1`
3. Break the circle at the right point

What it tests:
- modular index arithmetic on list
- circular link manipulation

---

---

### 16. Swap Nodes in Pairs
Swap every two adjacent nodes without modifying values.

Input:
- `1 → 2 → 3 → 4`

Output:
- `2 → 1 → 4 → 3`

What it tests:
- dummy head pattern
- pair-by-pair pointer rewiring

---

### 17. Remove Linked List Elements
Remove all nodes whose value equals a given target.

Input:
- `1 → 2 → 6 → 3 → 4 → 5 → 6`, val = 6

Output:
- `1 → 2 → 3 → 4 → 5`

What it tests:
- in-place node removal
- dummy head for edge case when head matches

---

### 18. Odd Even Linked List
Group all odd-indexed nodes first, then even-indexed nodes (index starts at 1).

Input:
- `1 → 2 → 3 → 4 → 5`

Output:
- `1 → 3 → 5 → 2 → 4`

What it tests:
- two-chain pattern
- relative order preservation

---

### 19. Partition List
Rearrange so all nodes with value less than x come before nodes greater than or equal to x.

Input:
- `1 → 4 → 3 → 2 → 5 → 2`, x = 3

Output:
- `1 → 2 → 2 → 4 → 3 → 5`

What it tests:
- two dummy heads
- stable partition on linked list

---

### 20. Merge K Sorted Lists
Merge k sorted linked lists into one sorted list.

Input:
- `[1→4→5, 1→3→4, 2→6]`

Output:
- `1→1→2→3→4→4→5→6`

Approaches:
- Min-heap: O(n log k) time, O(k) space
- Divide and conquer: O(n log k) time, O(1) extra

What it tests:
- heap usage
- divide-and-conquer merging

---

### 21. Reverse Nodes in k-Group
Reverse every k nodes in the list. Leave remaining nodes as is.

Input:
- `1 → 2 → 3 → 4 → 5`, k = 2

Output:
- `2 → 1 → 4 → 3 → 5`

Input:
- `1 → 2 → 3 → 4 → 5`, k = 3

Output:
- `3 → 2 → 1 → 4 → 5`

What it tests:
- group reversal
- recursion with pointer reconnection

---

### 22. Find the Duplicate Number
Given n+1 integers each in range [1, n], find the duplicate without modifying the array.

Input:
- `[1, 3, 4, 2, 2]`

Output:
- `2`

Approach:
- Treat the array as a linked list (index → nums[index])
- Apply Floyd's cycle detection to find the cycle entry

What it tests:
- creative problem reduction
- Floyd's algorithm applied to arrays

---

### 23. Convert Binary Number in Linked List to Integer
The list represents a binary number most-significant-bit first. Return its decimal value.

Input:
- `1 → 0 → 1`

Output:
- `5`

What it tests:
- bit shifting logic on nodes
- simple traversal with accumulation

---

### 24. LRU Cache
Design a cache that evicts the least recently used item when full. Both get and put must be O(1).

Example:
- `capacity = 2`
- `put(1,1)`, `put(2,2)`, `get(1)` → 1, `put(3,3)` evicts key 2, `get(2)` → -1

Approach:
- Hash map for O(1) lookup
- Doubly linked list for O(1) move-to-front and eviction

What it tests:
- combining hash map with linked list
- LRU eviction policy implementation

---

### 25. Linked List Components
Given a linked list and a subset of its values, count connected components entirely within the subset.

Input:
- `0 → 1 → 2 → 3`, nums = `[0, 1, 3]`

Output:
- `2`  (components: `[0,1]` and `[3]`)

What it tests:
- set lookup combined with list traversal
- component boundary detection

---

## Best Study Order

1. Reverse Linked List
2. Find Middle of Linked List
3. Merge Two Sorted Lists
4. Linked List Cycle
5. Remove Nth Node From End
6. Palindrome Linked List
7. Intersection of Two Linked Lists
8. Add Two Numbers
9. Reverse Linked List II
10. Remove Duplicates from Sorted List
11. Remove All Duplicates from Sorted List II
12. Reorder List
13. Sort List
14. Copy List with Random Pointer
15. Rotate List
16. Swap Nodes in Pairs
17. Remove Linked List Elements
18. Odd Even Linked List
19. Partition List
20. Merge K Sorted Lists
21. Reverse Nodes in k-Group
22. Find the Duplicate Number
23. Convert Binary Number in Linked List to Integer
24. LRU Cache
25. Linked List Components

---

## Debugging Pattern For Linked List Problems

1. Always draw the list on paper before coding.
2. Print each node's value and next pointer inside the loop.
3. For two-pointer problems, print slow and fast at every step.
4. When rewiring pointers, confirm you saved `next` before overwriting.
5. Use dummy head when the result list's head might change.
6. Test with: empty list, single node, two nodes, cycle at tail, cycle at head.

---

## Code Files

- `python/linked_list.py`
- `javascript/linked_list.js`
