"""
Set and HashSet Problems
========================

Complete set of common interview problems that use Set, HashSet,
or set-theory operations (intersection, union, difference).

Quick input/output examples:
- `contains_duplicate([1,2,3,1]) -> True`
- `longest_consecutive([100,4,200,1,3,2]) -> 4`
- `first_missing_positive([3,4,-1,1]) -> 2`
- `intersection_of_arrays([1,2,2,1],[2,2]) -> [2]`
- `repeated_dna_sequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") -> ["AAAAACCCCC","CCCCCAAAAA"]`
- `subarray_sum_divisible_k([4,5,0,-2,-3,1], 5) -> 7`
"""

import heapq
from collections import defaultdict, Counter


# ---------------------------------------------------------------------------
# 1. Contains Duplicate
# ---------------------------------------------------------------------------

def contains_duplicate(nums: list[int]) -> bool:
    """
    Problem:
    Return True if any value appears more than once.

    Input:  [1, 2, 3, 1]
    Output: True

    Input:  [1, 2, 3, 4]
    Output: False

    Approach:
    - Add to a set; if value already in set return True

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print element being added and whether it was already in the set
    """
    seen: set[int] = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# ---------------------------------------------------------------------------
# 2. Contains Duplicate II
# ---------------------------------------------------------------------------

def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    """
    Problem:
    Return True if any two equal elements are within k indices of each other.

    Input:  [1, 2, 3, 1], k=3
    Output: True

    Input:  [1, 0, 1, 1], k=1
    Output: True

    Approach:
    - Sliding window set of size k
    - If element already in window return True; add and trim window

    Complexity: Time O(n), Space O(k)

    Debugging steps:
    1. Print the window set and current element each iteration
    """
    window: set[int] = set()
    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        if len(window) > k:
            window.discard(nums[i - k])
    return False


# ---------------------------------------------------------------------------
# 3. Intersection of Two Arrays
# ---------------------------------------------------------------------------

def intersection_of_arrays(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Problem:
    Return unique elements present in both arrays.

    Input:  [1, 2, 2, 1], [2, 2]
    Output: [2]

    Input:  [4, 9, 5], [9, 4, 9, 8, 4]
    Output: [9, 4]

    Complexity: Time O(n + m), Space O(n)

    Debugging steps:
    1. Print set1 and set2 before intersection
    """
    return list(set(nums1) & set(nums2))


# ---------------------------------------------------------------------------
# 4. Union of Two Arrays
# ---------------------------------------------------------------------------

def union_of_arrays(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Problem:
    Return all unique elements from both arrays combined.

    Input:  [1, 2, 3], [2, 3, 4, 5]
    Output: [1, 2, 3, 4, 5]

    Complexity: Time O(n + m), Space O(n + m)
    """
    return sorted(set(nums1) | set(nums2))


# ---------------------------------------------------------------------------
# 5. Difference of Two Arrays
# ---------------------------------------------------------------------------

def find_difference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    """
    Problem:
    Return [elements in nums1 not in nums2, elements in nums2 not in nums1].

    Input:  [1, 2, 3], [2, 4, 6]
    Output: [[1, 3], [4, 6]]

    Complexity: Time O(n + m), Space O(n + m)

    Debugging steps:
    1. Print set1 - set2 and set2 - set1 separately
    """
    set1, set2 = set(nums1), set(nums2)
    return [sorted(set1 - set2), sorted(set2 - set1)]


# ---------------------------------------------------------------------------
# 6. Longest Consecutive Sequence
# ---------------------------------------------------------------------------

def longest_consecutive(nums: list[int]) -> int:
    """
    Problem:
    Find the length of the longest consecutive integer sequence.

    Input:  [100, 4, 200, 1, 3, 2]
    Output: 4   (sequence: 1, 2, 3, 4)

    Input:  [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    Output: 9

    Approach:
    - Build set of all numbers
    - Only start counting from sequence beginnings (num - 1 not in set)
    - Extend sequence count while num + length is in set

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print when a sequence start is found
    2. Print each extension step and the length reached
    """
    num_set = set(nums)
    best = 0

    for num in num_set:
        if num - 1 not in num_set:  # sequence start
            length = 1
            while num + length in num_set:
                length += 1
            best = max(best, length)

    return best


# ---------------------------------------------------------------------------
# 7. Happy Number
# ---------------------------------------------------------------------------

def is_happy(n: int) -> bool:
    """
    Problem:
    Repeatedly replace n with sum of squares of its digits.
    Return True if it reaches 1.

    Input:  19
    Output: True   (1² + 9² = 82 → 8²+2²=68 → ... → 1)

    Input:  2
    Output: False

    Approach:
    - Track visited sums in a set; if n repeats it's a cycle → False
    - Return True when n == 1

    Complexity: Time O(log n), Space O(log n)

    Debugging steps:
    1. Print n and the computed next value each step
    2. Print when a cycle is detected
    """
    def digit_square_sum(x: int) -> int:
        total = 0
        while x:
            total += (x % 10) ** 2
            x //= 10
        return total

    seen: set[int] = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = digit_square_sum(n)
    return True


# ---------------------------------------------------------------------------
# 8. Single Number
# ---------------------------------------------------------------------------

def single_number(nums: list[int]) -> int:
    """
    Problem:
    Every element appears twice except one. Find it.

    Input:  [4, 1, 2, 1, 2]
    Output: 4

    Approaches:
    A) XOR: O(1) space — XOR all elements; pairs cancel out
    B) Set toggle: add to set if not present, remove if present

    Complexity: Time O(n), Space O(1) for XOR

    Debugging steps:
    1. Print running XOR value at each step
    """
    result = 0
    for num in nums:
        result ^= num
    return result


def single_number_set(nums: list[int]) -> int:
    """Set toggle approach — O(n) space."""
    seen: set[int] = set()
    for num in nums:
        if num in seen:
            seen.discard(num)
        else:
            seen.add(num)
    return seen.pop()


# ---------------------------------------------------------------------------
# 9. Two Sum Using Set (existence check only)
# ---------------------------------------------------------------------------

def two_sum_exists(nums: list[int], target: int) -> bool:
    """
    Problem:
    Return True if any two elements sum to target.

    Input:  [2, 7, 11, 15], target=9
    Output: True

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print current number and its complement each step
    """
    seen: set[int] = set()
    for num in nums:
        if target - num in seen:
            return True
        seen.add(num)
    return False


# ---------------------------------------------------------------------------
# 10. Jewels and Stones
# ---------------------------------------------------------------------------

def num_jewels_in_stones(jewels: str, stones: str) -> int:
    """
    Problem:
    Count how many characters in stones are also in jewels.

    Input:  jewels="aA", stones="aAAbbbb"
    Output: 3

    Complexity: Time O(j + s), Space O(j)

    Debugging steps:
    1. Print each stone and whether it is in the jewels set
    """
    jewel_set = set(jewels)
    return sum(1 for s in stones if s in jewel_set)


# ---------------------------------------------------------------------------
# 11. Distribute Candies
# ---------------------------------------------------------------------------

def distribute_candies(candy_type: list[int]) -> int:
    """
    Problem:
    Person can eat n/2 candies. Return maximum variety they can eat.

    Input:  [1, 1, 2, 2, 3, 3]
    Output: 3

    Input:  [1, 1, 2, 3]
    Output: 2

    Approach:
    - Answer is min(distinct types, n // 2)

    Complexity: Time O(n), Space O(n)
    """
    return min(len(set(candy_type)), len(candy_type) // 2)


# ---------------------------------------------------------------------------
# 12. Unique Email Addresses
# ---------------------------------------------------------------------------

def num_unique_emails(emails: list[str]) -> int:
    """
    Problem:
    Count unique email addresses after Gmail-style normalization:
    - Remove dots before @
    - Ignore everything after + before @

    Input:  ["test.email+alex@leetcode.com","test.e.mail+bob@leetcode.com","testemail+david@lee.tcode.com"]
    Output: 2

    Complexity: Time O(n * m), Space O(n)

    Debugging steps:
    1. Print each normalized email as it is processed
    """
    def normalize(email: str) -> str:
        local, domain = email.split("@")
        local = local.split("+")[0].replace(".", "")
        return local + "@" + domain

    return len({normalize(e) for e in emails})


# ---------------------------------------------------------------------------
# 13. Uncommon Words from Two Sentences
# ---------------------------------------------------------------------------

def uncommon_from_sentences(s1: str, s2: str) -> list[str]:
    """
    Problem:
    Return words that appear exactly once across both sentences combined.

    Input:  s1="this apple is sweet", s2="this apple is sour"
    Output: ["sweet", "sour"]

    Complexity: Time O(n + m), Space O(n + m)

    Debugging steps:
    1. Print the combined word frequency map
    """
    count = Counter((s1 + " " + s2).split())
    return [word for word, freq in count.items() if freq == 1]


# ---------------------------------------------------------------------------
# 14. Set Mismatch
# ---------------------------------------------------------------------------

def find_error_nums(nums: list[int]) -> list[int]:
    """
    Problem:
    One number appears twice and one is missing. Return [duplicate, missing].

    Input:  [1, 2, 2, 4]
    Output: [2, 3]

    Approach:
    - Use a set: find duplicate while building, then scan 1..n for missing

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print duplicate when detected
    2. Print the missing number found in the scan
    """
    seen: set[int] = set()
    duplicate = -1
    for num in nums:
        if num in seen:
            duplicate = num
        seen.add(num)
    n = len(nums)
    missing = next(i for i in range(1, n + 1) if i not in seen)
    return [duplicate, missing]


# ---------------------------------------------------------------------------
# 15. Find All Duplicates in an Array
# ---------------------------------------------------------------------------

def find_duplicates(nums: list[int]) -> list[int]:
    """
    Problem:
    Find all elements that appear exactly twice (values in [1, n]).

    Input:  [4, 3, 2, 7, 8, 2, 3, 1]
    Output: [2, 3]

    Approaches:
    A) Set: O(n) space
    B) In-place sign marking: negate nums[abs(num)-1]; if already negative it's a duplicate

    Complexity (in-place): Time O(n), Space O(1)

    Debugging steps:
    1. Print index being negated and current array state
    """
    result: list[int] = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            result.append(abs(num))
        else:
            nums[index] = -nums[index]
    return result


# ---------------------------------------------------------------------------
# 16. First Missing Positive
# ---------------------------------------------------------------------------

def first_missing_positive(nums: list[int]) -> int:
    """
    Problem:
    Find the smallest positive integer not present in nums.

    Input:  [3, 4, -1, 1]
    Output: 2

    Input:  [1, 2, 0]
    Output: 3

    Approaches:
    A) Set: O(n) space — add all to set, scan from 1
    B) In-place bucket sort: swap nums[i] to index nums[i]-1

    Complexity (set): Time O(n), Space O(n)

    Debugging steps:
    1. Print the set before scanning
    2. Print each candidate checked
    """
    num_set = set(nums)
    i = 1
    while i in num_set:
        i += 1
    return i


def first_missing_positive_inplace(nums: list[int]) -> int:
    """In-place O(1) space approach."""
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            correct = nums[i] - 1
            nums[i], nums[correct] = nums[correct], nums[i]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1


# ---------------------------------------------------------------------------
# 17. Valid Sudoku
# ---------------------------------------------------------------------------

def is_valid_sudoku(board: list[list[str]]) -> bool:
    """
    Problem:
    Check if a 9×9 Sudoku board is valid.

    Rules:
    - Each row must have digits 1-9 without repetition
    - Each column must have digits 1-9 without repetition
    - Each of the nine 3×3 boxes must have digits 1-9 without repetition

    Complexity: Time O(1) — fixed 81 cells, Space O(1) — fixed sets

    Debugging steps:
    1. Print which row/column/box caused a violation
    """
    rows: list[set] = [set() for _ in range(9)]
    cols: list[set] = [set() for _ in range(9)]
    boxes: list[set] = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue
            box_idx = (r // 3) * 3 + (c // 3)
            if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                return False
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_idx].add(val)

    return True


# ---------------------------------------------------------------------------
# 18. Word Pattern
# ---------------------------------------------------------------------------

def word_pattern(pattern: str, s: str) -> bool:
    """
    Problem:
    Check whether s follows the same pattern (bijection) as pattern.

    Input:  pattern="abba", s="dog cat cat dog"
    Output: True

    Input:  pattern="abba", s="dog cat cat fish"
    Output: False

    Approach:
    - Two maps: char->word and word->char
    - Conflict in either direction → False

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print both maps after each character-word pair
    """
    words = s.split()
    if len(pattern) != len(words):
        return False

    char_to_word: dict[str, str] = {}
    word_to_char: dict[str, str] = {}

    for ch, word in zip(pattern, words):
        if ch in char_to_word:
            if char_to_word[ch] != word:
                return False
        else:
            if word in word_to_char and word_to_char[word] != ch:
                return False
            char_to_word[ch] = word
            word_to_char[word] = ch

    return True


# ---------------------------------------------------------------------------
# 19. Isomorphic Strings
# ---------------------------------------------------------------------------

def is_isomorphic(s: str, t: str) -> bool:
    """
    Problem:
    Check if s and t have the same character-mapping structure.

    Input:  s="egg", t="add"   Output: True
    Input:  s="foo", t="bar"   Output: False
    Input:  s="paper", t="title" Output: True

    Complexity: Time O(n), Space O(1) — at most 256 chars

    Debugging steps:
    1. Print both maps after each character pair
    """
    s_to_t: dict[str, str] = {}
    t_to_s: dict[str, str] = {}

    for cs, ct in zip(s, t):
        if cs in s_to_t:
            if s_to_t[cs] != ct:
                return False
        else:
            if ct in t_to_s and t_to_s[ct] != cs:
                return False
            s_to_t[cs] = ct
            t_to_s[ct] = cs

    return True


# ---------------------------------------------------------------------------
# 20. Palindrome Permutation
# ---------------------------------------------------------------------------

def can_permute_palindrome(s: str) -> bool:
    """
    Problem:
    Check if any permutation of s is a palindrome.

    Input:  "tactcoa"
    Output: True   (can form "tacocat")

    Input:  "code"
    Output: False

    Approach:
    - At most one character can have an odd frequency
    - Toggle characters in a set; if in set remove, else add

    Complexity: Time O(n), Space O(1) — at most 26 chars

    Debugging steps:
    1. Print the odd-frequency set after each character
    """
    odd_chars: set[str] = set()
    for ch in s:
        if ch in odd_chars:
            odd_chars.discard(ch)
        else:
            odd_chars.add(ch)
    return len(odd_chars) <= 1


# ---------------------------------------------------------------------------
# 21. Group Anagrams
# ---------------------------------------------------------------------------

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Problem:
    Group strings that are anagrams of each other.

    Input:  ["eat","tea","tan","ate","nat","bat"]
    Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

    Approach:
    - Key = sorted string (canonical form)
    - Group by key in a hash map

    Complexity: Time O(n * k log k), Space O(n * k)

    Debugging steps:
    1. Print the key for each string
    """
    groups: dict[str, list[str]] = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())


# ---------------------------------------------------------------------------
# 22. Repeated DNA Sequences
# ---------------------------------------------------------------------------

def find_repeated_dna_sequences(s: str) -> list[str]:
    """
    Problem:
    Find all 10-letter substrings that appear more than once.

    Input:  "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    Output: ["AAAAACCCCC","CCCCCAAAAA"]

    Approach:
    - Slide a window of size 10
    - Add to seen; if already seen add to result set

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print each 10-char window and whether it was already seen
    """
    if len(s) < 10:
        return []

    seen: set[str] = set()
    repeated: set[str] = set()

    for i in range(len(s) - 9):
        sub = s[i:i + 10]
        if sub in seen:
            repeated.add(sub)
        seen.add(sub)

    return list(repeated)


# ---------------------------------------------------------------------------
# 23. Brick Wall
# ---------------------------------------------------------------------------

def least_bricks(wall: list[list[int]]) -> int:
    """
    Problem:
    Draw a vertical line through the wall crossing the fewest bricks.
    Edges at the start and end do not count.

    Input:  [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    Output: 2

    Approach:
    - Count positions of all internal edges (cumulative sums per row)
    - Most frequent edge position = fewest bricks crossed

    Complexity: Time O(n * w), Space O(n)

    Debugging steps:
    1. Print edge positions for each row
    2. Print the edge frequency map
    """
    edge_count: dict[int, int] = defaultdict(int)

    for row in wall:
        pos = 0
        for brick in row[:-1]:  # skip last edge
            pos += brick
            edge_count[pos] += 1

    if not edge_count:
        return len(wall)

    return len(wall) - max(edge_count.values())


# ---------------------------------------------------------------------------
# 24. Minimum Steps to Make Two Strings Anagram
# ---------------------------------------------------------------------------

def min_steps_to_anagram(s: str, t: str) -> int:
    """
    Problem:
    Return minimum number of characters to change in t to make it an anagram of s.

    Input:  s="bab", t="aba"
    Output: 1

    Input:  s="leetcode", t="practice"
    Output: 5

    Approach:
    - Count frequency difference
    - Sum of positive differences (characters s has more of than t)

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print the frequency counter difference
    """
    count = Counter(s)
    for ch in t:
        count[ch] -= 1
    return sum(max(0, v) for v in count.values())


# ---------------------------------------------------------------------------
# 25. Longest Substring Without Repeating Characters
# ---------------------------------------------------------------------------

def length_of_longest_substring(s: str) -> int:
    """
    Problem:
    Find the length of the longest substring with all unique characters.

    Input:  "abcabcbb"
    Output: 3

    Input:  "pwwkew"
    Output: 3

    Approach:
    - Sliding window using a character set
    - Shrink from left when duplicate detected

    Complexity: Time O(n), Space O(min(n, alphabet))

    Debugging steps:
    1. Print the window set and current element each step
    """
    char_set: set[str] = set()
    left = 0
    best = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.discard(s[left])
            left += 1
        char_set.add(s[right])
        best = max(best, right - left + 1)

    return best


# ---------------------------------------------------------------------------
# 26. Find Duplicate File in System
# ---------------------------------------------------------------------------

def find_duplicate(paths: list[str]) -> list[list[str]]:
    """
    Problem:
    Group file paths that have the same content.

    Input:  ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)"]
    Output: [["root/a/1.txt","root/c/3.txt"]]

    Complexity: Time O(n * m), Space O(n * m)

    Debugging steps:
    1. Print each parsed (content, path) pair
    """
    content_map: dict[str, list[str]] = defaultdict(list)

    for path_info in paths:
        parts = path_info.split()
        directory = parts[0]
        for file_info in parts[1:]:
            name, _, content = file_info.partition("(")
            content = content.rstrip(")")
            content_map[content].append(f"{directory}/{name}")

    return [group for group in content_map.values() if len(group) > 1]


# ---------------------------------------------------------------------------
# 27. Minimum Index Sum of Two Lists
# ---------------------------------------------------------------------------

def find_restaurant(list1: list[str], list2: list[str]) -> list[str]:
    """
    Problem:
    Find common items with the minimum sum of indices from both lists.

    Input:
    list1=["Shogun","Tapioca Express","Burger King","KFC"]
    list2=["Piatti","The Grill","Hungry Hunter","Shogun"]
    Output: ["Shogun"]

    Complexity: Time O(n + m), Space O(n)

    Debugging steps:
    1. Print index_map for list1
    2. Print each match in list2 and its combined index sum
    """
    index_map = {item: i for i, item in enumerate(list1)}
    min_sum = float("inf")
    result: list[str] = []

    for j, item in enumerate(list2):
        if item in index_map:
            total = index_map[item] + j
            if total < min_sum:
                min_sum = total
                result = [item]
            elif total == min_sum:
                result.append(item)

    return result


# ---------------------------------------------------------------------------
# 28. Kth Largest Element in a Stream
# ---------------------------------------------------------------------------

class KthLargest:
    """
    Problem:
    Design a class that finds the kth largest element in a live stream.

    Example:
    k=3, initial=[4,5,8,2]
    add(3) -> 4   (stream: [2,3,4,5,8], 3rd largest = 4)
    add(5) -> 5   (stream: [2,3,4,5,5,8], 3rd largest = 5)

    Approach:
    - Min-heap of size k
    - Top of heap is always the kth largest

    Complexity:
    - Init: O(n log k)
    - Add: O(log k)

    Debugging steps:
    1. Print heap after each add
    """

    def __init__(self, k: int, nums: list[int]) -> None:
        self.k = k
        self.heap: list[int] = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# ---------------------------------------------------------------------------
# 29. Top K Frequent Elements
# ---------------------------------------------------------------------------

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Problem:
    Return the k most frequent elements.

    Input:  [1,1,1,2,2,3], k=2
    Output: [1,2]

    Approaches:
    A) Heap: build freq map, push to min-heap of size k — O(n log k)
    B) Bucket sort: index = frequency — O(n)

    Complexity (bucket sort): Time O(n), Space O(n)

    Debugging steps:
    1. Print frequency map
    2. Print bucket array after populating
    """
    freq = Counter(nums)
    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]

    for num, count in freq.items():
        buckets[count].append(num)

    result: list[int] = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result

    return result


# ---------------------------------------------------------------------------
# 30. Subarray Sum Divisible by K
# ---------------------------------------------------------------------------

def subarray_sum_divisible_k(nums: list[int], k: int) -> int:
    """
    Problem:
    Count subarrays whose sum is divisible by k.

    Input:  [4, 5, 0, -2, -3, 1], k=5
    Output: 7

    Approach:
    - prefix_sum % k: if same remainder seen before, the subarray between is divisible by k
    - Count of (current mod) in map = number of valid subarrays ending here

    Complexity: Time O(n), Space O(k)

    Debugging steps:
    1. Print prefix sum, mod value, and map lookup at each step
    """
    remainder_count: dict[int, int] = defaultdict(int)
    remainder_count[0] = 1
    prefix_sum = 0
    count = 0

    for num in nums:
        prefix_sum += num
        mod = prefix_sum % k
        count += remainder_count[mod]
        remainder_count[mod] += 1

    return count
