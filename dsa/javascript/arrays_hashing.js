/*
Arrays and Hashing
==================

Common company-style questions:
1. Two Sum
2. Product of Array Except Self
3. Top K Frequent Elements

Quick input/output examples:
- `twoSumHashMap([2, 7, 11, 15], 9) -> [0, 1]`
- `productExceptSelfOptimized([1, 2, 3, 4]) -> [24, 12, 8, 6]`
- `topKFrequentHeap([1, 1, 1, 2, 2, 3], 2) -> [1, 2]`
*/

function twoSumBruteforce(nums, target) {
  /*
  Debugging steps:
  1. Print i, j, nums[i], nums[j]
  2. Check current sum against target
  3. Return indices, not values
  */
  for (let i = 0; i < nums.length; i += 1) {
    for (let j = i + 1; j < nums.length; j += 1) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
  return [];
}

function twoSumHashMap(nums, target) {
  /*
  Time: O(n)
  Space: O(n)
  */
  const seen = new Map();

  for (let index = 0; index < nums.length; index += 1) {
    const value = nums[index];
    const complement = target - value;
    if (seen.has(complement)) {
      return [seen.get(complement), index];
    }
    seen.set(value, index);
  }

  return [];
}

function productExceptSelf(nums) {
  /*
  Debugging steps:
  1. Print result after prefix pass
  2. Print suffix before each multiplication
  */
  const result = new Array(nums.length).fill(1);

  let prefix = 1;
  for (let i = 0; i < nums.length; i += 1) {
    result[i] = prefix;
    prefix *= nums[i];
  }

  let suffix = 1;
  for (let i = nums.length - 1; i >= 0; i -= 1) {
    result[i] *= suffix;
    suffix *= nums[i];
  }

  return result;
}

function topKFrequentSort(nums, k) {
  const frequency = new Map();

  for (const num of nums) {
    frequency.set(num, (frequency.get(num) || 0) + 1);
  }

  return [...frequency.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, k)
    .map(([value]) => value);
}

console.log("Two Sum:", twoSumHashMap([2, 7, 11, 15], 9));
console.log("Product Except Self:", productExceptSelf([1, 2, 3, 4]));
console.log("Top K Frequent:", topKFrequentSort([1, 1, 1, 2, 2, 3], 2));
