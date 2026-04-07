/*
Tuple and Two-Pointer Problems
==============================

Problems that return pairs/triplets/quadruplets,
and problems solved with two-pointer or multi-pointer technique.

Quick input/output examples:
- `twoSumII([2,7,11,15], 9) -> [1,2]`
- `threeSum([-1,0,1,2,-1,-4]) -> [[-1,-1,2],[-1,0,1]]`
- `threeSumClosest([-1,2,1,-4], 1) -> 2`
- `fourSum([1,0,-1,0,-2,2], 0) -> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`
- `containerWithMostWater([1,8,6,2,5,4,8,3,7]) -> 49`
- `trap([0,1,0,2,1,0,1,3,2,1,2,1]) -> 6`
- `mergeIntervals([[1,3],[2,6],[8,10],[15,18]]) -> [[1,6],[8,10],[15,18]]`
- `subarraySumEqualsK([1,1,1], 2) -> 2`
*/

// ---------------------------------------------------------------------------
// 1. Two Sum (hash map — baseline)
// ---------------------------------------------------------------------------

function twoSum(nums, target) {
  /*
  Problem:
  Return indices of two numbers that sum to target.

  Input:  [2, 7, 11, 15], target=9
  Output: [0, 1]

  Complexity: Time O(n), Space O(n)

  Debugging steps:
  1. Print current number and complement
  2. Print map before insertion
  */
  const seen = new Map();
  for (let i = 0; i < nums.length; i += 1) {
    const complement = target - nums[i];
    if (seen.has(complement)) {
      return [seen.get(complement), i];
    }
    seen.set(nums[i], i);
  }
  return [];
}

// ---------------------------------------------------------------------------
// 2. Two Sum II – Sorted Array
// ---------------------------------------------------------------------------

function twoSumII(numbers, target) {
  /*
  Problem:
  Sorted array. Return 1-indexed pair summing to target.

  Input:  [2, 7, 11, 15], target=9
  Output: [1, 2]

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print left, right, and current sum
  */
  let left = 0;
  let right = numbers.length - 1;

  while (left < right) {
    const sum = numbers[left] + numbers[right];
    if (sum === target) return [left + 1, right + 1];
    if (sum < target) left += 1;
    else right -= 1;
  }
  return [];
}

// ---------------------------------------------------------------------------
// 3. 3Sum
// ---------------------------------------------------------------------------

function threeSum(nums) {
  /*
  Problem:
  Find all unique triplets summing to zero.

  Input:  [-1, 0, 1, 2, -1, -4]
  Output: [[-1,-1,2],[-1,0,1]]

  Approach:
  - Sort, fix one element, two pointers for rest
  - Skip duplicates at every level

  Complexity: Time O(n²), Space O(1) extra

  Debugging steps:
  1. Print fixed element and pointer values each iteration
  2. Print when duplicate is skipped
  */
  nums.sort((a, b) => a - b);
  const result = [];

  for (let i = 0; i < nums.length - 2; i += 1) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const total = nums[i] + nums[left] + nums[right];
      if (total === 0) {
        result.push([nums[i], nums[left], nums[right]]);
        while (left < right && nums[left] === nums[left + 1]) left += 1;
        while (left < right && nums[right] === nums[right - 1]) right -= 1;
        left += 1;
        right -= 1;
      } else if (total < 0) {
        left += 1;
      } else {
        right -= 1;
      }
    }
  }

  return result;
}

// ---------------------------------------------------------------------------
// 4. 3Sum Closest
// ---------------------------------------------------------------------------

function threeSumClosest(nums, target) {
  /*
  Problem:
  Find the triplet sum closest to target.

  Input:  [-1, 2, 1, -4], target=1
  Output: 2

  Complexity: Time O(n²), Space O(1)

  Debugging steps:
  1. Print current sum and distance from target
  2. Print when closest is updated
  */
  nums.sort((a, b) => a - b);
  let closest = nums[0] + nums[1] + nums[2];

  for (let i = 0; i < nums.length - 2; i += 1) {
    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];
      if (Math.abs(sum - target) < Math.abs(closest - target)) {
        closest = sum;
      }
      if (sum < target) left += 1;
      else if (sum > target) right -= 1;
      else return sum;
    }
  }

  return closest;
}

// ---------------------------------------------------------------------------
// 5. 4Sum
// ---------------------------------------------------------------------------

function fourSum(nums, target) {
  /*
  Problem:
  Find all unique quadruplets summing to target.

  Input:  [1, 0, -1, 0, -2, 2], target=0
  Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

  Complexity: Time O(n³), Space O(1) extra

  Debugging steps:
  1. Print i, j and pointer values each step
  2. Print when duplicates are skipped
  */
  nums.sort((a, b) => a - b);
  const result = [];
  const n = nums.length;

  for (let i = 0; i < n - 3; i += 1) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    for (let j = i + 1; j < n - 2; j += 1) {
      if (j > i + 1 && nums[j] === nums[j - 1]) continue;
      let left = j + 1;
      let right = n - 1;
      while (left < right) {
        const total = nums[i] + nums[j] + nums[left] + nums[right];
        if (total === target) {
          result.push([nums[i], nums[j], nums[left], nums[right]]);
          while (left < right && nums[left] === nums[left + 1]) left += 1;
          while (left < right && nums[right] === nums[right - 1]) right -= 1;
          left += 1;
          right -= 1;
        } else if (total < target) {
          left += 1;
        } else {
          right -= 1;
        }
      }
    }
  }

  return result;
}

// ---------------------------------------------------------------------------
// 6. Pair with Target Sum (Two Pointer on sorted)
// ---------------------------------------------------------------------------

function pairWithTargetSum(arr, target) {
  /*
  Problem:
  Given a sorted array, return indices of the pair summing to target.

  Input:  [1, 2, 3, 4, 6], target=6
  Output: [1, 3]

  Complexity: Time O(n), Space O(1)
  */
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    const sum = arr[left] + arr[right];
    if (sum === target) return [left, right];
    if (sum < target) left += 1;
    else right -= 1;
  }
  return [];
}

// ---------------------------------------------------------------------------
// 7. Count Pairs with Given Sum
// ---------------------------------------------------------------------------

function countPairsWithSum(arr, target) {
  /*
  Problem:
  Count all pairs summing to target.

  Input:  [1, 5, 7, -1, 5], target=6
  Output: 3

  Complexity: Time O(n), Space O(n)

  Debugging steps:
  1. Print current element and complement frequency
  */
  const freq = new Map();
  let count = 0;

  for (const num of arr) {
    const complement = target - num;
    count += freq.get(complement) || 0;
    freq.set(num, (freq.get(num) || 0) + 1);
  }

  return count;
}

// ---------------------------------------------------------------------------
// 8. Subarray with Given Sum (all positive)
// ---------------------------------------------------------------------------

function subarrayWithGivenSum(arr, target) {
  /*
  Problem:
  Find [start, end] of a contiguous subarray summing to target (positive elements).

  Input:  [1, 4, 20, 3, 10, 5], target=33
  Output: [2, 4]

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print window and current sum at each step
  */
  let left = 0;
  let currentSum = 0;

  for (let right = 0; right < arr.length; right += 1) {
    currentSum += arr[right];
    while (currentSum > target && left < right) {
      currentSum -= arr[left];
      left += 1;
    }
    if (currentSum === target) return [left, right];
  }
  return [];
}

// ---------------------------------------------------------------------------
// 9. Subarray Sum Equals K
// ---------------------------------------------------------------------------

function subarraySumEqualsK(nums, k) {
  /*
  Problem:
  Count subarrays whose sum equals k (array may have negatives).

  Input:  [1, 1, 1], k=2
  Output: 2

  Input:  [1, 2, 3], k=3
  Output: 2

  Approach:
  - Prefix sum + hash map
  - If (prefixSum - k) was seen before, those subarrays contribute

  Complexity: Time O(n), Space O(n)

  Debugging steps:
  1. Print prefix sum and lookup (prefixSum - k) each step
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
// 10. Container with Most Water
// ---------------------------------------------------------------------------

function containerWithMostWater(height) {
  /*
  Problem:
  Find two lines forming a container holding the most water.

  Input:  [1, 8, 6, 2, 5, 4, 8, 3, 7]
  Output: 49

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print left, right, and current area each step
  */
  let left = 0;
  let right = height.length - 1;
  let maxArea = 0;

  while (left < right) {
    const area = (right - left) * Math.min(height[left], height[right]);
    maxArea = Math.max(maxArea, area);
    if (height[left] <= height[right]) left += 1;
    else right -= 1;
  }

  return maxArea;
}

// ---------------------------------------------------------------------------
// 11. Trapping Rain Water
// ---------------------------------------------------------------------------

function trap(height) {
  /*
  Problem:
  Calculate total water trapped between walls.

  Input:  [0,1,0,2,1,0,1,3,2,1,2,1]
  Output: 6

  Approach (two pointers — O(1) space):
  - Track left_max and right_max
  - Process side with smaller max

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print left, right, leftMax, rightMax, and water added each step
  */
  let left = 0;
  let right = height.length - 1;
  let leftMax = 0;
  let rightMax = 0;
  let water = 0;

  while (left < right) {
    if (height[left] < height[right]) {
      if (height[left] >= leftMax) leftMax = height[left];
      else water += leftMax - height[left];
      left += 1;
    } else {
      if (height[right] >= rightMax) rightMax = height[right];
      else water += rightMax - height[right];
      right -= 1;
    }
  }

  return water;
}

// ---------------------------------------------------------------------------
// 12. Boats to Save People
// ---------------------------------------------------------------------------

function numRescueBoats(people, limit) {
  /*
  Problem:
  Minimum boats where each carries at most 2 people with total ≤ limit.

  Input:  [1, 2, 2, 3], limit=3
  Output: 3

  Complexity: Time O(n log n), Space O(1)

  Debugging steps:
  1. Print light, heavy, and whether they share a boat
  */
  people.sort((a, b) => a - b);
  let light = 0;
  let heavy = people.length - 1;
  let boats = 0;

  while (light <= heavy) {
    if (people[light] + people[heavy] <= limit) {
      light += 1;
    }
    heavy -= 1;
    boats += 1;
  }

  return boats;
}

// ---------------------------------------------------------------------------
// 13. Valid Triangle Number
// ---------------------------------------------------------------------------

function triangleNumber(nums) {
  /*
  Problem:
  Count triplets that can form a valid triangle.

  Input:  [2, 2, 3, 4]
  Output: 3

  Complexity: Time O(n²), Space O(1)

  Debugging steps:
  1. Print left, mid, fixed right and comparison
  */
  nums.sort((a, b) => a - b);
  let count = 0;

  for (let right = nums.length - 1; right >= 2; right -= 1) {
    let left = 0;
    let mid = right - 1;
    while (left < mid) {
      if (nums[left] + nums[mid] > nums[right]) {
        count += mid - left;
        mid -= 1;
      } else {
        left += 1;
      }
    }
  }

  return count;
}

// ---------------------------------------------------------------------------
// 14. Minimum Size Subarray Sum
// ---------------------------------------------------------------------------

function minSubarrayLen(target, nums) {
  /*
  Problem:
  Minimal length subarray with sum >= target.

  Input:  target=7, nums=[2,3,1,2,4,3]
  Output: 2

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print window bounds and sum when shrinking
  */
  let left = 0;
  let currentSum = 0;
  let minLen = Infinity;

  for (let right = 0; right < nums.length; right += 1) {
    currentSum += nums[right];
    while (currentSum >= target) {
      minLen = Math.min(minLen, right - left + 1);
      currentSum -= nums[left];
      left += 1;
    }
  }

  return minLen === Infinity ? 0 : minLen;
}

// ---------------------------------------------------------------------------
// 15. Sort Colors (Dutch National Flag)
// ---------------------------------------------------------------------------

function sortColors(nums) {
  /*
  Problem:
  Sort array of 0s, 1s, 2s in place, single pass.

  Input:  [2, 0, 2, 1, 1, 0]
  Output: [0, 0, 1, 1, 2, 2]

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print low, mid, high and array state at each swap
  */
  let low = 0;
  let mid = 0;
  let high = nums.length - 1;

  while (mid <= high) {
    if (nums[mid] === 0) {
      [nums[low], nums[mid]] = [nums[mid], nums[low]];
      low += 1;
      mid += 1;
    } else if (nums[mid] === 1) {
      mid += 1;
    } else {
      [nums[mid], nums[high]] = [nums[high], nums[mid]];
      high -= 1;
    }
  }
}

// ---------------------------------------------------------------------------
// 16. Move Zeros
// ---------------------------------------------------------------------------

function moveZeroes(nums) {
  /*
  Problem:
  Move all zeros to end, preserve relative order of non-zero elements.

  Input:  [0, 1, 0, 3, 12]
  Output: [1, 3, 12, 0, 0]

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print write pointer and element being moved
  */
  let write = 0;
  for (let read = 0; read < nums.length; read += 1) {
    if (nums[read] !== 0) {
      [nums[write], nums[read]] = [nums[read], nums[write]];
      write += 1;
    }
  }
}

// ---------------------------------------------------------------------------
// 17. Remove Duplicates from Sorted Array (keep one)
// ---------------------------------------------------------------------------

function removeDuplicates(nums) {
  /*
  Problem:
  Remove duplicates in place, return unique count.

  Input:  [1, 1, 2, 3, 3]
  Output: 3

  Complexity: Time O(n), Space O(1)
  */
  if (!nums.length) return 0;
  let k = 1;
  for (let i = 1; i < nums.length; i += 1) {
    if (nums[i] !== nums[i - 1]) {
      nums[k] = nums[i];
      k += 1;
    }
  }
  return k;
}

// ---------------------------------------------------------------------------
// 18. Remove Duplicates II (allow at most 2)
// ---------------------------------------------------------------------------

function removeDuplicatesII(nums) {
  /*
  Problem:
  Each element may appear at most twice.

  Input:  [1, 1, 1, 2, 2, 3]
  Output: 5

  Complexity: Time O(n), Space O(1)
  */
  let k = 2;
  for (let i = 2; i < nums.length; i += 1) {
    if (nums[i] !== nums[k - 2]) {
      nums[k] = nums[i];
      k += 1;
    }
  }
  return k;
}

// ---------------------------------------------------------------------------
// 19. Merge Intervals
// ---------------------------------------------------------------------------

function mergeIntervals(intervals) {
  /*
  Problem:
  Merge all overlapping intervals.

  Input:  [[1,3],[2,6],[8,10],[15,18]]
  Output: [[1,6],[8,10],[15,18]]

  Complexity: Time O(n log n), Space O(n)

  Debugging steps:
  1. Print each interval and whether it merges with previous
  */
  intervals.sort((a, b) => a[0] - b[0]);
  const merged = [];

  for (const interval of intervals) {
    if (merged.length && interval[0] <= merged[merged.length - 1][1]) {
      merged[merged.length - 1][1] = Math.max(merged[merged.length - 1][1], interval[1]);
    } else {
      merged.push([...interval]);
    }
  }

  return merged;
}

// ---------------------------------------------------------------------------
// 20. Insert Interval
// ---------------------------------------------------------------------------

function insertInterval(intervals, newInterval) {
  /*
  Problem:
  Insert newInterval into sorted non-overlapping list and merge.

  Input:  [[1,3],[6,9]], newInterval=[2,5]
  Output: [[1,5],[6,9]]

  Complexity: Time O(n), Space O(n)
  */
  const result = [];
  let i = 0;
  const n = intervals.length;

  while (i < n && intervals[i][1] < newInterval[0]) {
    result.push(intervals[i]);
    i += 1;
  }

  while (i < n && intervals[i][0] <= newInterval[1]) {
    newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
    newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
    i += 1;
  }

  result.push(newInterval);

  while (i < n) {
    result.push(intervals[i]);
    i += 1;
  }

  return result;
}

// ---------------------------------------------------------------------------
// 21. Non-Overlapping Intervals
// ---------------------------------------------------------------------------

function eraseOverlapIntervals(intervals) {
  /*
  Problem:
  Minimum intervals to remove so none overlap.

  Input:  [[1,2],[2,3],[3,4],[1,3]]
  Output: 1

  Complexity: Time O(n log n), Space O(1)

  Debugging steps:
  1. Print current interval and last kept end time
  */
  if (!intervals.length) return 0;
  intervals.sort((a, b) => a[1] - b[1]);
  let removeCount = 0;
  let lastEnd = intervals[0][1];

  for (let i = 1; i < intervals.length; i += 1) {
    if (intervals[i][0] < lastEnd) {
      removeCount += 1;
    } else {
      lastEnd = intervals[i][1];
    }
  }

  return removeCount;
}

// ---------------------------------------------------------------------------
// 22. Meeting Rooms (can attend all?)
// ---------------------------------------------------------------------------

function canAttendMeetings(intervals) {
  /*
  Problem:
  Return true if a person can attend all meetings.

  Input:  [[0,30],[5,10],[15,20]]
  Output: false

  Complexity: Time O(n log n), Space O(1)
  */
  intervals.sort((a, b) => a[0] - b[0]);
  for (let i = 1; i < intervals.length; i += 1) {
    if (intervals[i][0] < intervals[i - 1][1]) return false;
  }
  return true;
}

// ---------------------------------------------------------------------------
// 23. Meeting Rooms II (minimum rooms needed)
// ---------------------------------------------------------------------------

function minMeetingRooms(intervals) {
  /*
  Problem:
  Minimum conference rooms required.

  Input:  [[0,30],[5,10],[15,20]]
  Output: 2

  Approach:
  - Separate start and end arrays, sort both
  - Two pointers: count rooms in use

  Complexity: Time O(n log n), Space O(n)

  Debugging steps:
  1. Print starts and ends arrays
  2. Print rooms count at each step
  */
  if (!intervals.length) return 0;

  const starts = intervals.map(i => i[0]).sort((a, b) => a - b);
  const ends = intervals.map(i => i[1]).sort((a, b) => a - b);

  let rooms = 0;
  let endPtr = 0;

  for (let i = 0; i < starts.length; i += 1) {
    if (starts[i] < ends[endPtr]) {
      rooms += 1;
    } else {
      endPtr += 1;
    }
  }

  return rooms;
}

// ---------------------------------------------------------------------------
// 24. K-diff Pairs in an Array
// ---------------------------------------------------------------------------

function findKDiffPairs(nums, k) {
  /*
  Problem:
  Count unique k-diff pairs where |nums[i] - nums[j]| = k.

  Input:  [3, 1, 4, 1, 5], k=2
  Output: 2

  Complexity: Time O(n), Space O(n)

  Debugging steps:
  1. Print each num and whether pair exists
  */
  if (k < 0) return 0;

  const freq = new Map();
  for (const num of nums) {
    freq.set(num, (freq.get(num) || 0) + 1);
  }

  let count = 0;
  for (const num of freq.keys()) {
    if (k === 0) {
      if (freq.get(num) > 1) count += 1;
    } else {
      if (freq.has(num + k)) count += 1;
    }
  }

  return count;
}

// ---------------------------------------------------------------------------
// 25. Longest Mountain in Array
// ---------------------------------------------------------------------------

function longestMountain(arr) {
  /*
  Problem:
  Find the length of the longest mountain subarray.
  A mountain increases then decreases (at least one element each side).

  Input:  [2, 1, 4, 7, 3, 2, 5]
  Output: 5   (mountain: [1,4,7,3,2])

  Input:  [2, 2, 2]
  Output: 0

  Approach:
  - Walk left pointer forward
  - From each left, find peak, then valley

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print peak index and mountain boundaries
  */
  const n = arr.length;
  let left = 0;
  let result = 0;

  while (left + 2 < n) {
    let right = left + 1;
    if (arr[right - 1] < arr[right]) {
      while (right + 1 < n && arr[right] < arr[right + 1]) right += 1;
      if (right + 1 < n && arr[right] > arr[right + 1]) {
        while (right + 1 < n && arr[right] > arr[right + 1]) right += 1;
        result = Math.max(result, right - left + 1);
      }
      left = right;
    } else {
      left += 1;
    }
  }

  return result;
}

// ---------------------------------------------------------------------------
// 26. Two Sum Less Than K
// ---------------------------------------------------------------------------

function twoSumLessThanK(nums, k) {
  /*
  Problem:
  Return maximum sum of a pair where sum < k. Return -1 if none.

  Input:  [34,23,1,24,75,33,54,8], k=60
  Output: 58

  Input:  [10,20,30], k=15
  Output: -1

  Complexity: Time O(n log n), Space O(1)

  Debugging steps:
  1. Print left, right, sum, and best each step
  */
  nums.sort((a, b) => a - b);
  let left = 0;
  let right = nums.length - 1;
  let best = -1;

  while (left < right) {
    const sum = nums[left] + nums[right];
    if (sum < k) {
      best = Math.max(best, sum);
      left += 1;
    } else {
      right -= 1;
    }
  }

  return best;
}

// ---------------------------------------------------------------------------
// 27. Count Subarrays with Product Less Than K
// ---------------------------------------------------------------------------

function numSubarrayProductLessThanK(nums, k) {
  /*
  Problem:
  Count contiguous subarrays whose product is strictly less than k.

  Input:  [10, 5, 2, 6], k=100
  Output: 8

  Approach:
  - Sliding window with running product
  - Shrink from left when product >= k
  - count += right - left + 1

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print left, right, product, and count added each step
  */
  if (k <= 1) return 0;

  let product = 1;
  let left = 0;
  let count = 0;

  for (let right = 0; right < nums.length; right += 1) {
    product *= nums[right];
    while (product >= k && left <= right) {
      product = Math.floor(product / nums[left]);
      left += 1;
    }
    count += right - left + 1;
  }

  return count;
}

// ---------------------------------------------------------------------------
// 28. Max Consecutive Ones III
// ---------------------------------------------------------------------------

function longestOnes(nums, k) {
  /*
  Problem:
  Maximum consecutive 1s after flipping at most k zeros.

  Input:  [1,1,1,0,0,0,1,1,1,1,0], k=2
  Output: 6

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print window size and zero count each step
  */
  let left = 0;
  let zeroCount = 0;
  let best = 0;

  for (let right = 0; right < nums.length; right += 1) {
    if (nums[right] === 0) zeroCount += 1;
    while (zeroCount > k) {
      if (nums[left] === 0) zeroCount -= 1;
      left += 1;
    }
    best = Math.max(best, right - left + 1);
  }

  return best;
}

// ---------------------------------------------------------------------------
// 29. Longest Subarray of 1s After Deleting One Element
// ---------------------------------------------------------------------------

function longestSubarray(nums) {
  /*
  Problem:
  Delete exactly one element. Return longest subarray of 1s.

  Input:  [1,1,0,1]
  Output: 3

  Input:  [0,1,1,1,0,1,1,0,1]
  Output: 5

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print window and zero count when shrinking
  */
  let left = 0;
  let zeroCount = 0;
  let best = 0;

  for (let right = 0; right < nums.length; right += 1) {
    if (nums[right] === 0) zeroCount += 1;
    while (zeroCount > 1) {
      if (nums[left] === 0) zeroCount -= 1;
      left += 1;
    }
    best = Math.max(best, right - left); // subtract 1 for deleted element
  }

  return best;
}

// ---------------------------------------------------------------------------
// 30. Fruit Into Baskets (at Most 2 Distinct Values)
// ---------------------------------------------------------------------------

function totalFruit(fruits) {
  /*
  Problem:
  Max fruits in a contiguous pick with at most 2 fruit types.

  Input:  [1,2,1]     Output: 3
  Input:  [0,1,2,2]   Output: 3
  Input:  [1,2,3,2,2] Output: 4

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print basket map after each update
  */
  const basket = new Map();
  let left = 0;
  let best = 0;

  for (let right = 0; right < fruits.length; right += 1) {
    basket.set(fruits[right], (basket.get(fruits[right]) || 0) + 1);
    while (basket.size > 2) {
      const leftFruit = fruits[left];
      basket.set(leftFruit, basket.get(leftFruit) - 1);
      if (basket.get(leftFruit) === 0) basket.delete(leftFruit);
      left += 1;
    }
    best = Math.max(best, right - left + 1);
  }

  return best;
}

// ---------------------------------------------------------------------------
// 31. Maximum Points You Can Obtain from Cards
// ---------------------------------------------------------------------------

function maxScore(cardPoints, k) {
  /*
  Problem:
  Pick k cards from either end. Maximize total points.

  Input:  [1,2,3,4,5,6,1], k=3
  Output: 12

  Approach:
  - Total - min subarray of length (n - k)

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print window sum as it slides
  */
  const n = cardPoints.length;
  const windowSize = n - k;
  let windowSum = 0;
  for (let i = 0; i < windowSize; i += 1) windowSum += cardPoints[i];
  let minSum = windowSum;
  const total = cardPoints.reduce((a, b) => a + b, 0);

  for (let i = windowSize; i < n; i += 1) {
    windowSum += cardPoints[i] - cardPoints[i - windowSize];
    minSum = Math.min(minSum, windowSum);
  }

  return total - minSum;
}

// ---------------------------------------------------------------------------
// 32. Longest Continuous Subarray with Absolute Diff ≤ Limit
// ---------------------------------------------------------------------------

function longestSubarrayWithLimit(nums, limit) {
  /*
  Problem:
  Longest subarray where |max - min| <= limit.

  Input:  [8,2,4,7], limit=4   Output: 2
  Input:  [10,1,2,4,7,2], limit=5 Output: 4

  Approach:
  - Two monotonic deques for max and min
  - Shrink left when max - min > limit

  Complexity: Time O(n), Space O(n)
  */
  const maxDq = []; // indices, decreasing values
  const minDq = []; // indices, increasing values
  let left = 0;
  let best = 0;

  for (let right = 0; right < nums.length; right += 1) {
    while (maxDq.length && nums[maxDq[maxDq.length - 1]] <= nums[right]) maxDq.pop();
    maxDq.push(right);

    while (minDq.length && nums[minDq[minDq.length - 1]] >= nums[right]) minDq.pop();
    minDq.push(right);

    while (nums[maxDq[0]] - nums[minDq[0]] > limit) {
      left += 1;
      if (maxDq[0] < left) maxDq.shift();
      if (minDq[0] < left) minDq.shift();
    }

    best = Math.max(best, right - left + 1);
  }

  return best;
}

// ---------------------------------------------------------------------------
// 33. Squares of a Sorted Array
// ---------------------------------------------------------------------------

function sortedSquares(nums) {
  /*
  Problem:
  Return sorted squares of a sorted array.

  Input:  [-4,-1,0,3,10]
  Output: [0,1,9,16,100]

  Approach:
  - Two pointers from both ends
  - Largest square always at one end
  - Fill result right to left

  Complexity: Time O(n), Space O(n)

  Debugging steps:
  1. Print left, right, and chosen square each step
  */
  const n = nums.length;
  const result = new Array(n);
  let left = 0;
  let right = n - 1;
  let pos = n - 1;

  while (left <= right) {
    const sqLeft = nums[left] ** 2;
    const sqRight = nums[right] ** 2;
    if (sqLeft > sqRight) {
      result[pos] = sqLeft;
      left += 1;
    } else {
      result[pos] = sqRight;
      right -= 1;
    }
    pos -= 1;
  }

  return result;
}

// ---------------------------------------------------------------------------
// 34. Minimum Difference Between Highest and Lowest of K Scores
// ---------------------------------------------------------------------------

function minimumDifference(nums, k) {
  /*
  Problem:
  Choose k elements. Return minimum difference between max and min of those k.

  Input:  [9,4,1,7], k=2
  Output: 2

  Approach:
  - Sort, sliding window of size k

  Complexity: Time O(n log n), Space O(1)
  */
  nums.sort((a, b) => a - b);
  let best = Infinity;
  for (let i = 0; i <= nums.length - k; i += 1) {
    best = Math.min(best, nums[i + k - 1] - nums[i]);
  }
  return best;
}

// ---------------------------------------------------------------------------
// 35. Number of Subarrays with Bounded Maximum
// ---------------------------------------------------------------------------

function numSubarrayBoundedMax(nums, leftBound, rightBound) {
  /*
  Problem:
  Count subarrays where maximum element is in [leftBound, rightBound].

  Input:  [2,1,4,3], L=2, R=3
  Output: 3

  Approach:
  - count(max <= R) - count(max <= L-1)

  Complexity: Time O(n), Space O(1)
  */
  function countAtMost(bound) {
    let count = 0;
    let current = 0;
    for (const num of nums) {
      current = num <= bound ? current + 1 : 0;
      count += current;
    }
    return count;
  }

  return countAtMost(rightBound) - countAtMost(leftBound - 1);
}

// ---------------------------------------------------------------------------
// 36. Find All Anagrams in a String
// ---------------------------------------------------------------------------

function findAnagrams(s, p) {
  /*
  Problem:
  Return all start indices where anagram of p begins in s.

  Input:  s="cbaebabacd", p="abc"
  Output: [0,6]

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print window freq map vs target map each slide
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
// 37. Partition Array Such That Maximum Difference ≤ K
// ---------------------------------------------------------------------------

function partitionArray(nums, k) {
  /*
  Problem:
  Minimum subsequences so each subsequence's max - min <= k.

  Input:  [3,6,1,2,5], k=2
  Output: 2

  Complexity: Time O(n log n), Space O(1)

  Debugging steps:
  1. Print group start and element when new group begins
  */
  nums.sort((a, b) => a - b);
  let groups = 1;
  let groupStart = nums[0];

  for (let i = 1; i < nums.length; i += 1) {
    if (nums[i] - groupStart > k) {
      groups += 1;
      groupStart = nums[i];
    }
  }

  return groups;
}

// ---------------------------------------------------------------------------
// 38. Longest Turbulent Subarray
// ---------------------------------------------------------------------------

function maxTurbulenceSize(arr) {
  /*
  Problem:
  Longest turbulent subarray: alternating >, < pattern.

  Input:  [9,4,2,10,7,8,8,1,9]
  Output: 5

  Input:  [4,8,12,16]
  Output: 2

  Complexity: Time O(n), Space O(1)

  Debugging steps:
  1. Print sign (+1/-1) at each step
  2. Print when window resets
  */
  const n = arr.length;
  if (n < 2) return n;

  let best = 1;
  let left = 0;

  const cmp = (a, b) => (a > b ? 1 : a < b ? -1 : 0);

  for (let right = 1; right < n; right += 1) {
    const c = cmp(arr[right], arr[right - 1]);
    if (c === 0) {
      left = right;
    } else if (right > 1) {
      const prev = cmp(arr[right - 1], arr[right - 2]);
      if (c === prev) left = right - 1;
    }
    best = Math.max(best, right - left + 1);
  }

  return best;
}

// ---------------------------------------------------------------------------
// 39. Maximum Erasure Value (Longest Subarray with Unique Elements)
// ---------------------------------------------------------------------------

function maximumUniqueSubarray(nums) {
  /*
  Problem:
  Return the maximum sum of a subarray that contains only unique elements.

  Input:  [4,2,4,5,6]
  Output: 17   (subarray [2,4,5,6])

  Input:  [5,2,1,2,5,2,1,2,5]
  Output: 8    (subarray [5,2,1] or [1,2,5])

  Approach:
  - Sliding window with a Set
  - Shrink from left when a duplicate is added
  - Track running sum

  Complexity: Time O(n), Space O(n)

  Debugging steps:
  1. Print set contents and running sum at each step
  */
  const seen = new Set();
  let left = 0;
  let currentSum = 0;
  let best = 0;

  for (let right = 0; right < nums.length; right += 1) {
    while (seen.has(nums[right])) {
      seen.delete(nums[left]);
      currentSum -= nums[left];
      left += 1;
    }
    seen.add(nums[right]);
    currentSum += nums[right];
    best = Math.max(best, currentSum);
  }

  return best;
}

// ---------------------------------------------------------------------------
// 40. Maximum Sum of Two Non-Overlapping Subarrays
// ---------------------------------------------------------------------------

function maxSumTwoNoOverlap(nums, firstLen, secondLen) {
  /*
  Problem:
  Find the maximum sum of two non-overlapping subarrays of lengths firstLen and secondLen.

  Input:  [0,6,5,2,2,5,1,9,4], firstLen=1, secondLen=2
  Output: 20   (subarrays [9] and [6,5])

  Input:  [3,8,1,3,2,1,8,9,0], firstLen=3, secondLen=2
  Output: 29

  Approach:
  - Build prefix sums
  - Two passes: fix first window, find best second window before/after it

  Complexity: Time O(n), Space O(n)

  Debugging steps:
  1. Print prefix sums
  2. Print maxFirst and maxSecond as they update
  */
  const n = nums.length;
  const prefix = new Array(n + 1).fill(0);
  for (let i = 0; i < n; i += 1) prefix[i + 1] = prefix[i] + nums[i];

  const windowSum = (l, r) => prefix[r] - prefix[l];

  let best = 0;

  // Case 1: firstLen window comes before secondLen window
  let maxFirst = 0;
  for (let i = firstLen + secondLen; i <= n; i += 1) {
    maxFirst = Math.max(maxFirst, windowSum(i - firstLen - secondLen, i - secondLen));
    best = Math.max(best, maxFirst + windowSum(i - secondLen, i));
  }

  // Case 2: secondLen window comes before firstLen window
  let maxSecond = 0;
  for (let i = firstLen + secondLen; i <= n; i += 1) {
    maxSecond = Math.max(maxSecond, windowSum(i - firstLen - secondLen, i - firstLen));
    best = Math.max(best, maxSecond + windowSum(i - firstLen, i));
  }

  return best;
}
