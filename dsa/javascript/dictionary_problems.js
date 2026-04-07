/*
Dictionary and HashMap Problems
================================

Complete set of common interview problems using Map (HashMap/Dictionary)
or frequency counting as the core data structure.

Quick input/output examples:
- `twoSum([2,7,11,15], 9) -> [0, 1]`
- `validAnagram("anagram","nagaram") -> true`
- `subarraySumK([1,1,1], 2) -> 2`
- `longestSubarraySumK([1,-1,5,-2,3], 3) -> 4`
- `minWindow("ADOBECODEBANC","ABC") -> "BANC"`
- `taskScheduler(["A","A","A","B","B","B"], 2) -> 8`
- `reorganizeString("aab") -> "aba"`
*/

// ---------------------------------------------------------------------------
// 1. Two Sum
// ---------------------------------------------------------------------------

function twoSum(nums, target) {
  /*
  Problem:
  Return indices of two numbers that sum to target.

  Input:  [2,7,11,15], target=9   Output: [0,1]

  Complexity: Time O(n), Space O(n)

  Debugging steps:
  1. Print current number and complement
  2. Print map before insertion
  */
  const seen = new Map();
  for (let i = 0; i < nums.length; i += 1) {
    const complement = target - nums[i];
    if (seen.has(complement)) return [seen.get(complement), i];
    seen.set(nums[i], i);
  }
  return [];
}

// ---------------------------------------------------------------------------
// 2. Valid Anagram
// ---------------------------------------------------------------------------

function validAnagram(s, t) {
  /*
  Problem:
  Check if t is an anagram of s.

  Input:  s="anagram", t="nagaram"  Output: true
  Input:  s="rat", t="car"          Output: false

  Complexity: Time O(n), Space O(1)
  */
  if (s.length !== t.length) return false;
  const count = new Map();
  for (const ch of s) count.set(ch, (count.get(ch) || 0) + 1);
  for (const ch of t) {
    if (!count.get(ch)) return false;
    count.set(ch, count.get(ch) - 1);
  }
  return true;
}

// ---------------------------------------------------------------------------
// 3. Ransom Note
// ---------------------------------------------------------------------------

function canConstruct(ransomNote, magazine) {
  /*
  Problem:
  Check if ransomNote can be built from characters in magazine.

  Input:  ransomNote="aa", magazine="aab"  Output: true
  Input:  ransomNote="aa", magazine="ab"   Output: false

  Complexity: Time O(n+m), Space O(1)

  Debugging steps:
  1. Print magazine count map
  2. Print when a character runs out
  */
  const count = new Map();
  for (const ch of magazine) count.set(ch, (count.get(ch) || 0) + 1);
  for (const ch of ransomNote) {
    if (!count.get(ch)) return false;
    count.set(ch, count.get(ch) - 1);
  }
  return true;
}

// ---------------------------------------------------------------------------
// 4. Word Frequency Count
// ---------------------------------------------------------------------------

function wordFrequency(text) {
  /*
  Problem:
  Count occurrences of each word.

  Input:  "the cat sat on the mat"
  Output: {the:2, cat:1, sat:1, on:1, mat:1}

  Complexity: Time O(n), Space O(n)
  */
  const freq = new Map();
  for (const word of text.toLowerCase().split(' ')) {
    freq.set(word, (freq.get(word) || 0) + 1);
  }
  return freq;
}

// ---------------------------------------------------------------------------
// 5. First Unique Character in a String
// ---------------------------------------------------------------------------

function firstUniqChar(s) {
  /*
  Problem:
  Return index of first character appearing only once. -1 if none.

  Input:  "leetcode"  Output: 0
  Input:  "aabb"      Output: -1

  Complexity: Time O(n), Space O(1)
  */
  const freq = new Map();
  for (const ch of s) freq.set(ch, (freq.get(ch) || 0) + 1);
  for (let i = 0; i < s.length; i += 1) {
    if (freq.get(s[i]) === 1) return i;
  }
  return -1;
}

// ---------------------------------------------------------------------------
// 6. Top K Frequent Words
// ---------------------------------------------------------------------------

function topKFrequentWords(words, k) {
  /*
  Problem:
  Return k most frequent words; ties broken lexicographically.

  Input:  ["i","love","leetcode","i","love","coding"], k=2
  Output: ["i","love"]

  Complexity: Time O(n log n), Space O(n)
  */
  const freq = new Map();
  for (const w of words) freq.set(w, (freq.get(w) || 0) + 1);
  return [...freq.keys()]
    .sort((a, b) => freq.get(b) - freq.get(a) || a.localeCompare(b))
    .slice(0, k);
}

// ---------------------------------------------------------------------------
// 7. Majority Element
// ---------------------------------------------------------------------------

function majorityElement(nums) {
  /*
  Problem:
  Find element appearing more than n/2 times.

  Input:  [3,2,3]   Output: 3

  Approach (Boyer-Moore voting): O(1) space.

  Debugging steps:
  1. Print candidate and count each step
  */
  let candidate = 0;
  let count = 0;
  for (const num of nums) {
    if (count === 0) candidate = num;
    count += num === candidate ? 1 : -1;
  }
  return candidate;
}

// ---------------------------------------------------------------------------
// 8. Majority Element II
// ---------------------------------------------------------------------------

function majorityElementII(nums) {
  /*
  Problem:
  Find all elements appearing more than n/3 times.

  Input:  [3,2,3]                 Output: [3]
  Input:  [1,1,1,3,3,2,2,2]      Output: [1,2]

  Complexity: Time O(n), Space O(1)
  */
  let [cand1, cand2, cnt1, cnt2] = [0, 1, 0, 0];
  for (const num of nums) {
    if (num === cand1) cnt1 += 1;
    else if (num === cand2) cnt2 += 1;
    else if (cnt1 === 0) { cand1 = num; cnt1 = 1; }
    else if (cnt2 === 0) { cand2 = num; cnt2 = 1; }
    else { cnt1 -= 1; cnt2 -= 1; }
  }
  const threshold = Math.floor(nums.length / 3);
  return [cand1, cand2].filter(c => nums.filter(n => n === c).length > threshold);
}

// ---------------------------------------------------------------------------
// 9. Two Sum III – Data Structure Design
// ---------------------------------------------------------------------------

class TwoSumDS {
  /*
  Problem:
  add(num): add num to the structure.
  find(value): return true if any two numbers sum to value.

  Example:
  add(1), add(3), add(5)
  find(4) -> true   (1+3)
  find(7) -> false

  Complexity: add O(1), find O(n)
  */
  constructor() {
    this.numCount = new Map();
  }

  add(number) {
    this.numCount.set(number, (this.numCount.get(number) || 0) + 1);
  }

  find(value) {
    for (const num of this.numCount.keys()) {
      const complement = value - num;
      if (this.numCount.has(complement)) {
        if (complement !== num || this.numCount.get(num) > 1) return true;
      }
    }
    return false;
  }
}

// ---------------------------------------------------------------------------
// 10. Subarray Sum Equals K
// ---------------------------------------------------------------------------

function subarraySumK(nums, k) {
  /*
  Problem:
  Count subarrays whose sum equals k.

  Input:  [1,1,1], k=2   Output: 2
  Input:  [1,2,3], k=3   Output: 2

  Complexity: Time O(n), Space O(n)

  Debugging steps:
  1. Print prefixSum, lookup (prefixSum-k), count added each step
  */
  const prefixCount = new Map([[0, 1]]);
  let prefixSum = 0;
  let count = 0;
  for (const num of nums) {
    prefixSum += num;
    count += prefixCount.get(prefixSum - k) || 0;
    prefixCount.set(prefixSum, (prefixCount.get(prefixSum) || 0) + 1);
  }
  return count;
}

// ---------------------------------------------------------------------------
// 11. Longest Subarray with Sum K
// ---------------------------------------------------------------------------

function longestSubarraySumK(nums, k) {
  /*
  Problem:
  Length of longest subarray summing to k.

  Input:  [1,-1,5,-2,3], k=3   Output: 4
  Input:  [-2,-1,2,1], k=1     Output: 3

  Complexity: Time O(n), Space O(n)

  Debugging steps:
  1. Print prefixSum and firstOccurrence map each step
  */
  const firstOccurrence = new Map([[0, -1]]);
  let prefixSum = 0;
  let best = 0;
  for (let i = 0; i < nums.length; i += 1) {
    prefixSum += nums[i];
    if (firstOccurrence.has(prefixSum - k)) {
      best = Math.max(best, i - firstOccurrence.get(prefixSum - k));
    }
    if (!firstOccurrence.has(prefixSum)) firstOccurrence.set(prefixSum, i);
  }
  return best;
}

// ---------------------------------------------------------------------------
// 12. Binary Subarrays with Sum
// ---------------------------------------------------------------------------

function numSubarraysWithSum(nums, goal) {
  /*
  Problem:
  Count binary subarrays with sum = goal.

  Input:  [1,0,1,0,1], goal=2   Output: 4

  Complexity: Time O(n), Space O(n)
  */
  const prefixCount = new Map([[0, 1]]);
  let prefixSum = 0;
  let count = 0;
  for (const num of nums) {
    prefixSum += num;
    count += prefixCount.get(prefixSum - goal) || 0;
    prefixCount.set(prefixSum, (prefixCount.get(prefixSum) || 0) + 1);
  }
  return count;
}

// ---------------------------------------------------------------------------
// 13. Contiguous Array (equal 0s and 1s)
// ---------------------------------------------------------------------------

function findMaxLength(nums) {
  /*
  Problem:
  Longest subarray with equal 0s and 1s.

  Input:  [0,1,0,0,1,1,0]   Output: 6

  Approach: transform 0→-1, find longest subarray with sum=0

  Complexity: Time O(n), Space O(n)
  */
  const firstOccurrence = new Map([[0, -1]]);
  let balance = 0;
  let best = 0;
  for (let i = 0; i < nums.length; i += 1) {
    balance += nums[i] === 1 ? 1 : -1;
    if (firstOccurrence.has(balance)) {
      best = Math.max(best, i - firstOccurrence.get(balance));
    } else {
      firstOccurrence.set(balance, i);
    }
  }
  return best;
}

// ---------------------------------------------------------------------------
// 14. Word Count Engine
// ---------------------------------------------------------------------------

function wordCountEngine(text) {
  /*
  Problem:
  Count words and return sorted by frequency (desc), then original order.

  Input:  "practice makes perfect and perfect practice makes perfect"
  Output: [["perfect","3"],["practice","2"],["makes","2"],["and","1"]]

  Complexity: Time O(n log n), Space O(n)
  */
  const words = text.toLowerCase().split(' ');
  const freq = new Map();
  const order = new Map();
  words.forEach((w, i) => {
    freq.set(w, (freq.get(w) || 0) + 1);
    if (!order.has(w)) order.set(w, i);
  });
  return [...freq.keys()]
    .sort((a, b) => freq.get(b) - freq.get(a) || order.get(a) - order.get(b))
    .map(w => [w, String(freq.get(w))]);
}

// ---------------------------------------------------------------------------
// 15. LRU Cache
// ---------------------------------------------------------------------------

class LRUCache {
  /*
  Problem:
  O(1) get and put with LRU eviction.

  Example:
  put(1,1), put(2,2), get(1)->1, put(3,3) evicts 2, get(2)->-1

  Approach: Map (insertion-ordered in JS) acts as an ordered dict.

  Complexity: O(1) for both
  */
  constructor(capacity) {
    this.capacity = capacity;
    this.cache = new Map();
  }

  get(key) {
    if (!this.cache.has(key)) return -1;
    const val = this.cache.get(key);
    this.cache.delete(key);
    this.cache.set(key, val);
    return val;
  }

  put(key, value) {
    if (this.cache.has(key)) this.cache.delete(key);
    this.cache.set(key, value);
    if (this.cache.size > this.capacity) {
      this.cache.delete(this.cache.keys().next().value);
    }
  }
}

// ---------------------------------------------------------------------------
// 16. LFU Cache
// ---------------------------------------------------------------------------

class LFUCache {
  /*
  Problem:
  O(1) get and put with LFU eviction. Ties broken by LRU order.

  Approach:
  - keyValue: key->value
  - keyFreq: key->freq
  - freqKeys: freq->Map of keys (LRU ordering within same freq)
  - minFreq: current min frequency

  Complexity: O(1) for all
  */
  constructor(capacity) {
    this.capacity = capacity;
    this.keyValue = new Map();
    this.keyFreq = new Map();
    this.freqKeys = new Map();
    this.minFreq = 0;
  }

  _updateFreq(key) {
    const freq = this.keyFreq.get(key);
    this.freqKeys.get(freq).delete(key);
    if (this.freqKeys.get(freq).size === 0) {
      this.freqKeys.delete(freq);
      if (this.minFreq === freq) this.minFreq += 1;
    }
    this.keyFreq.set(key, freq + 1);
    if (!this.freqKeys.has(freq + 1)) this.freqKeys.set(freq + 1, new Map());
    this.freqKeys.get(freq + 1).set(key, true);
  }

  get(key) {
    if (!this.keyValue.has(key)) return -1;
    this._updateFreq(key);
    return this.keyValue.get(key);
  }

  put(key, value) {
    if (this.capacity <= 0) return;
    if (this.keyValue.has(key)) {
      this.keyValue.set(key, value);
      this._updateFreq(key);
    } else {
      if (this.keyValue.size >= this.capacity) {
        const evictKey = this.freqKeys.get(this.minFreq).keys().next().value;
        this.freqKeys.get(this.minFreq).delete(evictKey);
        if (this.freqKeys.get(this.minFreq).size === 0) this.freqKeys.delete(this.minFreq);
        this.keyValue.delete(evictKey);
        this.keyFreq.delete(evictKey);
      }
      this.keyValue.set(key, value);
      this.keyFreq.set(key, 1);
      if (!this.freqKeys.has(1)) this.freqKeys.set(1, new Map());
      this.freqKeys.get(1).set(key, true);
      this.minFreq = 1;
    }
  }
}

// ---------------------------------------------------------------------------
// 17. Group Shifted Strings
// ---------------------------------------------------------------------------

function groupStrings(strings) {
  /*
  Problem:
  Group strings in the same shift sequence.

  Input:  ["abc","bcd","acef","xyz","az","ba","a","z"]
  Output: [["abc","bcd","xyz"],["az","ba"],["acef"],["a","z"]]

  Complexity: Time O(n*m), Space O(n*m)

  Debugging steps:
  1. Print normalized key for each string
  */
  const groups = new Map();
  for (const s of strings) {
    const shift = s.charCodeAt(0);
    const key = s.split('').map(ch => ((ch.charCodeAt(0) - shift + 26) % 26)).join(',');
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(s);
  }
  return [...groups.values()];
}

// ---------------------------------------------------------------------------
// 18. Find All Anagrams in a String
// ---------------------------------------------------------------------------

function findAnagrams(s, p) {
  /*
  Problem:
  Return starting indices of all anagrams of p in s.

  Input:  s="cbaebabacd", p="abc"  Output: [0,6]
  Input:  s="abab", p="ab"         Output: [0,1,2]

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print window count and p count each slide
  */
  if (p.length > s.length) return [];
  const pCount = new Array(26).fill(0);
  const wCount = new Array(26).fill(0);
  const a = 'a'.charCodeAt(0);
  const result = [];

  for (let i = 0; i < p.length; i += 1) {
    pCount[p.charCodeAt(i) - a] += 1;
    wCount[s.charCodeAt(i) - a] += 1;
  }
  if (pCount.join(',') === wCount.join(',')) result.push(0);

  for (let i = p.length; i < s.length; i += 1) {
    wCount[s.charCodeAt(i) - a] += 1;
    wCount[s.charCodeAt(i - p.length) - a] -= 1;
    if (pCount.join(',') === wCount.join(',')) result.push(i - p.length + 1);
  }
  return result;
}

// ---------------------------------------------------------------------------
// 19. Minimum Window Substring
// ---------------------------------------------------------------------------

function minWindow(s, t) {
  /*
  Problem:
  Smallest window in s containing all chars of t.

  Input:  s="ADOBECODEBANC", t="ABC"  Output: "BANC"

  Complexity: Time O(n+m), Space O(n+m)

  Debugging steps:
  1. Print have/need and window bounds when shrinking
  */
  if (!t || !s) return '';
  const need = new Map();
  for (const ch of t) need.set(ch, (need.get(ch) || 0) + 1);
  const window = new Map();
  let have = 0;
  const required = need.size;
  let left = 0;
  let best = [Infinity, 0, 0];

  for (let right = 0; right < s.length; right += 1) {
    const ch = s[right];
    window.set(ch, (window.get(ch) || 0) + 1);
    if (need.has(ch) && window.get(ch) === need.get(ch)) have += 1;

    while (have === required) {
      if (right - left + 1 < best[0]) best = [right - left + 1, left, right];
      const lch = s[left];
      window.set(lch, window.get(lch) - 1);
      if (need.has(lch) && window.get(lch) < need.get(lch)) have -= 1;
      left += 1;
    }
  }
  return best[0] === Infinity ? '' : s.slice(best[1], best[2] + 1);
}

// ---------------------------------------------------------------------------
// 20. Longest Repeating Character Replacement
// ---------------------------------------------------------------------------

function characterReplacement(s, k) {
  /*
  Problem:
  Longest substring you can make all one character after at most k replacements.

  Input:  "AABABBA", k=1  Output: 4

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print maxFreq and window size each step
  */
  const freq = new Map();
  let left = 0;
  let maxFreq = 0;
  let best = 0;

  for (let right = 0; right < s.length; right += 1) {
    freq.set(s[right], (freq.get(s[right]) || 0) + 1);
    maxFreq = Math.max(maxFreq, freq.get(s[right]));

    while ((right - left + 1) - maxFreq > k) {
      freq.set(s[left], freq.get(s[left]) - 1);
      left += 1;
    }
    best = Math.max(best, right - left + 1);
  }
  return best;
}

// ---------------------------------------------------------------------------
// 21. Decode String
// ---------------------------------------------------------------------------

function decodeString(s) {
  /*
  Problem:
  Decode nested patterns like k[encoded_string].

  Input:  "3[a2[c]]"    Output: "accaccacc"
  Input:  "2[abc]3[cd]" Output: "abcabccdcdcd"

  Complexity: Time O(n * max_k), Space O(n)

  Debugging steps:
  1. Print stack and current string at each [ and ]
  */
  const stack = [];
  let current = '';
  let k = 0;

  for (const ch of s) {
    if (ch >= '0' && ch <= '9') {
      k = k * 10 + Number(ch);
    } else if (ch === '[') {
      stack.push([k, current]);
      current = '';
      k = 0;
    } else if (ch === ']') {
      const [repeat, prev] = stack.pop();
      current = prev + current.repeat(repeat);
    } else {
      current += ch;
    }
  }
  return current;
}

// ---------------------------------------------------------------------------
// 22. Evaluate Division
// ---------------------------------------------------------------------------

function calcEquation(equations, values, queries) {
  /*
  Problem:
  Given variable ratios, answer division queries.

  Input:
  equations=[["a","b"],["b","c"]], values=[2.0,3.0]
  queries=[["a","c"],["b","a"]]
  Output: [6.0, 0.5]

  Complexity: Time O((V+E)*Q), Space O(V+E)

  Debugging steps:
  1. Print adjacency map
  2. Print BFS queue and product each step
  */
  const graph = new Map();

  equations.forEach(([src, dst], i) => {
    if (!graph.has(src)) graph.set(src, new Map());
    if (!graph.has(dst)) graph.set(dst, new Map());
    graph.get(src).set(dst, values[i]);
    graph.get(dst).set(src, 1.0 / values[i]);
  });

  const bfs = (src, dst) => {
    if (!graph.has(src) || !graph.has(dst)) return -1.0;
    if (src === dst) return 1.0;
    const visited = new Set();
    const queue = [[src, 1.0]];
    while (queue.length) {
      const [node, product] = queue.shift();
      if (node === dst) return product;
      visited.add(node);
      for (const [neighbor, weight] of graph.get(node)) {
        if (!visited.has(neighbor)) queue.push([neighbor, product * weight]);
      }
    }
    return -1.0;
  };

  return queries.map(([s, d]) => bfs(s, d));
}

// ---------------------------------------------------------------------------
// 23. Task Scheduler
// ---------------------------------------------------------------------------

function taskScheduler(tasks, n) {
  /*
  Problem:
  Minimum time to run all tasks with cooldown n.

  Input:  ["A","A","A","B","B","B"], n=2  Output: 8
  Input:  ["A","A","A","B","B","B"], n=0  Output: 6

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print maxFreq, numMaxFreq, and formula result
  */
  const freq = new Map();
  for (const t of tasks) freq.set(t, (freq.get(t) || 0) + 1);
  const maxFreq = Math.max(...freq.values());
  const numMaxFreq = [...freq.values()].filter(v => v === maxFreq).length;
  return Math.max(tasks.length, (maxFreq - 1) * (n + 1) + numMaxFreq);
}

// ---------------------------------------------------------------------------
// 24. Reorganize String
// ---------------------------------------------------------------------------

function reorganizeString(s) {
  /*
  Problem:
  Rearrange so no two adjacent characters are the same.

  Input:  "aab"    Output: "aba"
  Input:  "aaab"   Output: ""

  Approach:
  - Max-heap by frequency; pop two most frequent, append each, push back

  Complexity: Time O(n log k), Space O(k)

  Debugging steps:
  1. Print heap and appended chars each iteration
  */
  const freq = new Map();
  for (const ch of s) freq.set(ch, (freq.get(ch) || 0) + 1);

  // Simple max-heap using sorted rebuild (small alphabet)
  const entries = [...freq.entries()].sort((a, b) => b[1] - a[1]);
  const result = [];

  while (entries.length >= 2) {
    entries.sort((a, b) => b[1] - a[1]);
    const [ch1, cnt1] = entries[0];
    const [ch2, cnt2] = entries[1];
    result.push(ch1, ch2);
    entries[0] = [ch1, cnt1 - 1];
    entries[1] = [ch2, cnt2 - 1];
    if (entries[0][1] === 0) entries.shift();
    else if (entries[1][1] === 0) entries.splice(1, 1);
  }

  if (entries.length === 1) {
    if (entries[0][1] > 1) return '';
    result.push(entries[0][0]);
  }

  return result.join('');
}

// ---------------------------------------------------------------------------
// 25. Hand of Straights
// ---------------------------------------------------------------------------

function isNStraightHand(hand, groupSize) {
  /*
  Problem:
  Check if cards can be grouped into consecutive sequences of size groupSize.

  Input:  [1,2,3,6,2,3,4,7,8], groupSize=3  Output: true
  Input:  [1,2,3,4,5], groupSize=4           Output: false

  Complexity: Time O(n log n), Space O(n)

  Debugging steps:
  1. Print count map after each group consumed
  */
  if (hand.length % groupSize !== 0) return false;
  const count = new Map();
  for (const card of hand) count.set(card, (count.get(card) || 0) + 1);
  const sorted = [...count.keys()].sort((a, b) => a - b);
  for (const card of sorted) {
    if (count.get(card) > 0) {
      const need = count.get(card);
      for (let i = 0; i < groupSize; i += 1) {
        if ((count.get(card + i) || 0) < need) return false;
        count.set(card + i, count.get(card + i) - need);
      }
    }
  }
  return true;
}

// ---------------------------------------------------------------------------
// 26. Frequency of Most Frequent Element
// ---------------------------------------------------------------------------

function maxFrequency(nums, k) {
  /*
  Problem:
  Max frequency for any element with at most k increments total.

  Input:  [1,2,4], k=5  Output: 3
  Input:  [1,4], k=5    Output: 2

  Complexity: Time O(n log n), Space O(1)

  Debugging steps:
  1. Print window sum, cost, and window size each step
  */
  nums.sort((a, b) => a - b);
  let left = 0;
  let windowSum = 0;
  let best = 0;

  for (let right = 0; right < nums.length; right += 1) {
    windowSum += nums[right];
    while (nums[right] * (right - left + 1) - windowSum > k) {
      windowSum -= nums[left];
      left += 1;
    }
    best = Math.max(best, right - left + 1);
  }
  return best;
}

// ---------------------------------------------------------------------------
// 27. Custom Sort String
// ---------------------------------------------------------------------------

function customSortString(order, s) {
  /*
  Problem:
  Sort s according to order string. Chars not in order placed at end.

  Input:  order="cba", s="abcd"   Output: "cbad"

  Complexity: Time O(n+m), Space O(n)
  */
  const freq = new Map();
  for (const ch of s) freq.set(ch, (freq.get(ch) || 0) + 1);
  const result = [];
  for (const ch of order) {
    if (freq.has(ch)) {
      result.push(ch.repeat(freq.get(ch)));
      freq.delete(ch);
    }
  }
  for (const [ch, cnt] of freq) result.push(ch.repeat(cnt));
  return result.join('');
}

// ---------------------------------------------------------------------------
// 28. Number of Atoms
// ---------------------------------------------------------------------------

function countOfAtoms(formula) {
  /*
  Problem:
  Parse a chemical formula and return sorted element counts.

  Input:  "H2O"       Output: "H2O"
  Input:  "Mg(OH)2"   Output: "H2MgO2"

  Complexity: Time O(n²), Space O(n)

  Debugging steps:
  1. Print stack and current map at each (, ), and element
  */
  const stack = [new Map()];
  let i = 0;
  const n = formula.length;

  while (i < n) {
    if (formula[i] === '(') {
      stack.push(new Map());
      i += 1;
    } else if (formula[i] === ')') {
      i += 1;
      let j = i;
      while (i < n && formula[i] >= '0' && formula[i] <= '9') i += 1;
      const multiplier = j < i ? Number(formula.slice(j, i)) : 1;
      const top = stack.pop();
      for (const [elem, cnt] of top) {
        const cur = stack[stack.length - 1];
        cur.set(elem, (cur.get(elem) || 0) + cnt * multiplier);
      }
    } else if (formula[i] >= 'A' && formula[i] <= 'Z') {
      let j = i + 1;
      while (j < n && formula[j] >= 'a' && formula[j] <= 'z') j += 1;
      const elem = formula.slice(i, j);
      i = j;
      let k = i;
      while (i < n && formula[i] >= '0' && formula[i] <= '9') i += 1;
      const count = k < i ? Number(formula.slice(k, i)) : 1;
      const cur = stack[stack.length - 1];
      cur.set(elem, (cur.get(elem) || 0) + count);
    } else {
      i += 1;
    }
  }

  const result = stack[0];
  return [...result.keys()]
    .sort()
    .map(elem => elem + (result.get(elem) > 1 ? result.get(elem) : ''))
    .join('');
}

// ---------------------------------------------------------------------------
// 29. Subarray Sum Divisible by K
// ---------------------------------------------------------------------------

function subarraySumDivisibleK(nums, k) {
  /*
  Problem:
  Count subarrays whose sum is divisible by k.

  Input:  [4,5,0,-2,-3,1], k=5  Output: 7

  Complexity: Time O(n), Space O(k)

  Debugging steps:
  1. Print prefix sum, mod, and map lookup each step
  */
  const remCount = new Map([[0, 1]]);
  let prefixSum = 0;
  let count = 0;
  for (const num of nums) {
    prefixSum += num;
    const mod = ((prefixSum % k) + k) % k;
    count += remCount.get(mod) || 0;
    remCount.set(mod, (remCount.get(mod) || 0) + 1);
  }
  return count;
}

// ---------------------------------------------------------------------------
// 30. Brick Wall
// ---------------------------------------------------------------------------

function leastBricks(wall) {
  /*
  Problem:
  Draw a vertical line crossing fewest bricks.

  Input:  [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
  Output: 2

  Complexity: Time O(n*w), Space O(n)

  Debugging steps:
  1. Print edge positions for each row
  2. Print edge frequency map after all rows
  */
  const edgeCount = new Map();
  for (const row of wall) {
    let pos = 0;
    for (let i = 0; i < row.length - 1; i += 1) {
      pos += row[i];
      edgeCount.set(pos, (edgeCount.get(pos) || 0) + 1);
    }
  }
  if (!edgeCount.size) return wall.length;
  return wall.length - Math.max(...edgeCount.values());
}
