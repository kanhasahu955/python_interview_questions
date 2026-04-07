"""
Linked List
===========

Complete set of common linked list interview questions.

Quick input/output examples:
- `reverse_list_iterative(1->2->3->4->5) -> 5->4->3->2->1`
- `merge_two_sorted_lists(1->3->5, 2->4->6) -> 1->2->3->4->5->6`
- `has_cycle_fast_slow(head_with_cycle) -> True`
- `remove_nth_from_end(1->2->3->4->5, n=2) -> 1->2->3->5`
- `is_palindrome(1->2->2->1) -> True`
- `add_two_numbers(2->4->3, 5->6->4) -> 7->0->8`
- `sort_list(4->2->1->3) -> 1->2->3->4`
- `rotate_right(1->2->3->4->5, k=2) -> 4->5->1->2->3`
- `swap_pairs(1->2->3->4) -> 2->1->4->3`
- `odd_even_list(1->2->3->4->5) -> 1->3->5->2->4`
- `merge_k_sorted_lists([1->4->5, 1->3->4, 2->6]) -> 1->1->2->3->4->4->5->6`
- `reverse_k_group(1->2->3->4->5, k=2) -> 2->1->4->3->5`
- `find_duplicate([1,3,4,2,2]) -> 2`
- `get_decimal_value(1->0->1) -> 5`
- `LRUCache(2): put(1,1), put(2,2), get(1) -> 1, put(3,3), get(2) -> -1`
"""

from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, value: int = 0, next_node: Optional["ListNode"] = None) -> None:
        self.value = value
        self.next = next_node

    def __repr__(self) -> str:
        return f"ListNode(value={self.value})"


# ---------------------------------------------------------------------------
# Helper: build a list from a Python list and convert result back to list
# ---------------------------------------------------------------------------

def build_list(values: list[int]) -> Optional[ListNode]:
    """Build a linked list from a plain list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def to_list(head: Optional[ListNode]) -> list[int]:
    """Convert a linked list back to a plain Python list for easy inspection."""
    result: list[int] = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result


# ---------------------------------------------------------------------------
# 1. Reverse Linked List
# ---------------------------------------------------------------------------

def reverse_list_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Problem:
    Reverse a singly linked list in place.

    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: 5 -> 4 -> 3 -> 2 -> 1

    Approach:
    - Track previous, current, next_node
    - Reverse links one by one

    Complexity:
    - Time: O(n)
    - Space: O(1)

    Debugging steps:
    1. Print previous, current, next_node each iteration
    2. Ensure you save next_node before overwriting current.next
    """
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Recursive approach — reverses by unwinding the call stack.

    Complexity:
    - Time: O(n)
    - Space: O(n) stack frames

    Debugging steps:
    1. Print head.value at each call
    2. Confirm head.next.next = head connects backward
    """
    if head is None or head.next is None:
        return head

    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


# ---------------------------------------------------------------------------
# 2. Merge Two Sorted Lists
# ---------------------------------------------------------------------------

def merge_two_sorted_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Problem:
    Merge two sorted linked lists into one sorted list.

    Input:  1->3->5  and  2->4->6
    Output: 1->2->3->4->5->6

    Approach:
    - Use a dummy head node so result head is always dummy.next
    - Always attach the smaller current node to tail

    Complexity:
    - Time: O(n + m)
    - Space: O(1)

    Debugging steps:
    1. Print list1.value and list2.value each iteration
    2. Print the node just attached to merged list
    """
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.value <= list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2
    return dummy.next


# ---------------------------------------------------------------------------
# 3. Linked List Cycle
# ---------------------------------------------------------------------------

def has_cycle_set(head: Optional[ListNode]) -> bool:
    """
    Problem:
    Detect whether a linked list contains a cycle.

    Input:  list where tail points to node at index 1
    Output: True

    Approach:
    - Store visited node references in a set

    Complexity:
    - Time: O(n)
    - Space: O(n)
    """
    seen: set[ListNode] = set()
    current = head

    while current:
        if current in seen:
            return True
        seen.add(current)
        current = current.next

    return False


def has_cycle_fast_slow(head: Optional[ListNode]) -> bool:
    """
    Floyd's cycle detection — no extra memory.

    Approach:
    - Slow pointer moves 1 step, fast moves 2 steps
    - If they meet, there is a cycle

    Complexity:
    - Time: O(n)
    - Space: O(1)

    Debugging steps:
    1. Print slow.value and fast.value each round
    2. Confirm fast and fast.next null checks are first
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next  # type: ignore[assignment]
        fast = fast.next.next
        if slow == fast:
            return True

    return False


# ---------------------------------------------------------------------------
# 4. Remove Nth Node From End of List
# ---------------------------------------------------------------------------

def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Problem:
    Remove the nth node from the end in a single pass.

    Input:  1->2->3->4->5, n=2
    Output: 1->2->3->5

    Approach:
    - Use dummy head so we can remove head itself if needed
    - Advance fast pointer n steps ahead
    - Move both until fast reaches end
    - slow.next is the node to remove

    Complexity:
    - Time: O(n)
    - Space: O(1)

    Debugging steps:
    1. Print fast pointer position as it advances
    2. Print slow.value when removing
    """
    dummy = ListNode(0)
    dummy.next = head
    fast: Optional[ListNode] = dummy
    slow: Optional[ListNode] = dummy

    for _ in range(n + 1):
        fast = fast.next  # type: ignore[union-attr]

    while fast:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next

    slow.next = slow.next.next  # type: ignore[union-attr]
    return dummy.next


# ---------------------------------------------------------------------------
# 5. Find Middle of Linked List
# ---------------------------------------------------------------------------

def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Problem:
    Return the middle node. If even length, return the second middle.

    Input:  1->2->3->4->5
    Output: node(3)

    Input:  1->2->3->4->5->6
    Output: node(4)

    Approach:
    - Fast moves 2 steps, slow moves 1 step
    - When fast reaches end, slow is at middle

    Complexity:
    - Time: O(n)
    - Space: O(1)

    Debugging steps:
    1. Print slow.value and fast.value each loop
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next  # type: ignore[assignment]
        fast = fast.next.next

    return slow


# ---------------------------------------------------------------------------
# 6. Palindrome Linked List
# ---------------------------------------------------------------------------

def is_palindrome(head: Optional[ListNode]) -> bool:
    """
    Problem:
    Check whether the linked list values form a palindrome.

    Input:  1->2->2->1
    Output: True

    Input:  1->2->3
    Output: False

    Approach:
    1. Find middle
    2. Reverse second half in place
    3. Compare first and second halves

    Complexity:
    - Time: O(n)
    - Space: O(1)

    Debugging steps:
    1. Print first half and reversed second half node by node
    2. Confirm middle is correct for odd/even lengths
    """
    middle = find_middle(head)
    second_half = reverse_list_iterative(middle)
    check = second_half

    result = True
    first = head
    while check:
        if first.value != check.value:  # type: ignore[union-attr]
            result = False
            break
        first = first.next  # type: ignore[assignment]
        check = check.next

    # Restore the list (optional, good practice)
    reverse_list_iterative(second_half)
    return result


# ---------------------------------------------------------------------------
# 7. Intersection of Two Linked Lists
# ---------------------------------------------------------------------------

def get_intersection_node(
    head_a: Optional[ListNode], head_b: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Problem:
    Return the node where two linked lists intersect (same object, not same value).

    Input:
    A: 4->1->8->4->5
    B: 5->6->1->8->4->5  (share 8->4->5)
    Output: node(8)

    Approach:
    - Two pointers start at each head
    - When one reaches end, redirect to the other list's head
    - After at most len(A) + len(B) steps they meet at intersection

    Complexity:
    - Time: O(n + m)
    - Space: O(1)

    Debugging steps:
    1. Print pointer values each step
    2. Confirm redirect only happens once per pointer
    """
    if not head_a or not head_b:
        return None

    pointer_a: Optional[ListNode] = head_a
    pointer_b: Optional[ListNode] = head_b

    while pointer_a is not pointer_b:
        pointer_a = pointer_a.next if pointer_a else head_b
        pointer_b = pointer_b.next if pointer_b else head_a

    return pointer_a


# ---------------------------------------------------------------------------
# 8. Add Two Numbers
# ---------------------------------------------------------------------------

def add_two_numbers(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Problem:
    Two lists represent integers in reverse order. Return their sum as a list.

    Input:  2->4->3  and  5->6->4
    Output: 7->0->8        (342 + 465 = 807)

    Approach:
    - Walk both lists simultaneously
    - Keep a carry variable
    - Append a new node for each sum digit

    Complexity:
    - Time: O(max(n, m))
    - Space: O(max(n, m))

    Debugging steps:
    1. Print current digit values and carry at each step
    2. Confirm extra node is added when carry remains after both lists finish
    """
    dummy = ListNode()
    tail = dummy
    carry = 0

    while l1 or l2 or carry:
        value1 = l1.value if l1 else 0
        value2 = l2.value if l2 else 0

        total = value1 + value2 + carry
        carry = total // 10
        tail.next = ListNode(total % 10)
        tail = tail.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next


# ---------------------------------------------------------------------------
# 9. Reverse Linked List II (partial reverse)
# ---------------------------------------------------------------------------

def reverse_between(
    head: Optional[ListNode], left: int, right: int
) -> Optional[ListNode]:
    """
    Problem:
    Reverse only the nodes from position left to right (1-indexed).

    Input:  1->2->3->4->5, left=2, right=4
    Output: 1->4->3->2->5

    Approach:
    - Walk to the node just before position left
    - Reverse the sublist of length (right - left + 1)
    - Reconnect the reversed segment

    Complexity:
    - Time: O(n)
    - Space: O(1)

    Debugging steps:
    1. Print pre.value (node before reversal zone)
    2. Print each node's next during reversal
    """
    dummy = ListNode(0)
    dummy.next = head
    pre: ListNode = dummy

    for _ in range(left - 1):
        pre = pre.next  # type: ignore[assignment]

    current: Optional[ListNode] = pre.next
    for _ in range(right - left):
        next_node = current.next  # type: ignore[union-attr]
        current.next = next_node.next  # type: ignore[union-attr]
        next_node.next = pre.next
        pre.next = next_node

    return dummy.next


# ---------------------------------------------------------------------------
# 10. Remove Duplicates from Sorted List (keep one copy)
# ---------------------------------------------------------------------------

def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Problem:
    Remove extra duplicate nodes — keep one of each value.

    Input:  1->1->2->3->3
    Output: 1->2->3

    Approach:
    - Compare current with current.next
    - Skip ahead while they match

    Complexity:
    - Time: O(n)
    - Space: O(1)

    Debugging steps:
    1. Print current.value and current.next.value at each step
    """
    current = head

    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next

    return head


# ---------------------------------------------------------------------------
# 11. Remove All Duplicates from Sorted List II (delete entire group)
# ---------------------------------------------------------------------------

def delete_all_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Problem:
    Remove every node whose value appears more than once.

    Input:  1->2->3->3->4->4->5
    Output: 1->2->5

    Approach:
    - Dummy head so head itself can be removed
    - Track previous clean node
    - Skip entire group when a duplicate is detected

    Complexity:
    - Time: O(n)
    - Space: O(1)

    Debugging steps:
    1. Print when a duplicate group is found and skipped
    2. Confirm pre.next is correctly reset after skipping
    """
    dummy = ListNode(0)
    dummy.next = head
    pre: ListNode = dummy

    while pre.next:
        current = pre.next
        # Check if the current value is repeated
        if current.next and current.value == current.next.value:
            duplicate_value = current.value
            while pre.next and pre.next.value == duplicate_value:
                pre.next = pre.next.next
        else:
            pre = pre.next  # type: ignore[assignment]

    return dummy.next


# ---------------------------------------------------------------------------
# 12. Sort List (merge sort)
# ---------------------------------------------------------------------------

def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Problem:
    Sort a linked list using O(n log n) time and O(1) auxiliary space.

    Input:  4->2->1->3
    Output: 1->2->3->4

    Approach:
    - Find the middle and split
    - Recursively sort both halves
    - Merge the two sorted halves

    Complexity:
    - Time: O(n log n)
    - Space: O(log n) recursive stack

    Debugging steps:
    1. Print both halves before each merge call
    2. Confirm the split point is correct (mid.next = None)
    """
    if not head or not head.next:
        return head

    middle = _find_mid_for_sort(head)
    right_head = middle.next
    middle.next = None  # split the list

    left_sorted = sort_list(head)
    right_sorted = sort_list(right_head)
    return merge_two_sorted_lists(left_sorted, right_sorted)


def _find_mid_for_sort(head: ListNode) -> ListNode:
    """Return the node just before the second half (for even splits)."""
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next  # type: ignore[assignment]
        fast = fast.next.next

    return slow


# ---------------------------------------------------------------------------
# 13. Rotate List
# ---------------------------------------------------------------------------

def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Problem:
    Rotate the list to the right by k positions.

    Input:  1->2->3->4->5, k=2
    Output: 4->5->1->2->3

    Approach:
    1. Compute length and make list circular
    2. New tail is at position (length - k % length - 1)
    3. Break circle at that point

    Complexity:
    - Time: O(n)
    - Space: O(1)

    Debugging steps:
    1. Print length and effective k (k % length)
    2. Print new tail and new head values
    """
    if not head or not head.next or k == 0:
        return head

    tail = head
    length = 1
    while tail.next:
        tail = tail.next
        length += 1

    k = k % length
    if k == 0:
        return head

    tail.next = head  # make circular

    steps_to_new_tail = length - k - 1
    new_tail = head
    for _ in range(steps_to_new_tail):
        new_tail = new_tail.next  # type: ignore[assignment]

    new_head = new_tail.next  # type: ignore[assignment]
    new_tail.next = None
    return new_head


# ---------------------------------------------------------------------------
# 14. Copy List with Random Pointer
# ---------------------------------------------------------------------------

class RandomListNode:
    def __init__(
        self,
        value: int = 0,
        next_node: Optional["RandomListNode"] = None,
        random: Optional["RandomListNode"] = None,
    ) -> None:
        self.value = value
        self.next = next_node
        self.random = random


def copy_random_list(
    head: Optional[RandomListNode],
) -> Optional[RandomListNode]:
    """
    Problem:
    Deep clone a linked list where every node has next and random pointers.

    Input:  [[7,null],[13,0],[11,4],[10,2],[1,0]]
    Output: deep copy with identical structure

    Approach:
    - Hash map: original node -> cloned node
    - First pass: create all clone nodes
    - Second pass: assign next and random on clones

    Complexity:
    - Time: O(n)
    - Space: O(n)

    Debugging steps:
    1. Print each node's value and its clone's value after first pass
    2. Confirm random pointers resolve correctly through the map
    """
    if not head:
        return None

    node_map: dict[RandomListNode, RandomListNode] = {}

    current: Optional[RandomListNode] = head
    while current:
        node_map[current] = RandomListNode(current.value)
        current = current.next

    current = head
    while current:
        clone = node_map[current]
        clone.next = node_map.get(current.next)  # type: ignore[arg-type]
        clone.random = node_map.get(current.random)  # type: ignore[arg-type]
        current = current.next

    return node_map[head]


# ---------------------------------------------------------------------------
# 15. Reorder List
# ---------------------------------------------------------------------------

def reorder_list(head: Optional[ListNode]) -> None:
    """
    Problem:
    Reorder L0->L1->...->Ln to L0->Ln->L1->Ln-1->...
    Modify in place, return nothing.

    Input:  1->2->3->4->5
    Output: 1->5->2->4->3

    Approach:
    1. Find middle (fast/slow)
    2. Reverse second half
    3. Merge first and reversed second half alternately

    Complexity:
    - Time: O(n)
    - Space: O(1)

    Debugging steps:
    1. Print first half and reversed second half separately
    2. Print each pair as they are interleaved
    """
    if not head or not head.next:
        return

    middle = find_middle(head)
    second = reverse_list_iterative(middle)
    first: Optional[ListNode] = head

    while second and second.next:
        tmp1 = first.next  # type: ignore[union-attr]
        tmp2 = second.next

        first.next = second  # type: ignore[union-attr]
        second.next = tmp1

        first = tmp1
        second = tmp2


# ---------------------------------------------------------------------------
# 16. Flatten a Multilevel Doubly Linked List
# ---------------------------------------------------------------------------

class MultiNode:
    def __init__(self, value: int = 0) -> None:
        self.value = value
        self.prev: Optional["MultiNode"] = None
        self.next: Optional["MultiNode"] = None
        self.child: Optional["MultiNode"] = None


def flatten(head: Optional[MultiNode]) -> Optional[MultiNode]:
    """
    Problem:
    Flatten a multilevel doubly linked list where nodes may have a child list.
    Append child lists after the node and before the node's next.

    Input:
    1 - 2 - 3 - 4 - 5
            |
            7 - 8 - 9

    Output: 1 - 2 - 3 - 7 - 8 - 9 - 4 - 5

    Approach:
    - Use a stack to save the rest of the list when a child is found
    - Insert child list in place

    Complexity:
    - Time: O(n)
    - Space: O(n) stack

    Debugging steps:
    1. Print node.value and whether it has a child
    2. Print stack contents when pushing and popping
    """
    if not head:
        return None

    stack: list[Optional[MultiNode]] = []
    current: Optional[MultiNode] = head

    while current:
        if current.child:
            if current.next:
                stack.append(current.next)
            current.next = current.child
            current.child.prev = current
            current.child = None

        if not current.next and stack:
            next_node = stack.pop()
            current.next = next_node
            if next_node:
                next_node.prev = current

        current = current.next

    return head


# ---------------------------------------------------------------------------
# 17. Swap Nodes in Pairs
# ---------------------------------------------------------------------------

def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Problem:
    Swap every two adjacent nodes. Do not modify node values.

    Input:  1 -> 2 -> 3 -> 4
    Output: 2 -> 1 -> 4 -> 3

    Input:  1 -> 2 -> 3
    Output: 2 -> 1 -> 3

    Approach:
    - Dummy head to handle swapping the first pair cleanly
    - For each pair: save pointers, rewire, advance

    Complexity:
    - Time: O(n)
    - Space: O(1)

    Debugging steps:
    1. Print first.value and second.value before each swap
    2. Confirm pre.next points to second after swap
    """
    dummy = ListNode(0)
    dummy.next = head
    pre: ListNode = dummy

    while pre.next and pre.next.next:
        first = pre.next
        second = pre.next.next

        pre.next = second
        first.next = second.next
        second.next = first

        pre = first

    return dummy.next


# ---------------------------------------------------------------------------
# 18. Remove Linked List Elements
# ---------------------------------------------------------------------------

def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """
    Problem:
    Remove all nodes whose value equals val.

    Input:  1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6, val = 6
    Output: 1 -> 2 -> 3 -> 4 -> 5

    Approach:
    - Dummy head so head itself can be removed
    - Skip any node whose value matches val

    Complexity:
    - Time: O(n)
    - Space: O(1)

    Debugging steps:
    1. Print each node before deciding to keep or skip
    """
    dummy = ListNode(0)
    dummy.next = head
    current: ListNode = dummy

    while current.next:
        if current.next.value == val:
            current.next = current.next.next
        else:
            current = current.next  # type: ignore[assignment]

    return dummy.next


# ---------------------------------------------------------------------------
# 19. Odd Even Linked List
# ---------------------------------------------------------------------------

def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Problem:
    Group all odd-indexed nodes first, then even-indexed nodes.
    Index starts at 1. Preserve relative order within each group.

    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: 1 -> 3 -> 5 -> 2 -> 4

    Input:  2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
    Output: 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4

    Approach:
    - Two chains: odd and even
    - Alternate adding to each chain
    - Connect odd tail to even head

    Complexity:
    - Time: O(n)
    - Space: O(1)

    Debugging steps:
    1. Print odd and even node values as they are assigned
    2. Confirm even_head is saved before modifying the list
    """
    if not head:
        return None

    odd: ListNode = head
    even: Optional[ListNode] = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next  # type: ignore[assignment]
        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head


# ---------------------------------------------------------------------------
# 20. Partition List
# ---------------------------------------------------------------------------

def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    """
    Problem:
    Rearrange so all nodes with value < x come before nodes with value >= x.
    Preserve relative order within each partition.

    Input:  1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
    Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5

    Approach:
    - Two dummy heads: less_dummy and greater_dummy
    - Append each node to the correct chain
    - Connect less chain tail to greater chain head

    Complexity:
    - Time: O(n)
    - Space: O(1)

    Debugging steps:
    1. Print which chain each node joins
    2. Confirm less tail's next is set to None before connecting
    """
    less_dummy = ListNode(0)
    greater_dummy = ListNode(0)
    less: ListNode = less_dummy
    greater: ListNode = greater_dummy
    current = head

    while current:
        if current.value < x:
            less.next = current
            less = less.next  # type: ignore[assignment]
        else:
            greater.next = current
            greater = greater.next  # type: ignore[assignment]
        current = current.next

    greater.next = None
    less.next = greater_dummy.next
    return less_dummy.next


# ---------------------------------------------------------------------------
# 21. Merge K Sorted Lists
# ---------------------------------------------------------------------------

import heapq


def merge_k_sorted_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Problem:
    Merge k sorted linked lists into one sorted list.

    Input:  [1->4->5, 1->3->4, 2->6]
    Output: 1->1->2->3->4->4->5->6

    Approaches:
    A) Min-heap: push (value, index, node) for each list head
       Pop minimum, push its next — O(n log k) time, O(k) space
    B) Divide and conquer: merge pairs repeatedly — O(n log k) time, O(1) extra

    Complexity:
    - Time: O(n log k)
    - Space: O(k)

    Debugging steps:
    1. Print the heap after each push/pop
    2. Confirm the correct node is popped and its next is pushed
    """
    dummy = ListNode()
    tail = dummy
    heap: list[tuple[int, int, ListNode]] = []

    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.value, i, node))

    while heap:
        value, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.value, i, node.next))

    return dummy.next


# ---------------------------------------------------------------------------
# 22. Reverse Nodes in k-Group
# ---------------------------------------------------------------------------

def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Problem:
    Reverse nodes of the list k at a time. Leave remaining nodes as is.

    Input:  1 -> 2 -> 3 -> 4 -> 5, k = 2
    Output: 2 -> 1 -> 4 -> 3 -> 5

    Input:  1 -> 2 -> 3 -> 4 -> 5, k = 3
    Output: 3 -> 2 -> 1 -> 4 -> 5

    Approach:
    - Check if k nodes exist ahead
    - Reverse that group, reconnect to the rest recursively

    Complexity:
    - Time: O(n)
    - Space: O(n/k) recursive stack

    Debugging steps:
    1. Print group start and end before reversing
    2. Print new head after each group reversal
    """
    count = 0
    node = head
    while node and count < k:
        node = node.next
        count += 1

    if count < k:
        return head

    previous = None
    current = head
    for _ in range(k):
        next_node = current.next  # type: ignore[union-attr]
        current.next = previous  # type: ignore[union-attr]
        previous = current
        current = next_node

    head.next = reverse_k_group(current, k)  # type: ignore[union-attr]
    return previous


# ---------------------------------------------------------------------------
# 23. Find the Duplicate Number (Floyd's on array as linked list)
# ---------------------------------------------------------------------------

def find_duplicate(nums: list[int]) -> int:
    """
    Problem:
    Given n+1 integers where each is in range [1, n], find the duplicate.
    Must not modify the array, must use O(1) extra space.

    Input:  [1, 3, 4, 2, 2]
    Output: 2

    Input:  [3, 1, 3, 4, 2]
    Output: 3

    Approach (Floyd's cycle detection on the array treated as a linked list):
    - Index i links to nums[i]
    - Cycle must exist because of the duplicate
    - Phase 1: find meeting point inside cycle
    - Phase 2: find cycle entry = duplicate

    Complexity:
    - Time: O(n)
    - Space: O(1)

    Debugging steps:
    1. Print slow and fast at each phase 1 step
    2. Print slow and finder at each phase 2 step
    """
    slow = nums[0]
    fast = nums[0]

    # Phase 1: detect cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: find entry point
    finder = nums[0]
    while finder != slow:
        finder = nums[finder]
        slow = nums[slow]

    return slow


# ---------------------------------------------------------------------------
# 24. Convert Binary Number in Linked List to Integer
# ---------------------------------------------------------------------------

def get_decimal_value(head: Optional[ListNode]) -> int:
    """
    Problem:
    A linked list represents a binary number (most significant bit first).
    Return the decimal value.

    Input:  1 -> 0 -> 1
    Output: 5  (binary 101 = 5)

    Input:  1 -> 1 -> 1 -> 0 -> 1
    Output: 29

    Approach:
    - Start with result = 0
    - For each node: result = result * 2 + node.value (left-shift and OR)

    Complexity:
    - Time: O(n)
    - Space: O(1)

    Debugging steps:
    1. Print result after each node
    """
    result = 0
    current = head

    while current:
        result = result * 2 + current.value
        current = current.next

    return result


# ---------------------------------------------------------------------------
# 25. LRU Cache (doubly linked list + hash map)
# ---------------------------------------------------------------------------

class _LRUNode:
    def __init__(self, key: int = 0, value: int = 0) -> None:
        self.key = key
        self.value = value
        self.prev: Optional["_LRUNode"] = None
        self.next: Optional["_LRUNode"] = None


class LRUCache:
    """
    Problem:
    Design a data structure that follows LRU (Least Recently Used) cache.
    Both get and put must run in O(1) time.

    Example:
    cache = LRUCache(2)
    cache.put(1, 1)    # cache: {1:1}
    cache.put(2, 2)    # cache: {1:1, 2:2}
    cache.get(1)       # returns 1, cache: {2:2, 1:1}
    cache.put(3, 3)    # evicts key 2, cache: {1:1, 3:3}
    cache.get(2)       # returns -1 (not found)

    Approach:
    - Hash map: key -> node (for O(1) lookup)
    - Doubly linked list: MRU at head, LRU at tail
    - On access or insert: move node to front
    - On capacity overflow: remove tail node

    Complexity:
    - Time: O(1) for get and put
    - Space: O(capacity)

    Debugging steps:
    1. Print cache contents and list order after each put/get
    2. Confirm evicted key is also removed from the map
    """

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: dict[int, _LRUNode] = {}
        self.head = _LRUNode()
        self.tail = _LRUNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: _LRUNode) -> None:
        node.prev.next = node.next  # type: ignore[union-attr]
        node.next.prev = node.prev  # type: ignore[union-attr]

    def _insert_front(self, node: _LRUNode) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node  # type: ignore[union-attr]
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = _LRUNode(key, value)
        self.cache[key] = node
        self._insert_front(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev  # type: ignore[assignment]
            self._remove(lru)
            del self.cache[lru.key]
