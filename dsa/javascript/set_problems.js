/*
Set and HashSet Problems
========================

Complete set of common interview problems that use Set, Map (HashSet/HashMap),
or set-theory operations (intersection, union, difference).

Quick input/output examples:
- `containsDuplicate([1,2,3,1]) -> true`
- `longestConsecutive([100,4,200,1,3,2]) -> 4`
- `firstMissingPositive([3,4,-1,1]) -> 2`
- `intersectionOfArrays([1,2,2,1],[2,2]) -> [2]`
- `repeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") -> ["AAAAACCCCC","CCCCCAAAAA"]`
- `subarraySumDivisibleK([4,5,0,-2,-3,1], 5) -> 7`
*/

// ---------------------------------------------------------------------------
// 1. Contains Duplicate
// ---------------------------------------------------------------------------

function containsDuplicate(nums) {
  /*
  Problem:
  Return true if any value appears more than once.

  Input:  [1,2,3,1]  Output: true
  Input:  [1,2,3,4]  Output: false

  Complexity: Time O(n), Space O(n)
  */
  const seen = new Set();
  for (const num of nums) {
    if (seen.has(num)) return true;
    seen.add(num);
  }
  return false;
}

// ---------------------------------------------------------------------------
// 2. Contains Duplicate II
// ---------------------------------------------------------------------------

function containsNearbyDuplicate(nums, k) {
  /*
  Problem:
  Return true if two equal elements are within k indices of each other.

  Input:  [1,2,3,1], k=3  Output: true
  Input:  [1,0,1,1], k=1  Output: true

  Complexity: Time O(n), Space O(k)

  Debugging steps:
  1. Print window set and current element each iteration
  */
  const window = new Set();
  for (let i = 0; i < nums.length; i += 1) {
    if (window.has(nums[i])) return true;
    window.add(nums[i]);
    if (window.size > k) window.delete(nums[i - k]);
  }
  return false;
}

// ---------------------------------------------------------------------------
// 3. Intersection of Two Arrays
// ---------------------------------------------------------------------------

function intersectionOfArrays(nums1, nums2) {
  /*
  Problem:
  Return unique elements present in both arrays.

  Input:  [1,2,2,1], [2,2]  Output: [2]
  Input:  [4,9,5], [9,4,9,8,4]  Output: [9,4]

  Complexity: Time O(n+m), Space O(n)
  */
  const set1 = new Set(nums1);
  return [...new Set(nums2.filter(n => set1.has(n)))];
}

// ---------------------------------------------------------------------------
// 4. Union of Two Arrays
// ---------------------------------------------------------------------------

function unionOfArrays(nums1, nums2) {
  /*
  Problem:
  Return all unique elements from both arrays combined.

  Input:  [1,2,3], [2,3,4,5]  Output: [1,2,3,4,5]

  Complexity: Time O(n+m), Space O(n+m)
  */
  return [...new Set([...nums1, ...nums2])].sort((a, b) => a - b);
}

// ---------------------------------------------------------------------------
// 5. Difference of Two Arrays
// ---------------------------------------------------------------------------

function findDifference(nums1, nums2) {
  /*
  Problem:
  Return [elements in nums1 not in nums2, elements in nums2 not in nums1].

  Input:  [1,2,3], [2,4,6]  Output: [[1,3],[4,6]]

  Complexity: Time O(n+m), Space O(n+m)
  */
  const set1 = new Set(nums1);
  const set2 = new Set(nums2);
  return [
    [...set1].filter(n => !set2.has(n)).sort((a, b) => a - b),
    [...set2].filter(n => !set1.has(n)).sort((a, b) => a - b),
  ];
}

// ---------------------------------------------------------------------------
// 6. Longest Consecutive Sequence
// ---------------------------------------------------------------------------

function longestConsecutive(nums) {
  /*
  Problem:
  Find the length of the longest consecutive integer sequence.

  Input:  [100,4,200,1,3,2]  Output: 4
  Input:  [0,3,7,2,5,8,4,6,0,1]  Output: 9

  Approach:
  - Build set of all numbers
  - Only start from sequence beginnings (num-1 not in set)

  Complexity: Time O(n), Space O(n)

  Debugging steps:
  1. Print when a sequence start is found
  2. Print each extension and final length
  */
  const numSet = new Set(nums);
  let best = 0;

  for (const num of numSet) {
    if (!numSet.has(num - 1)) {
      let length = 1;
      while (numSet.has(num + length)) length += 1;
      best = Math.max(best, length);
    }
  }

  return best;
}

// ---------------------------------------------------------------------------
// 7. Happy Number
// ---------------------------------------------------------------------------

function isHappy(n) {
  /*
  Problem:
  Return true if repeatedly summing squares of digits eventually reaches 1.

  Input:  19  Output: true
  Input:  2   Output: false

  Complexity: Time O(log n), Space O(log n)

  Debugging steps:
  1. Print n and next value each step
  2. Print when cycle detected
  */
  const digitSquareSum = x => {
    let total = 0;
    while (x > 0) {
      total += (x % 10) ** 2;
      x = Math.floor(x / 10);
    }
    return total;
  };

  const seen = new Set();
  while (n !== 1) {
    if (seen.has(n)) return false;
    seen.add(n);
    n = digitSquareSum(n);
  }
  return true;
}

// ---------------------------------------------------------------------------
// 8. Single Number
// ---------------------------------------------------------------------------

function singleNumber(nums) {
  /*
  Problem:
  Every element appears twice except one. Find it.

  Input:  [4,1,2,1,2]  Output: 4

  Approach (XOR): pairs cancel out, lone element remains.

  Complexity: Time O(n), Space O(1)
  */
  return nums.reduce((acc, n) => acc ^ n, 0);
}

function singleNumberSet(nums) {
  /*Set toggle approach — O(n) space.*/
  const seen = new Set();
  for (const num of nums) {
    if (seen.has(num)) seen.delete(num);
    else seen.add(num);
  }
  return [...seen][0];
}

// ---------------------------------------------------------------------------
// 9. Two Sum Using Set (existence check)
// ---------------------------------------------------------------------------

function twoSumExists(nums, target) {
  /*
  Problem:
  Return true if any two elements sum to target.

  Input:  [2,7,11,15], target=9  Output: true

  Complexity: Time O(n), Space O(n)
  */
  const seen = new Set();
  for (const num of nums) {
    if (seen.has(target - num)) return true;
    seen.add(num);
  }
  return false;
}

// ---------------------------------------------------------------------------
// 10. Jewels and Stones
// ---------------------------------------------------------------------------

function numJewelsInStones(jewels, stones) {
  /*
  Problem:
  Count how many characters in stones are in jewels.

  Input:  jewels="aA", stones="aAAbbbb"  Output: 3

  Complexity: Time O(j+s), Space O(j)
  */
  const jewelSet = new Set(jewels);
  return [...stones].filter(s => jewelSet.has(s)).length;
}

// ---------------------------------------------------------------------------
// 11. Distribute Candies
// ---------------------------------------------------------------------------

function distributeCandies(candyType) {
  /*
  Problem:
  Person can eat n/2 candies. Return maximum variety.

  Input:  [1,1,2,2,3,3]  Output: 3
  Input:  [1,1,2,3]      Output: 2

  Complexity: Time O(n), Space O(n)
  */
  return Math.min(new Set(candyType).size, candyType.length / 2);
}

// ---------------------------------------------------------------------------
// 12. Unique Email Addresses
// ---------------------------------------------------------------------------

function numUniqueEmails(emails) {
  /*
  Problem:
  Count unique emails after Gmail normalization (remove dots before @, ignore + suffix).

  Input:  ["test.email+alex@leetcode.com","test.e.mail+bob@leetcode.com","testemail+david@lee.tcode.com"]
  Output: 2

  Complexity: Time O(n*m), Space O(n)

  Debugging steps:
  1. Print each normalized email
  */
  const normalize = email => {
    const [local, domain] = email.split('@');
    return local.split('+')[0].replace(/\./g, '') + '@' + domain;
  };
  return new Set(emails.map(normalize)).size;
}

// ---------------------------------------------------------------------------
// 13. Uncommon Words from Two Sentences
// ---------------------------------------------------------------------------

function uncommonFromSentences(s1, s2) {
  /*
  Problem:
  Return words appearing exactly once across both sentences.

  Input:  s1="this apple is sweet", s2="this apple is sour"
  Output: ["sweet","sour"]

  Complexity: Time O(n+m), Space O(n+m)
  */
  const count = new Map();
  for (const word of [...s1.split(' '), ...s2.split(' ')]) {
    count.set(word, (count.get(word) || 0) + 1);
  }
  return [...count.entries()].filter(([, v]) => v === 1).map(([k]) => k);
}

// ---------------------------------------------------------------------------
// 14. Set Mismatch
// ---------------------------------------------------------------------------

function findErrorNums(nums) {
  /*
  Problem:
  One number appears twice, one is missing. Return [duplicate, missing].

  Input:  [1,2,2,4]  Output: [2,3]

  Complexity: Time O(n), Space O(n)

  Debugging steps:
  1. Print duplicate when found
  2. Print missing after scanning 1..n
  */
  const seen = new Set();
  let duplicate = -1;
  for (const num of nums) {
    if (seen.has(num)) duplicate = num;
    seen.add(num);
  }
  let missing = -1;
  for (let i = 1; i <= nums.length; i += 1) {
    if (!seen.has(i)) { missing = i; break; }
  }
  return [duplicate, missing];
}

// ---------------------------------------------------------------------------
// 15. Find All Duplicates in an Array
// ---------------------------------------------------------------------------

function findDuplicates(nums) {
  /*
  Problem:
  Find all elements appearing exactly twice (values in [1,n]).

  Input:  [4,3,2,7,8,2,3,1]  Output: [2,3]

  Approach (in-place sign marking):
  - Negate nums[abs(num)-1]; if already negative it's a duplicate

  Complexity: Time O(n), Space O(1)
  */
  const result = [];
  for (const num of nums) {
    const index = Math.abs(num) - 1;
    if (nums[index] < 0) result.push(Math.abs(num));
    else nums[index] = -nums[index];
  }
  return result;
}

// ---------------------------------------------------------------------------
// 16. First Missing Positive
// ---------------------------------------------------------------------------

function firstMissingPositive(nums) {
  /*
  Problem:
  Find the smallest positive integer not in nums.

  Input:  [3,4,-1,1]  Output: 2
  Input:  [1,2,0]     Output: 3

  Approach (set): O(n) space — add all, scan from 1.

  Complexity: Time O(n), Space O(n)
  */
  const numSet = new Set(nums);
  let i = 1;
  while (numSet.has(i)) i += 1;
  return i;
}

// ---------------------------------------------------------------------------
// 17. Valid Sudoku
// ---------------------------------------------------------------------------

function isValidSudoku(board) {
  /*
  Problem:
  Check if a 9×9 Sudoku board is valid.

  Complexity: Time O(1), Space O(1) — fixed 81 cells

  Debugging steps:
  1. Print which row/col/box caused a violation
  */
  const rows = Array.from({ length: 9 }, () => new Set());
  const cols = Array.from({ length: 9 }, () => new Set());
  const boxes = Array.from({ length: 9 }, () => new Set());

  for (let r = 0; r < 9; r += 1) {
    for (let c = 0; c < 9; c += 1) {
      const val = board[r][c];
      if (val === '.') continue;
      const boxIdx = Math.floor(r / 3) * 3 + Math.floor(c / 3);
      if (rows[r].has(val) || cols[c].has(val) || boxes[boxIdx].has(val)) return false;
      rows[r].add(val);
      cols[c].add(val);
      boxes[boxIdx].add(val);
    }
  }
  return true;
}

// ---------------------------------------------------------------------------
// 18. Word Pattern
// ---------------------------------------------------------------------------

function wordPattern(pattern, s) {
  /*
  Problem:
  Check if s follows pattern as a bijection.

  Input:  pattern="abba", s="dog cat cat dog"  Output: true
  Input:  pattern="abba", s="dog cat cat fish" Output: false

  Complexity: Time O(n), Space O(n)
  */
  const words = s.split(' ');
  if (pattern.length !== words.length) return false;

  const charToWord = new Map();
  const wordToChar = new Map();

  for (let i = 0; i < pattern.length; i += 1) {
    const ch = pattern[i];
    const word = words[i];
    if (charToWord.has(ch)) {
      if (charToWord.get(ch) !== word) return false;
    } else {
      if (wordToChar.has(word) && wordToChar.get(word) !== ch) return false;
      charToWord.set(ch, word);
      wordToChar.set(word, ch);
    }
  }
  return true;
}

// ---------------------------------------------------------------------------
// 19. Isomorphic Strings
// ---------------------------------------------------------------------------

function isIsomorphic(s, t) {
  /*
  Problem:
  Check if s and t have the same character-mapping structure.

  Input:  s="egg", t="add"    Output: true
  Input:  s="foo", t="bar"   Output: false

  Complexity: Time O(n), Space O(1)
  */
  const sToT = new Map();
  const tToS = new Map();

  for (let i = 0; i < s.length; i += 1) {
    const cs = s[i], ct = t[i];
    if (sToT.has(cs)) {
      if (sToT.get(cs) !== ct) return false;
    } else {
      if (tToS.has(ct) && tToS.get(ct) !== cs) return false;
      sToT.set(cs, ct);
      tToS.set(ct, cs);
    }
  }
  return true;
}

// ---------------------------------------------------------------------------
// 20. Palindrome Permutation
// ---------------------------------------------------------------------------

function canPermutePalindrome(s) {
  /*
  Problem:
  Check if any permutation of s is a palindrome.

  Input:  "tactcoa"  Output: true
  Input:  "code"     Output: false

  Approach:
  - At most one character can have odd frequency
  - Toggle characters in a set

  Complexity: Time O(n), Space O(1)
  */
  const odd = new Set();
  for (const ch of s) {
    if (odd.has(ch)) odd.delete(ch);
    else odd.add(ch);
  }
  return odd.size <= 1;
}

// ---------------------------------------------------------------------------
// 21. Group Anagrams
// ---------------------------------------------------------------------------

function groupAnagrams(strs) {
  /*
  Problem:
  Group strings that are anagrams of each other.

  Input:  ["eat","tea","tan","ate","nat","bat"]
  Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

  Complexity: Time O(n * k log k), Space O(n * k)
  */
  const groups = new Map();
  for (const word of strs) {
    const key = word.split('').sort().join('');
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(word);
  }
  return [...groups.values()];
}

// ---------------------------------------------------------------------------
// 22. Repeated DNA Sequences
// ---------------------------------------------------------------------------

function findRepeatedDnaSequences(s) {
  /*
  Problem:
  Find all 10-letter substrings appearing more than once.

  Input:  "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
  Output: ["AAAAACCCCC","CCCCCAAAAA"]

  Complexity: Time O(n), Space O(n)

  Debugging steps:
  1. Print each window and whether it was already seen
  */
  if (s.length < 10) return [];
  const seen = new Set();
  const repeated = new Set();

  for (let i = 0; i <= s.length - 10; i += 1) {
    const sub = s.slice(i, i + 10);
    if (seen.has(sub)) repeated.add(sub);
    else seen.add(sub);
  }
  return [...repeated];
}

// ---------------------------------------------------------------------------
// 23. Brick Wall
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

// ---------------------------------------------------------------------------
// 24. Minimum Steps to Make Two Strings Anagram
// ---------------------------------------------------------------------------

function minStepsToAnagram(s, t) {
  /*
  Problem:
  Minimum characters to change in t to make it an anagram of s.

  Input:  s="bab", t="aba"      Output: 1
  Input:  s="leetcode", t="practice" Output: 5

  Complexity: Time O(n), Space O(1)
  */
  const count = new Map();
  for (const ch of s) count.set(ch, (count.get(ch) || 0) + 1);
  for (const ch of t) count.set(ch, (count.get(ch) || 0) - 1);
  return [...count.values()].filter(v => v > 0).reduce((a, b) => a + b, 0);
}

// ---------------------------------------------------------------------------
// 25. Longest Substring Without Repeating Characters
// ---------------------------------------------------------------------------

function lengthOfLongestSubstring(s) {
  /*
  Problem:
  Find length of the longest substring with all unique characters.

  Input:  "abcabcbb"  Output: 3
  Input:  "pwwkew"   Output: 3

  Complexity: Time O(n), Space O(min(n, alphabet))

  Debugging steps:
  1. Print window set and current character each step
  */
  const charSet = new Set();
  let left = 0;
  let best = 0;

  for (let right = 0; right < s.length; right += 1) {
    while (charSet.has(s[right])) {
      charSet.delete(s[left]);
      left += 1;
    }
    charSet.add(s[right]);
    best = Math.max(best, right - left + 1);
  }

  return best;
}

// ---------------------------------------------------------------------------
// 26. Find Duplicate File in System
// ---------------------------------------------------------------------------

function findDuplicateFiles(paths) {
  /*
  Problem:
  Group file paths that have the same content.

  Input:  ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)"]
  Output: [["root/a/1.txt","root/c/3.txt"]]

  Complexity: Time O(n*m), Space O(n*m)
  */
  const contentMap = new Map();
  for (const pathInfo of paths) {
    const parts = pathInfo.split(' ');
    const dir = parts[0];
    for (let i = 1; i < parts.length; i += 1) {
      const parenIdx = parts[i].indexOf('(');
      const name = parts[i].slice(0, parenIdx);
      const content = parts[i].slice(parenIdx + 1, -1);
      if (!contentMap.has(content)) contentMap.set(content, []);
      contentMap.get(content).push(`${dir}/${name}`);
    }
  }
  return [...contentMap.values()].filter(g => g.length > 1);
}

// ---------------------------------------------------------------------------
// 27. Minimum Index Sum of Two Lists
// ---------------------------------------------------------------------------

function findRestaurant(list1, list2) {
  /*
  Problem:
  Find common items with minimum sum of indices from both lists.

  Input:
  list1=["Shogun","Tapioca Express","Burger King","KFC"]
  list2=["Piatti","The Grill","Hungry Hunter","Shogun"]
  Output: ["Shogun"]

  Complexity: Time O(n+m), Space O(n)
  */
  const indexMap = new Map(list1.map((item, i) => [item, i]));
  let minSum = Infinity;
  const result = [];

  for (let j = 0; j < list2.length; j += 1) {
    if (indexMap.has(list2[j])) {
      const total = indexMap.get(list2[j]) + j;
      if (total < minSum) {
        minSum = total;
        result.length = 0;
        result.push(list2[j]);
      } else if (total === minSum) {
        result.push(list2[j]);
      }
    }
  }
  return result;
}

// ---------------------------------------------------------------------------
// 28. Kth Largest Element in a Stream
// ---------------------------------------------------------------------------

class KthLargest {
  /*
  Problem:
  Design a class that finds the kth largest element in a live stream.

  Example:
  const kth = new KthLargest(3, [4,5,8,2]);
  kth.add(3) -> 4
  kth.add(5) -> 5

  Approach:
  - Min-heap of size k; top of heap = kth largest

  Complexity: add O(log k), init O(n log k)
  */
  constructor(k, nums) {
    this.k = k;
    this.heap = [];
    for (const num of nums) this.add(num);
  }

  add(val) {
    this._push(val);
    if (this.heap.length > this.k) this._pop();
    return this.heap[0];
  }

  _push(val) {
    this.heap.push(val);
    let i = this.heap.length - 1;
    while (i > 0) {
      const parent = Math.floor((i - 1) / 2);
      if (this.heap[parent] > this.heap[i]) {
        [this.heap[parent], this.heap[i]] = [this.heap[i], this.heap[parent]];
        i = parent;
      } else break;
    }
  }

  _pop() {
    this.heap[0] = this.heap.pop();
    let i = 0;
    while (true) {
      const left = 2 * i + 1, right = 2 * i + 2;
      let smallest = i;
      if (left < this.heap.length && this.heap[left] < this.heap[smallest]) smallest = left;
      if (right < this.heap.length && this.heap[right] < this.heap[smallest]) smallest = right;
      if (smallest === i) break;
      [this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]];
      i = smallest;
    }
  }
}

// ---------------------------------------------------------------------------
// 29. Top K Frequent Elements
// ---------------------------------------------------------------------------

function topKFrequent(nums, k) {
  /*
  Problem:
  Return the k most frequent elements.

  Input:  [1,1,1,2,2,3], k=2  Output: [1,2]

  Approach (bucket sort): index = frequency — O(n) time.

  Complexity: Time O(n), Space O(n)

  Debugging steps:
  1. Print frequency map
  2. Print bucket array
  */
  const freq = new Map();
  for (const num of nums) freq.set(num, (freq.get(num) || 0) + 1);

  const buckets = Array.from({ length: nums.length + 1 }, () => []);
  for (const [num, count] of freq) buckets[count].push(num);

  const result = [];
  for (let i = buckets.length - 1; i >= 1 && result.length < k; i -= 1) {
    result.push(...buckets[i]);
  }
  return result.slice(0, k);
}

// ---------------------------------------------------------------------------
// 30. Subarray Sum Divisible by K
// ---------------------------------------------------------------------------

function subarraySumDivisibleK(nums, k) {
  /*
  Problem:
  Count subarrays whose sum is divisible by k.

  Input:  [4,5,0,-2,-3,1], k=5  Output: 7

  Approach:
  - prefix % k; if same mod seen before, subarray between is divisible by k

  Complexity: Time O(n), Space O(k)

  Debugging steps:
  1. Print prefix sum, mod, and map lookup each step
  */
  const remainderCount = new Map([[0, 1]]);
  let prefixSum = 0;
  let count = 0;

  for (const num of nums) {
    prefixSum += num;
    let mod = ((prefixSum % k) + k) % k; // handle negative mod
    count += remainderCount.get(mod) || 0;
    remainderCount.set(mod, (remainderCount.get(mod) || 0) + 1);
  }

  return count;
}
