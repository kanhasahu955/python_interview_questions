/*
Linked List
===========

Complete set of common linked list interview questions.

Quick input/output examples:
- `reverseListIterative(1->2->3->4->5) -> 5->4->3->2->1`
- `mergeTwoSortedLists(1->3->5, 2->4->6) -> 1->2->3->4->5->6`
- `hasCycleFastSlow(headWithCycle) -> true`
- `removeNthFromEnd(1->2->3->4->5, n=2) -> 1->2->3->5`
- `isPalindrome(1->2->2->1) -> true`
- `addTwoNumbers(2->4->3, 5->6->4) -> 7->0->8`
- `sortList(4->2->1->3) -> 1->2->3->4`
- `rotateRight(1->2->3->4->5, k=2) -> 4->5->1->2->3`
*/

class ListNode {
  constructor(value = 0, next = null) {
    this.value = value;
    this.next = next;
  }
}

// ---------------------------------------------------------------------------
// Helper: build a list from array, convert result back to array
// ---------------------------------------------------------------------------

function buildList(values) {
  if (!values.length) return null;
  const head = new ListNode(values[0]);
  let current = head;
  for (let i = 1; i < values.length; i += 1) {
    current.next = new ListNode(values[i]);
    current = current.next;
  }
  return head;
}

function toArray(head) {
  const result = [];
  let current = head;
  while (current) {
    result.push(current.value);
    current = current.next;
  }
  return result;
}

// ---------------------------------------------------------------------------
// 1. Reverse Linked List
// ---------------------------------------------------------------------------

function reverseListIterative(head) {
  /*
  Problem:
  Reverse a singly linked list in place.

  Input:  1->2->3->4->5
  Output: 5->4->3->2->1

  Approach:
  - Track previous, current, nextNode
  - Reverse links one by one

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print previous, current, nextNode each iteration
  2. Confirm you save nextNode before overwriting current.next
  */
  let previous = null;
  let current = head;

  while (current) {
    const nextNode = current.next;
    current.next = previous;
    previous = current;
    current = nextNode;
  }

  return previous;
}

function reverseListRecursive(head) {
  /*
  Recursive approach — reverses by unwinding the call stack.

  Complexity: Time O(n), Space O(n) stack frames
  */
  if (!head || !head.next) {
    return head;
  }

  const newHead = reverseListRecursive(head.next);
  head.next.next = head;
  head.next = null;
  return newHead;
}

// ---------------------------------------------------------------------------
// 2. Merge Two Sorted Lists
// ---------------------------------------------------------------------------

function mergeTwoSortedLists(list1, list2) {
  /*
  Problem:
  Merge two sorted linked lists into one sorted list.

  Input:  1->3->5  and  2->4->6
  Output: 1->2->3->4->5->6

  Approach:
  - Dummy head so result head is always dummy.next
  - Always attach the smaller current node

  Complexity: Time O(n+m), Space O(1)

  Debugging steps:
  1. Print list1.value and list2.value each iteration
  */
  const dummy = new ListNode();
  let tail = dummy;

  while (list1 && list2) {
    if (list1.value <= list2.value) {
      tail.next = list1;
      list1 = list1.next;
    } else {
      tail.next = list2;
      list2 = list2.next;
    }
    tail = tail.next;
  }

  tail.next = list1 || list2;
  return dummy.next;
}

// ---------------------------------------------------------------------------
// 3. Linked List Cycle
// ---------------------------------------------------------------------------

function hasCycleSet(head) {
  /*
  Detect cycle using a Set of visited nodes.
  Complexity: Time O(n), Space O(n)
  */
  const seen = new Set();
  let current = head;

  while (current) {
    if (seen.has(current)) {
      return true;
    }
    seen.add(current);
    current = current.next;
  }

  return false;
}

function hasCycleFastSlow(head) {
  /*
  Floyd's cycle detection — no extra memory.

  Input:  list where tail points back to middle
  Output: true

  Approach:
  - Slow moves 1 step, fast moves 2 steps
  - If they meet, there is a cycle

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print slow.value and fast.value every round
  */
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) {
      return true;
    }
  }

  return false;
}

// ---------------------------------------------------------------------------
// 4. Remove Nth Node From End of List
// ---------------------------------------------------------------------------

function removeNthFromEnd(head, n) {
  /*
  Problem:
  Remove the nth node from the end in a single pass.

  Input:  1->2->3->4->5, n=2
  Output: 1->2->3->5

  Approach:
  - Dummy head to handle removing the head node
  - Advance fast pointer n+1 steps ahead
  - Move both until fast reaches end
  - slow.next is the node to remove

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print fast position as it advances
  2. Print slow.value when removing
  */
  const dummy = new ListNode(0);
  dummy.next = head;
  let fast = dummy;
  let slow = dummy;

  for (let i = 0; i <= n; i += 1) {
    fast = fast.next;
  }

  while (fast) {
    slow = slow.next;
    fast = fast.next;
  }

  slow.next = slow.next.next;
  return dummy.next;
}

// ---------------------------------------------------------------------------
// 5. Find Middle of Linked List
// ---------------------------------------------------------------------------

function findMiddle(head) {
  /*
  Problem:
  Return the middle node. If even length, return the second middle.

  Input:  1->2->3->4->5   Output: node(3)
  Input:  1->2->3->4->5->6 Output: node(4)

  Approach:
  - Fast moves 2 steps, slow moves 1 step

  Complexity: Time O(n), Space O(1)
  */
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  return slow;
}

// ---------------------------------------------------------------------------
// 6. Palindrome Linked List
// ---------------------------------------------------------------------------

function isPalindrome(head) {
  /*
  Problem:
  Check whether the linked list values form a palindrome.

  Input:  1->2->2->1  Output: true
  Input:  1->2->3     Output: false

  Approach:
  1. Find middle
  2. Reverse second half in place
  3. Compare both halves

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print first and second half values side by side
  */
  const middle = findMiddle(head);
  let secondHalf = reverseListIterative(middle);
  const savedSecond = secondHalf;

  let result = true;
  let first = head;

  while (secondHalf) {
    if (first.value !== secondHalf.value) {
      result = false;
      break;
    }
    first = first.next;
    secondHalf = secondHalf.next;
  }

  reverseListIterative(savedSecond);
  return result;
}

// ---------------------------------------------------------------------------
// 7. Intersection of Two Linked Lists
// ---------------------------------------------------------------------------

function getIntersectionNode(headA, headB) {
  /*
  Problem:
  Return the node where two lists intersect (same object reference).

  Input:
  A: 4->1->8->4->5
  B: 5->6->1->8->4->5  (shared: 8->4->5)
  Output: node(8)

  Approach:
  - Two pointers redirect to the other list's head when reaching end
  - After at most len(A)+len(B) steps they meet at intersection

  Complexity: Time O(n+m), Space O(1)

  Debugging steps:
  1. Print pointer values each step
  */
  if (!headA || !headB) return null;

  let pointerA = headA;
  let pointerB = headB;

  while (pointerA !== pointerB) {
    pointerA = pointerA ? pointerA.next : headB;
    pointerB = pointerB ? pointerB.next : headA;
  }

  return pointerA;
}

// ---------------------------------------------------------------------------
// 8. Add Two Numbers
// ---------------------------------------------------------------------------

function addTwoNumbers(l1, l2) {
  /*
  Problem:
  Two lists represent integers in reverse order. Return their sum as a list.

  Input:  2->4->3  and  5->6->4
  Output: 7->0->8   (342 + 465 = 807)

  Approach:
  - Walk both lists simultaneously
  - Track carry
  - Append new node for each sum digit

  Complexity: Time O(max(n,m)), Space O(max(n,m))

  Debugging steps:
  1. Print digit values and carry at each step
  */
  const dummy = new ListNode();
  let tail = dummy;
  let carry = 0;

  while (l1 || l2 || carry) {
    const value1 = l1 ? l1.value : 0;
    const value2 = l2 ? l2.value : 0;
    const total = value1 + value2 + carry;
    carry = Math.floor(total / 10);
    tail.next = new ListNode(total % 10);
    tail = tail.next;

    if (l1) l1 = l1.next;
    if (l2) l2 = l2.next;
  }

  return dummy.next;
}

// ---------------------------------------------------------------------------
// 9. Reverse Linked List II (partial reverse)
// ---------------------------------------------------------------------------

function reverseBetween(head, left, right) {
  /*
  Problem:
  Reverse nodes from position left to right (1-indexed).

  Input:  1->2->3->4->5, left=2, right=4
  Output: 1->4->3->2->5

  Approach:
  - Walk to the node just before position left
  - Reverse the sublist in place
  - Reconnect the segments

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print pre.value (node before reversal zone)
  2. Print nextNode and its new position each step
  */
  const dummy = new ListNode(0);
  dummy.next = head;
  let pre = dummy;

  for (let i = 0; i < left - 1; i += 1) {
    pre = pre.next;
  }

  let current = pre.next;

  for (let i = 0; i < right - left; i += 1) {
    const nextNode = current.next;
    current.next = nextNode.next;
    nextNode.next = pre.next;
    pre.next = nextNode;
  }

  return dummy.next;
}

// ---------------------------------------------------------------------------
// 10. Remove Duplicates from Sorted List (keep one copy)
// ---------------------------------------------------------------------------

function deleteDuplicates(head) {
  /*
  Problem:
  Remove extra duplicate nodes — keep one of each value.

  Input:  1->1->2->3->3
  Output: 1->2->3

  Approach:
  - Compare current with current.next
  - Skip ahead while they match

  Complexity: Time O(n), Space O(1)
  */
  let current = head;

  while (current && current.next) {
    if (current.value === current.next.value) {
      current.next = current.next.next;
    } else {
      current = current.next;
    }
  }

  return head;
}

// ---------------------------------------------------------------------------
// 11. Remove All Duplicates from Sorted List II (delete entire group)
// ---------------------------------------------------------------------------

function deleteAllDuplicates(head) {
  /*
  Problem:
  Remove every node whose value appears more than once.

  Input:  1->2->3->3->4->4->5
  Output: 1->2->5

  Approach:
  - Dummy head so the head itself can be removed
  - Track previous clean node
  - Skip entire group when a duplicate is detected

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print when a duplicate group is found and skipped
  */
  const dummy = new ListNode(0);
  dummy.next = head;
  let pre = dummy;

  while (pre.next) {
    const current = pre.next;
    if (current.next && current.value === current.next.value) {
      const duplicateValue = current.value;
      while (pre.next && pre.next.value === duplicateValue) {
        pre.next = pre.next.next;
      }
    } else {
      pre = pre.next;
    }
  }

  return dummy.next;
}

// ---------------------------------------------------------------------------
// 12. Sort List (merge sort)
// ---------------------------------------------------------------------------

function sortList(head) {
  /*
  Problem:
  Sort a linked list using O(n log n) time.

  Input:  4->2->1->3
  Output: 1->2->3->4

  Approach:
  - Find middle and split
  - Recursively sort both halves
  - Merge sorted halves

  Complexity: Time O(n log n), Space O(log n) stack

  Debugging steps:
  1. Print both halves before each merge call
  */
  if (!head || !head.next) return head;

  const middle = findMidForSort(head);
  const rightHead = middle.next;
  middle.next = null;

  const leftSorted = sortList(head);
  const rightSorted = sortList(rightHead);
  return mergeTwoSortedLists(leftSorted, rightSorted);
}

function findMidForSort(head) {
  let slow = head;
  let fast = head;

  while (fast.next && fast.next.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  return slow;
}

// ---------------------------------------------------------------------------
// 13. Rotate List
// ---------------------------------------------------------------------------

function rotateRight(head, k) {
  /*
  Problem:
  Rotate the list to the right by k positions.

  Input:  1->2->3->4->5, k=2
  Output: 4->5->1->2->3

  Approach:
  1. Compute length and make list circular
  2. New tail is at (length - k % length - 1)
  3. Break circle at new tail

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print length and effective k
  2. Print new head and new tail values
  */
  if (!head || !head.next || k === 0) return head;

  let tail = head;
  let length = 1;
  while (tail.next) {
    tail = tail.next;
    length += 1;
  }

  k = k % length;
  if (k === 0) return head;

  tail.next = head;

  let newTail = head;
  for (let i = 0; i < length - k - 1; i += 1) {
    newTail = newTail.next;
  }

  const newHead = newTail.next;
  newTail.next = null;
  return newHead;
}

// ---------------------------------------------------------------------------
// 14. Copy List with Random Pointer
// ---------------------------------------------------------------------------

class RandomListNode {
  constructor(value = 0, next = null, random = null) {
    this.value = value;
    this.next = next;
    this.random = random;
  }
}

function copyRandomList(head) {
  /*
  Problem:
  Deep clone a linked list with next and random pointers.

  Input:  [[7,null],[13,0],[11,4],[10,2],[1,0]]
  Output: deep copy with identical structure

  Approach:
  - Map: original node -> cloned node
  - First pass: create all clones
  - Second pass: assign next and random on clones

  Complexity: Time O(n), Space O(n)

  Debugging steps:
  1. Print each clone's value after first pass
  2. Confirm random pointers resolve correctly through the map
  */
  if (!head) return null;

  const nodeMap = new Map();

  let current = head;
  while (current) {
    nodeMap.set(current, new RandomListNode(current.value));
    current = current.next;
  }

  current = head;
  while (current) {
    const clone = nodeMap.get(current);
    clone.next = nodeMap.get(current.next) || null;
    clone.random = nodeMap.get(current.random) || null;
    current = current.next;
  }

  return nodeMap.get(head);
}

// ---------------------------------------------------------------------------
// 15. Reorder List
// ---------------------------------------------------------------------------

function reorderList(head) {
  /*
  Problem:
  Reorder L0->L1->...->Ln to L0->Ln->L1->Ln-1->...
  Modifies in place.

  Input:  1->2->3->4->5
  Output: 1->5->2->4->3

  Approach:
  1. Find middle (fast/slow)
  2. Reverse second half
  3. Merge first and reversed second half alternately

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print first and reversed second half separately
  2. Print each pair as they are interleaved
  */
  if (!head || !head.next) return;

  const middle = findMiddle(head);
  let second = reverseListIterative(middle);
  let first = head;

  while (second && second.next) {
    const tmp1 = first.next;
    const tmp2 = second.next;

    first.next = second;
    second.next = tmp1;

    first = tmp1;
    second = tmp2;
  }
}

// ---------------------------------------------------------------------------
// 16. Swap Nodes in Pairs
// ---------------------------------------------------------------------------

function swapPairs(head) {
  /*
  Problem:
  Swap every two adjacent nodes. Do not modify node values.

  Input:  1->2->3->4
  Output: 2->1->4->3

  Input:  1->2->3
  Output: 2->1->3

  Approach:
  - Dummy head to handle first pair cleanly
  - For each pair: save pointers, rewire, advance

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print first.value and second.value before each swap
  */
  const dummy = new ListNode(0);
  dummy.next = head;
  let pre = dummy;

  while (pre.next && pre.next.next) {
    const first = pre.next;
    const second = pre.next.next;

    pre.next = second;
    first.next = second.next;
    second.next = first;

    pre = first;
  }

  return dummy.next;
}

// ---------------------------------------------------------------------------
// 17. Remove Linked List Elements
// ---------------------------------------------------------------------------

function removeElements(head, val) {
  /*
  Problem:
  Remove all nodes whose value equals val.

  Input:  1->2->6->3->4->5->6, val=6
  Output: 1->2->3->4->5

  Approach:
  - Dummy head so head itself can be removed
  - Skip nodes that match val

  Complexity: Time O(n), Space O(1)
  */
  const dummy = new ListNode(0);
  dummy.next = head;
  let current = dummy;

  while (current.next) {
    if (current.next.value === val) {
      current.next = current.next.next;
    } else {
      current = current.next;
    }
  }

  return dummy.next;
}

// ---------------------------------------------------------------------------
// 18. Odd Even Linked List
// ---------------------------------------------------------------------------

function oddEvenList(head) {
  /*
  Problem:
  Group all odd-indexed nodes first, then even-indexed nodes (index starts at 1).

  Input:  1->2->3->4->5
  Output: 1->3->5->2->4

  Input:  2->1->3->5->6->4->7
  Output: 2->3->6->7->1->5->4

  Approach:
  - Two chains: odd and even
  - Alternate assigning nodes to each chain
  - Connect odd tail to even head

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print odd and even values as they are assigned
  */
  if (!head) return null;

  let odd = head;
  let even = head.next;
  const evenHead = even;

  while (even && even.next) {
    odd.next = even.next;
    odd = odd.next;
    even.next = odd.next;
    even = even.next;
  }

  odd.next = evenHead;
  return head;
}

// ---------------------------------------------------------------------------
// 19. Partition List
// ---------------------------------------------------------------------------

function partition(head, x) {
  /*
  Problem:
  Rearrange so all nodes with value < x come before nodes >= x.
  Preserve relative order.

  Input:  1->4->3->2->5->2, x=3
  Output: 1->2->2->4->3->5

  Approach:
  - Two dummy heads: lessDummy and greaterDummy
  - Append each node to the correct chain
  - Connect less tail to greater head

  Complexity: Time O(n), Space O(1)
  */
  const lessDummy = new ListNode(0);
  const greaterDummy = new ListNode(0);
  let less = lessDummy;
  let greater = greaterDummy;
  let current = head;

  while (current) {
    if (current.value < x) {
      less.next = current;
      less = less.next;
    } else {
      greater.next = current;
      greater = greater.next;
    }
    current = current.next;
  }

  greater.next = null;
  less.next = greaterDummy.next;
  return lessDummy.next;
}

// ---------------------------------------------------------------------------
// 20. Merge K Sorted Lists
// ---------------------------------------------------------------------------

function mergeKSortedLists(lists) {
  /*
  Problem:
  Merge k sorted linked lists into one sorted list.

  Input:  [1->4->5, 1->3->4, 2->6]
  Output: 1->1->2->3->4->4->5->6

  Approach (divide and conquer):
  - Merge pairs of lists repeatedly until one remains

  Complexity: Time O(n log k), Space O(log k) stack

  Debugging steps:
  1. Print lists remaining at each round of merging
  */
  if (!lists || !lists.length) return null;

  while (lists.length > 1) {
    const merged = [];
    for (let i = 0; i < lists.length; i += 2) {
      const l1 = lists[i];
      const l2 = i + 1 < lists.length ? lists[i + 1] : null;
      merged.push(mergeTwoSortedLists(l1, l2));
    }
    lists = merged;
  }

  return lists[0];
}

// ---------------------------------------------------------------------------
// 21. Reverse Nodes in k-Group
// ---------------------------------------------------------------------------

function reverseKGroup(head, k) {
  /*
  Problem:
  Reverse nodes k at a time. Leave remaining nodes as is.

  Input:  1->2->3->4->5, k=2
  Output: 2->1->4->3->5

  Input:  1->2->3->4->5, k=3
  Output: 3->2->1->4->5

  Approach:
  - Check if k nodes exist ahead
  - Reverse that group, connect to rest recursively

  Complexity: Time O(n), Space O(n/k) stack

  Debugging steps:
  1. Print group start and end before reversing
  */
  let count = 0;
  let node = head;
  while (node && count < k) {
    node = node.next;
    count += 1;
  }

  if (count < k) return head;

  let previous = null;
  let current = head;
  for (let i = 0; i < k; i += 1) {
    const nextNode = current.next;
    current.next = previous;
    previous = current;
    current = nextNode;
  }

  head.next = reverseKGroup(current, k);
  return previous;
}

// ---------------------------------------------------------------------------
// 22. Find the Duplicate Number (Floyd's on array as linked list)
// ---------------------------------------------------------------------------

function findDuplicate(nums) {
  /*
  Problem:
  Given n+1 integers each in range [1,n], find the duplicate.
  No modification to array, O(1) extra space.

  Input:  [1, 3, 4, 2, 2]
  Output: 2

  Input:  [3, 1, 3, 4, 2]
  Output: 3

  Approach (Floyd's cycle detection — treat array as linked list):
  - Index i links to nums[i]
  - Phase 1: detect meeting point inside cycle
  - Phase 2: find cycle entry = duplicate

  Complexity: Time O(n), Space O(1)
  */
  let slow = nums[0];
  let fast = nums[0];

  do {
    slow = nums[slow];
    fast = nums[nums[fast]];
  } while (slow !== fast);

  let finder = nums[0];
  while (finder !== slow) {
    finder = nums[finder];
    slow = nums[slow];
  }

  return slow;
}

// ---------------------------------------------------------------------------
// 23. Convert Binary Number in Linked List to Integer
// ---------------------------------------------------------------------------

function getDecimalValue(head) {
  /*
  Problem:
  Linked list represents a binary number (MSB first). Return decimal value.

  Input:  1->0->1
  Output: 5  (binary 101 = 5)

  Input:  1->1->1->0->1
  Output: 29

  Approach:
  - result = result * 2 + node.value for each node

  Complexity: Time O(n), Space O(1)
  */
  let result = 0;
  let current = head;

  while (current) {
    result = result * 2 + current.value;
    current = current.next;
  }

  return result;
}

// ---------------------------------------------------------------------------
// 24. LRU Cache (doubly linked list + hash map)
// ---------------------------------------------------------------------------

class LRUNode {
  constructor(key = 0, value = 0) {
    this.key = key;
    this.value = value;
    this.prev = null;
    this.next = null;
  }
}

class LRUCache {
  /*
  Problem:
  Design an LRU cache with O(1) get and put.

  Example:
  const cache = new LRUCache(2);
  cache.put(1, 1);   // {1:1}
  cache.put(2, 2);   // {1:1, 2:2}
  cache.get(1);      // returns 1, {2:2, 1:1}
  cache.put(3, 3);   // evicts 2, {1:1, 3:3}
  cache.get(2);      // returns -1

  Approach:
  - Map: key -> node for O(1) lookup
  - Doubly linked list: MRU at head, LRU at tail
  - On access/insert: move node to front
  - On overflow: remove tail node

  Debugging steps:
  1. Print cache map and list order after each operation
  */

  constructor(capacity) {
    this.capacity = capacity;
    this.cache = new Map();
    this.head = new LRUNode();
    this.tail = new LRUNode();
    this.head.next = this.tail;
    this.tail.prev = this.head;
  }

  _remove(node) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
  }

  _insertFront(node) {
    node.next = this.head.next;
    node.prev = this.head;
    this.head.next.prev = node;
    this.head.next = node;
  }

  get(key) {
    if (!this.cache.has(key)) return -1;
    const node = this.cache.get(key);
    this._remove(node);
    this._insertFront(node);
    return node.value;
  }

  put(key, value) {
    if (this.cache.has(key)) {
      this._remove(this.cache.get(key));
    }
    const node = new LRUNode(key, value);
    this.cache.set(key, node);
    this._insertFront(node);
    if (this.cache.size > this.capacity) {
      const lru = this.tail.prev;
      this._remove(lru);
      this.cache.delete(lru.key);
    }
  }
}

// ---------------------------------------------------------------------------
// 25. Linked List Components
// ---------------------------------------------------------------------------

function numComponents(head, nums) {
  /*
  Problem:
  Given a linked list and a subset array nums, count the number of connected
  components in the list that are entirely within nums.

  Input:  0->1->2->3, nums=[0,1,3]
  Output: 2  (components: [0,1] and [3])

  Input:  0->1->2->3->4, nums=[0,3,1,4]
  Output: 2  (components: [0,1] and [3,4])

  Approach:
  - Convert nums to a Set for O(1) lookup
  - Walk the list; count a component when the current node is in set
    and either the next is not in set or there is no next

  Complexity: Time O(n), Space O(k) where k = nums length

  Debugging steps:
  1. Print current.value and whether it ends a component
  */
  const numSet = new Set(nums);
  let count = 0;
  let current = head;

  while (current) {
    if (numSet.has(current.value) && (!current.next || !numSet.has(current.next.value))) {
      count += 1;
    }
    current = current.next;
  }

  return count;
}
