"""
Dictionary and HashMap Problems
================================

Complete set of common interview problems that use dict, Counter,
defaultdict, or OrderedDict as the core data structure.

Quick input/output examples:
- `two_sum([2,7,11,15], 9) -> [0, 1]`
- `valid_anagram("anagram","nagaram") -> True`
- `subarray_sum_k([1,1,1], 2) -> 2`
- `longest_subarray_sum_k([1,-1,5,-2,3], 3) -> 4`
- `min_window("ADOBECODEBANC","ABC") -> "BANC"`
- `task_scheduler(["A","A","A","B","B","B"], 2) -> 8`
- `reorganize_string("aab") -> "aba"`
"""

import heapq
from collections import Counter, defaultdict, OrderedDict
from typing import Optional


# ---------------------------------------------------------------------------
# 1. Two Sum
# ---------------------------------------------------------------------------

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Problem:
    Return indices of two numbers that sum to target.

    Input:  [2, 7, 11, 15], target=9
    Output: [0, 1]

    Approach:
    - dict: value -> index
    - For each number check if complement exists

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print current number and complement
    2. Print dict before insertion
    """
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# ---------------------------------------------------------------------------
# 2. Valid Anagram
# ---------------------------------------------------------------------------

def valid_anagram(s: str, t: str) -> bool:
    """
    Problem:
    Check if t is an anagram of s.

    Input:  s="anagram", t="nagaram"
    Output: True

    Input:  s="rat", t="car"
    Output: False

    Complexity: Time O(n), Space O(1) — at most 26 chars

    Debugging steps:
    1. Print Counter(s) and Counter(t) side by side
    """
    return Counter(s) == Counter(t)


# ---------------------------------------------------------------------------
# 3. Ransom Note
# ---------------------------------------------------------------------------

def can_construct(ransom_note: str, magazine: str) -> bool:
    """
    Problem:
    Check if ransomNote can be built using characters from magazine.

    Input:  ransomNote="aa", magazine="aab"
    Output: True

    Input:  ransomNote="aa", magazine="ab"
    Output: False

    Approach:
    - Build frequency map of magazine
    - Subtract each character of ransomNote; if count goes negative return False

    Complexity: Time O(n+m), Space O(1)

    Debugging steps:
    1. Print magazine count map
    2. Print when a character runs out
    """
    mag_count = Counter(magazine)
    for ch in ransom_note:
        if mag_count[ch] <= 0:
            return False
        mag_count[ch] -= 1
    return True


# ---------------------------------------------------------------------------
# 4. Word Frequency Count
# ---------------------------------------------------------------------------

def word_frequency(text: str) -> dict[str, int]:
    """
    Problem:
    Count how many times each word appears in text.

    Input:  "the cat sat on the mat"
    Output: {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}

    Complexity: Time O(n), Space O(n)
    """
    return dict(Counter(text.lower().split()))


# ---------------------------------------------------------------------------
# 5. First Unique Character in a String
# ---------------------------------------------------------------------------

def first_uniq_char(s: str) -> int:
    """
    Problem:
    Return index of the first character that appears only once. Return -1 if none.

    Input:  "leetcode"   Output: 0
    Input:  "aabb"       Output: -1

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print frequency map
    2. Print index as you scan for first count-1 char
    """
    freq = Counter(s)
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1


# ---------------------------------------------------------------------------
# 6. Top K Frequent Words
# ---------------------------------------------------------------------------

def top_k_frequent_words(words: list[str], k: int) -> list[str]:
    """
    Problem:
    Return k most frequent words. Ties broken lexicographically.

    Input:  ["i","love","leetcode","i","love","coding"], k=2
    Output: ["i","love"]

    Complexity: Time O(n log n), Space O(n)

    Debugging steps:
    1. Print frequency map
    2. Print sorting key for each word
    """
    freq = Counter(words)
    return sorted(freq.keys(), key=lambda w: (-freq[w], w))[:k]


# ---------------------------------------------------------------------------
# 7. Majority Element
# ---------------------------------------------------------------------------

def majority_element(nums: list[int]) -> int:
    """
    Problem:
    Find the element appearing more than n/2 times.

    Input:  [3, 2, 3]   Output: 3
    Input:  [2, 2, 1, 1, 1, 2, 2]  Output: 2

    Approaches:
    A) Counter: O(n) space
    B) Boyer-Moore voting: O(1) space

    Complexity (Boyer-Moore): Time O(n), Space O(1)

    Debugging steps:
    1. Print candidate and count at each step
    """
    candidate = 0
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate


# ---------------------------------------------------------------------------
# 8. Majority Element II
# ---------------------------------------------------------------------------

def majority_element_ii(nums: list[int]) -> list[int]:
    """
    Problem:
    Find all elements appearing more than n/3 times.

    Input:  [3, 2, 3]                   Output: [3]
    Input:  [1, 1, 1, 3, 3, 2, 2, 2]   Output: [1, 2]

    Approach:
    - At most 2 elements can appear > n/3 times
    - Two-candidate Boyer-Moore, then verify counts

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print candidates and their counts after each pass
    """
    cand1, cand2 = 0, 1
    cnt1, cnt2 = 0, 0

    for num in nums:
        if num == cand1:
            cnt1 += 1
        elif num == cand2:
            cnt2 += 1
        elif cnt1 == 0:
            cand1, cnt1 = num, 1
        elif cnt2 == 0:
            cand2, cnt2 = num, 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    threshold = len(nums) // 3
    return [c for c in (cand1, cand2) if nums.count(c) > threshold]


# ---------------------------------------------------------------------------
# 9. Two Sum III – Data Structure Design
# ---------------------------------------------------------------------------

class TwoSumDS:
    """
    Problem:
    Design a class that supports:
    - add(num): add num to internal data structure
    - find(value): return True if any two numbers sum to value

    Example:
    add(1), add(3), add(5)
    find(4) -> True  (1+3)
    find(7) -> False

    Complexity: add O(1), find O(n)

    Debugging steps:
    1. Print the num_count dict after each add
    2. Print complement lookup in find
    """

    def __init__(self) -> None:
        self.num_count: dict[int, int] = defaultdict(int)

    def add(self, number: int) -> None:
        self.num_count[number] += 1

    def find(self, value: int) -> bool:
        for num in self.num_count:
            complement = value - num
            if complement in self.num_count:
                if complement != num or self.num_count[num] > 1:
                    return True
        return False


# ---------------------------------------------------------------------------
# 10. Subarray Sum Equals K
# ---------------------------------------------------------------------------

def subarray_sum_k(nums: list[int], k: int) -> int:
    """
    Problem:
    Count subarrays whose sum equals k.

    Input:  [1, 1, 1], k=2   Output: 2
    Input:  [1, 2, 3], k=3   Output: 2

    Approach:
    - prefix_sum map: count[prefix_sum] += 1
    - If (prefix_sum - k) was seen, those subarrays contribute

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print prefix_sum, lookup (prefix_sum - k), and count added each step
    """
    prefix_count: dict[int, int] = defaultdict(int)
    prefix_count[0] = 1
    prefix_sum = 0
    count = 0
    for num in nums:
        prefix_sum += num
        count += prefix_count[prefix_sum - k]
        prefix_count[prefix_sum] += 1
    return count


# ---------------------------------------------------------------------------
# 11. Longest Subarray with Sum K
# ---------------------------------------------------------------------------

def longest_subarray_sum_k(nums: list[int], k: int) -> int:
    """
    Problem:
    Find the length of the longest subarray summing to k.

    Input:  [1, -1, 5, -2, 3], k=3   Output: 4
    Input:  [-2, -1, 2, 1], k=1       Output: 3

    Approach:
    - prefix_sum map storing FIRST occurrence index
    - If (prefix_sum - k) seen before, update max length

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print prefix_sum and first_occurrence map after each step
    """
    first_occurrence: dict[int, int] = {0: -1}
    prefix_sum = 0
    best = 0
    for i, num in enumerate(nums):
        prefix_sum += num
        if prefix_sum - k in first_occurrence:
            best = max(best, i - first_occurrence[prefix_sum - k])
        if prefix_sum not in first_occurrence:
            first_occurrence[prefix_sum] = i
    return best


# ---------------------------------------------------------------------------
# 12. Binary Subarrays with Sum
# ---------------------------------------------------------------------------

def num_subarrays_with_sum(nums: list[int], goal: int) -> int:
    """
    Problem:
    Count subarrays of 0s and 1s with sum equal to goal.

    Input:  [1, 0, 1, 0, 1], goal=2   Output: 4

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Same as subarray_sum_k — print prefix_sum and lookup
    """
    prefix_count: dict[int, int] = defaultdict(int)
    prefix_count[0] = 1
    prefix_sum = 0
    count = 0
    for num in nums:
        prefix_sum += num
        count += prefix_count[prefix_sum - goal]
        prefix_count[prefix_sum] += 1
    return count


# ---------------------------------------------------------------------------
# 13. Contiguous Array (equal 0s and 1s)
# ---------------------------------------------------------------------------

def find_max_length(nums: list[int]) -> int:
    """
    Problem:
    Find the longest subarray with equal number of 0s and 1s.

    Input:  [0, 1, 0, 0, 1, 1, 0]   Output: 6

    Approach:
    - Transform 0 → -1
    - Longest subarray with sum = 0 = longest prefix-sum balance seen before

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print running balance and first_occurrence map each step
    """
    first_occurrence: dict[int, int] = {0: -1}
    balance = 0
    best = 0
    for i, num in enumerate(nums):
        balance += 1 if num == 1 else -1
        if balance in first_occurrence:
            best = max(best, i - first_occurrence[balance])
        else:
            first_occurrence[balance] = i
    return best


# ---------------------------------------------------------------------------
# 14. Word Count Engine
# ---------------------------------------------------------------------------

def word_count_engine(text: str) -> list[list[str]]:
    """
    Problem:
    Count word occurrences; return sorted by frequency (desc), then original order.

    Input:  "practice makes perfect and perfect practice makes perfect"
    Output: [["perfect","3"],["practice","2"],["makes","2"],["and","1"]]

    Complexity: Time O(n log n), Space O(n)

    Debugging steps:
    1. Print frequency map
    2. Print the first-seen order map
    """
    words = text.lower().split()
    freq: dict[str, int] = {}
    order: dict[str, int] = {}
    for i, word in enumerate(words):
        freq[word] = freq.get(word, 0) + 1
        if word not in order:
            order[word] = i

    sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], order[w]))
    return [[w, str(freq[w])] for w in sorted_words]


# ---------------------------------------------------------------------------
# 15. LRU Cache
# ---------------------------------------------------------------------------

class LRUCache:
    """
    Problem:
    Design an LRU cache with O(1) get and put.

    Example:
    cache = LRUCache(2)
    cache.put(1, 1)    # {1:1}
    cache.put(2, 2)    # {1:1, 2:2}
    cache.get(1)       # 1  — now {2:2, 1:1}
    cache.put(3, 3)    # evicts 2 — {1:1, 3:3}
    cache.get(2)       # -1

    Approach:
    - OrderedDict: move_to_end on access/insert, popitem(last=False) to evict

    Complexity: O(1) for both get and put

    Debugging steps:
    1. Print OrderedDict contents after each operation
    """

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# ---------------------------------------------------------------------------
# 16. LFU Cache
# ---------------------------------------------------------------------------

class LFUCache:
    """
    Problem:
    Design an LFU cache — evict the least frequently used item.
    Ties broken by LRU order.

    Example:
    cache = LFUCache(2)
    cache.put(1,1), cache.put(2,2), cache.get(1)→1
    cache.put(3,3) — evicts 2, cache.get(2)→-1

    Approach:
    - key_value: key -> value
    - key_freq: key -> frequency
    - freq_keys: freq -> OrderedDict of keys (LRU within same frequency)
    - min_freq: current minimum frequency

    Complexity: O(1) for all operations

    Debugging steps:
    1. Print key_freq and freq_keys after each put/get
    2. Print evicted key and min_freq update
    """

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.key_value: dict[int, int] = {}
        self.key_freq: dict[int, int] = {}
        self.freq_keys: dict[int, OrderedDict] = defaultdict(OrderedDict)
        self.min_freq = 0

    def _update_freq(self, key: int) -> None:
        freq = self.key_freq[key]
        del self.freq_keys[freq][key]
        if not self.freq_keys[freq]:
            del self.freq_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.key_freq[key] = freq + 1
        self.freq_keys[freq + 1][key] = True

    def get(self, key: int) -> int:
        if key not in self.key_value:
            return -1
        self._update_freq(key)
        return self.key_value[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.key_value:
            self.key_value[key] = value
            self._update_freq(key)
        else:
            if len(self.key_value) >= self.capacity:
                evict_key, _ = self.freq_keys[self.min_freq].popitem(last=False)
                if not self.freq_keys[self.min_freq]:
                    del self.freq_keys[self.min_freq]
                del self.key_value[evict_key]
                del self.key_freq[evict_key]
            self.key_value[key] = value
            self.key_freq[key] = 1
            self.freq_keys[1][key] = True
            self.min_freq = 1


# ---------------------------------------------------------------------------
# 17. Group Shifted Strings
# ---------------------------------------------------------------------------

def group_strings(strings: list[str]) -> list[list[str]]:
    """
    Problem:
    Group strings that belong to the same shift sequence.

    Input:  ["abc","bcd","acef","xyz","az","ba","a","z"]
    Output: [["abc","bcd","xyz"],["az","ba"],["acef"],["a","z"]]

    Approach:
    - Normalize each string to start from 'a' using modular shift
    - Use normalized form as dict key

    Complexity: Time O(n * m), Space O(n * m)

    Debugging steps:
    1. Print the normalized key for each string
    """
    groups: dict[tuple, list[str]] = defaultdict(list)
    for s in strings:
        shift = ord(s[0])
        key = tuple((ord(ch) - shift) % 26 for ch in s)
        groups[key].append(s)
    return list(groups.values())


# ---------------------------------------------------------------------------
# 18. Find All Anagrams in a String
# ---------------------------------------------------------------------------

def find_anagrams(s: str, p: str) -> list[int]:
    """
    Problem:
    Return starting indices of all anagrams of p in s.

    Input:  s="cbaebabacd", p="abc"   Output: [0, 6]
    Input:  s="abab", p="ab"          Output: [0, 1, 2]

    Approach:
    - Fixed-size sliding window with character frequency dicts
    - Use a 'need' counter that tracks unmatched requirements

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print window_count and p_count after each slide
    """
    if len(p) > len(s):
        return []

    p_count = Counter(p)
    window = Counter(s[:len(p)])
    result = [0] if window == p_count else []

    for i in range(len(p), len(s)):
        right_ch = s[i]
        left_ch = s[i - len(p)]

        window[right_ch] += 1
        window[left_ch] -= 1
        if window[left_ch] == 0:
            del window[left_ch]

        if window == p_count:
            result.append(i - len(p) + 1)

    return result


# ---------------------------------------------------------------------------
# 19. Minimum Window Substring
# ---------------------------------------------------------------------------

def min_window(s: str, t: str) -> str:
    """
    Problem:
    Find the smallest window in s containing all characters of t.

    Input:  s="ADOBECODEBANC", t="ABC"   Output: "BANC"
    Input:  s="a", t="aa"               Output: ""

    Approach:
    - need: frequency map of t
    - have/need counters: shrink window once all chars satisfied

    Complexity: Time O(n + m), Space O(n + m)

    Debugging steps:
    1. Print have/need and window [left, right] when shrinking
    """
    if not t or not s:
        return ""

    need = Counter(t)
    have = 0
    required = len(need)
    window: dict[str, int] = {}
    left = 0
    best = (float("inf"), 0, 0)

    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1
        if ch in need and window[ch] == need[ch]:
            have += 1

        while have == required:
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right)
            left_ch = s[left]
            window[left_ch] -= 1
            if left_ch in need and window[left_ch] < need[left_ch]:
                have -= 1
            left += 1

    return "" if best[0] == float("inf") else s[best[1]: best[2] + 1]


# ---------------------------------------------------------------------------
# 20. Longest Repeating Character Replacement
# ---------------------------------------------------------------------------

def character_replacement(s: str, k: int) -> int:
    """
    Problem:
    Longest substring you can make all one character after at most k replacements.

    Input:  "AABABBA", k=1   Output: 4
    Input:  "ABAB", k=2      Output: 4

    Approach:
    - Sliding window with frequency map
    - Window is valid if (window_size - max_freq) <= k

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print max_freq and window size each step
    2. Print when window shrinks
    """
    freq: dict[str, int] = {}
    left = 0
    max_freq = 0
    best = 0

    for right, ch in enumerate(s):
        freq[ch] = freq.get(ch, 0) + 1
        max_freq = max(max_freq, freq[ch])

        while (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best


# ---------------------------------------------------------------------------
# 21. Decode String
# ---------------------------------------------------------------------------

def decode_string(s: str) -> str:
    """
    Problem:
    Decode nested patterns like k[encoded_string].

    Input:  "3[a2[c]]"    Output: "accaccacc"
    Input:  "2[abc]3[cd]" Output: "abcabccdcdcd"

    Approach:
    - Stack-based: push current string and multiplier on [, pop and repeat on ]

    Complexity: Time O(n * max_k), Space O(n)

    Debugging steps:
    1. Print stack and current string at each [ and ]
    """
    stack: list[tuple[int, str]] = []
    current = ""
    k = 0

    for ch in s:
        if ch.isdigit():
            k = k * 10 + int(ch)
        elif ch == "[":
            stack.append((k, current))
            current = ""
            k = 0
        elif ch == "]":
            repeat, prev = stack.pop()
            current = prev + repeat * current
        else:
            current += ch

    return current


# ---------------------------------------------------------------------------
# 22. Evaluate Division
# ---------------------------------------------------------------------------

def calc_equation(
    equations: list[list[str]],
    values: list[float],
    queries: list[list[str]],
) -> list[float]:
    """
    Problem:
    Given variable ratios, answer division queries.

    Input:
    equations=[["a","b"],["b","c"]], values=[2.0,3.0]
    queries=[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    Output: [6.0, 0.5, -1.0, 1.0, -1.0]

    Approach:
    - Build adjacency dict with edge weights
    - BFS/DFS for each query multiplying edge weights

    Complexity: Time O((V+E) * Q), Space O(V+E)

    Debugging steps:
    1. Print the adjacency dict
    2. Print BFS queue and product at each step
    """
    graph: dict[str, dict[str, float]] = defaultdict(dict)

    for (src, dst), val in zip(equations, values):
        graph[src][dst] = val
        graph[dst][src] = 1.0 / val

    def bfs(src: str, dst: str) -> float:
        if src not in graph or dst not in graph:
            return -1.0
        if src == dst:
            return 1.0
        visited: set[str] = set()
        queue = [(src, 1.0)]
        while queue:
            node, product = queue.pop(0)
            if node == dst:
                return product
            visited.add(node)
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    queue.append((neighbor, product * weight))
        return -1.0

    return [bfs(s, d) for s, d in queries]


# ---------------------------------------------------------------------------
# 23. Number of Atoms
# ---------------------------------------------------------------------------

def count_of_atoms(formula: str) -> str:
    """
    Problem:
    Parse a chemical formula and return atom counts in sorted order.

    Input:  "H2O"       Output: "H2O"
    Input:  "Mg(OH)2"   Output: "H2MgO2"
    Input:  "K4(ON(SO3)2)2" Output: "K4N2O14S4"

    Approach:
    - Stack of dicts: push on (, multiply and merge on )

    Complexity: Time O(n²), Space O(n)

    Debugging steps:
    1. Print the stack and current dict at each (, ), and element
    """
    stack: list[dict[str, int]] = [defaultdict(int)]
    i = 0
    n = len(formula)

    while i < n:
        if formula[i] == "(":
            stack.append(defaultdict(int))
            i += 1
        elif formula[i] == ")":
            i += 1
            j = i
            while i < n and formula[i].isdigit():
                i += 1
            multiplier = int(formula[j:i]) if j < i else 1
            top = stack.pop()
            for elem, cnt in top.items():
                stack[-1][elem] += cnt * multiplier
        elif formula[i].isupper():
            j = i + 1
            while j < n and formula[j].islower():
                j += 1
            elem = formula[i:j]
            i = j
            k = i
            while i < n and formula[i].isdigit():
                i += 1
            count = int(formula[k:i]) if k < i else 1
            stack[-1][elem] += count
        else:
            i += 1

    result = stack[0]
    return "".join(
        elem + (str(cnt) if cnt > 1 else "")
        for elem, cnt in sorted(result.items())
    )


# ---------------------------------------------------------------------------
# 24. Task Scheduler
# ---------------------------------------------------------------------------

def task_scheduler(tasks: list[str], n: int) -> int:
    """
    Problem:
    Return minimum time to execute all tasks with cooldown n between same tasks.

    Input:  ["A","A","A","B","B","B"], n=2   Output: 8
    Input:  ["A","A","A","B","B","B"], n=0   Output: 6

    Approach:
    - freq map + max-heap
    - Each cycle of (n+1) slots: execute most frequent tasks
    - If fewer tasks than n+1, pad with idle time

    Complexity: Time O(n * tasks), Space O(1) — at most 26 tasks

    Debugging steps:
    1. Print max_freq, num_max_freq, and formula result
    """
    freq = Counter(tasks)
    max_freq = max(freq.values())
    num_max_freq = sum(1 for f in freq.values() if f == max_freq)
    # Formula: (max_freq - 1) * (n + 1) + num_max_freq
    return max(len(tasks), (max_freq - 1) * (n + 1) + num_max_freq)


# ---------------------------------------------------------------------------
# 25. Reorganize String
# ---------------------------------------------------------------------------

def reorganize_string(s: str) -> str:
    """
    Problem:
    Rearrange s so no two adjacent characters are the same.
    Return "" if impossible.

    Input:  "aab"    Output: "aba"
    Input:  "aaab"   Output: ""

    Approach:
    - Max-heap by frequency
    - Pop top two most frequent, append one each, push back if remaining

    Complexity: Time O(n log k), Space O(k)

    Debugging steps:
    1. Print heap contents each iteration
    2. Print appended characters
    """
    freq = Counter(s)
    max_heap = [(-cnt, ch) for ch, cnt in freq.items()]
    heapq.heapify(max_heap)

    result: list[str] = []

    while len(max_heap) >= 2:
        cnt1, ch1 = heapq.heappop(max_heap)
        cnt2, ch2 = heapq.heappop(max_heap)
        result.extend([ch1, ch2])
        if cnt1 + 1 < 0:
            heapq.heappush(max_heap, (cnt1 + 1, ch1))
        if cnt2 + 1 < 0:
            heapq.heappush(max_heap, (cnt2 + 1, ch2))

    if max_heap:
        cnt, ch = max_heap[0]
        if -cnt > 1:
            return ""
        result.append(ch)

    return "".join(result)


# ---------------------------------------------------------------------------
# 26. Hand of Straights
# ---------------------------------------------------------------------------

def is_n_straight_hand(hand: list[int], group_size: int) -> bool:
    """
    Problem:
    Check if cards can be grouped into consecutive sequences of length group_size.

    Input:  [1,2,3,6,2,3,4,7,8], group_size=3   Output: True
    Input:  [1,2,3,4,5], group_size=4            Output: False

    Approach:
    - Count frequencies, iterate sorted keys
    - For each smallest key, consume group_size consecutive cards

    Complexity: Time O(n log n), Space O(n)

    Debugging steps:
    1. Print count dict after each group is consumed
    """
    if len(hand) % group_size != 0:
        return False

    count = Counter(hand)
    for card in sorted(count):
        if count[card] > 0:
            need = count[card]
            for i in range(group_size):
                if count[card + i] < need:
                    return False
                count[card + i] -= need
    return True


# ---------------------------------------------------------------------------
# 27. Frequency of Most Frequent Element
# ---------------------------------------------------------------------------

def max_frequency(nums: list[int], k: int) -> int:
    """
    Problem:
    Max frequency achievable for any element with at most k total increments.

    Input:  [1,2,4], k=5   Output: 3
    Input:  [1,4], k=5     Output: 2

    Approach:
    - Sort, sliding window
    - Window [left, right]: cost to make all elements = nums[right]
      is nums[right]*window_size - window_sum
    - Shrink if cost > k

    Complexity: Time O(n log n), Space O(1)

    Debugging steps:
    1. Print left, right, window_sum, cost, and window_size each step
    """
    nums.sort()
    left = 0
    window_sum = 0
    best = 0

    for right in range(len(nums)):
        window_sum += nums[right]
        while nums[right] * (right - left + 1) - window_sum > k:
            window_sum -= nums[left]
            left += 1
        best = max(best, right - left + 1)

    return best


# ---------------------------------------------------------------------------
# 28. Custom Sort String
# ---------------------------------------------------------------------------

def custom_sort_string(order: str, s: str) -> str:
    """
    Problem:
    Sort s according to the character order defined in order.
    Characters not in order can be in any position.

    Input:  order="cba", s="abcd"   Output: "cbad"
    Input:  order="kqep", s="pekeq"  Output: "kqeep"

    Approach:
    - Count frequency of chars in s
    - Place chars in order first, then remaining chars

    Complexity: Time O(n + m), Space O(n)

    Debugging steps:
    1. Print freq map and order traversal
    """
    freq = Counter(s)
    result: list[str] = []
    for ch in order:
        result.append(ch * freq.pop(ch, 0))
    for ch, cnt in freq.items():
        result.append(ch * cnt)
    return "".join(result)


# ---------------------------------------------------------------------------
# 29. Word Pattern II (backtracking with dict)
# ---------------------------------------------------------------------------

def word_pattern_ii(pattern: str, s: str) -> bool:
    """
    Problem:
    Check if pattern can bijectively map to non-overlapping words in s.

    Input:  pattern="aabb", s="dogdogcatcat"   Output: True
    Input:  pattern="aabb", s="dogdogcatdog"   Output: False

    Approach:
    - Backtracking: try all splits at each step
    - Two dicts ensure bijection: char->word and word->char

    Complexity: Time O(n * m), Space O(n + m)

    Debugging steps:
    1. Print char, tried word, and both maps at each recursive step
    """
    def backtrack(
        pi: int,
        si: int,
        char_to_word: dict[str, str],
        word_to_char: dict[str, str],
    ) -> bool:
        if pi == len(pattern) and si == len(s):
            return True
        if pi == len(pattern) or si == len(s):
            return False

        ch = pattern[pi]
        if ch in char_to_word:
            word = char_to_word[ch]
            if not s[si:].startswith(word):
                return False
            return backtrack(pi + 1, si + len(word), char_to_word, word_to_char)

        for end in range(si + 1, len(s) + 1):
            word = s[si:end]
            if word in word_to_char:
                continue
            char_to_word[ch] = word
            word_to_char[word] = ch
            if backtrack(pi + 1, end, char_to_word, word_to_char):
                return True
            del char_to_word[ch]
            del word_to_char[word]

        return False

    return backtrack(0, 0, {}, {})


# ---------------------------------------------------------------------------
# 30. Brick Wall (frequency map)
# ---------------------------------------------------------------------------

def least_bricks(wall: list[list[int]]) -> int:
    """
    Problem:
    Draw a vertical line through the wall crossing fewest bricks.

    Input:  [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    Output: 2

    Approach:
    - Count internal edge positions (cumulative sum per row)
    - Position with most edges = fewest bricks crossed

    Complexity: Time O(n*w), Space O(n)

    Debugging steps:
    1. Print edge positions for each row
    2. Print the edge frequency map after processing all rows
    """
    edge_count: dict[int, int] = defaultdict(int)

    for row in wall:
        pos = 0
        for brick in row[:-1]:
            pos += brick
            edge_count[pos] += 1

    if not edge_count:
        return len(wall)

    return len(wall) - max(edge_count.values())
