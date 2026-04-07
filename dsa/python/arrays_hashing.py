"""
Arrays and Hashing
==================

Common company-style questions in this topic:
1. Two Sum
2. Product of Array Except Self
3. Top K Frequent Elements

Why this topic matters:
- It tests lookup optimization
- It checks whether you can move from brute force to linear time
- It is one of the most common interview starting points

Quick input/output examples:
- `two_sum_hashmap([2, 7, 11, 15], 9) -> [0, 1]`
- `product_except_self_optimized([1, 2, 3, 4]) -> [24, 12, 8, 6]`
- `top_k_frequent_heap([1, 1, 1, 2, 2, 3], 2) -> [1, 2]`
"""

from collections import Counter
from heapq import nlargest


def two_sum_bruteforce(nums: list[int], target: int) -> list[int]:
    """
    Problem:
    Return indices of two numbers whose sum is equal to target.

    Approach:
    - Try every pair
    - Stop when the pair matches target

    Complexity:
    - Time: O(n^2)
    - Space: O(1)

    Debugging steps:
    1. Print i, j, nums[i], nums[j]
    2. Check the current sum
    3. Confirm that you return indices, not values
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_hashmap(nums: list[int], target: int) -> list[int]:
    """
    Better approach:
    - Store number -> index in a hash map
    - For each number, check whether target - number already exists

    Complexity:
    - Time: O(n)
    - Space: O(n)

    Debugging steps:
    1. Print current number and required complement
    2. Print hash map before insertion
    3. Verify duplicates are handled correctly
    """
    seen: dict[int, int] = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index
    return []


def product_except_self_prefix_suffix(nums: list[int]) -> list[int]:
    """
    Problem:
    Return an output array where output[i] is the product of all numbers
    except nums[i], without using division.

    Approach:
    - Build prefix products from left to right
    - Build suffix products from right to left
    - Multiply prefix and suffix at each index

    Complexity:
    - Time: O(n)
    - Space: O(n)

    Debugging steps:
    1. Print prefix array after each update
    2. Print suffix array after each update
    3. Verify first and last index handling carefully
    """
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    result = [1] * n

    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    for i in range(n):
        result[i] = prefix[i] * suffix[i]

    return result


def product_except_self_optimized(nums: list[int]) -> list[int]:
    """
    Optimized approach:
    - Store prefix products directly in result
    - Walk from right side with one suffix variable

    Complexity:
    - Time: O(n)
    - Space: O(1) extra output excluded

    Debugging steps:
    1. Print result after prefix pass
    2. Print suffix before and after each multiplication
    3. Check index order in reverse traversal
    """
    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


def top_k_frequent_sort(nums: list[int], k: int) -> list[int]:
    """
    Approach:
    - Count frequencies
    - Sort by frequency descending

    Complexity:
    - Time: O(n log n)
    - Space: O(n)

    Debugging steps:
    1. Print the frequency map
    2. Print sorted items
    3. Verify whether the result expects values only
    """
    frequency = Counter(nums)
    sorted_items = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    return [value for value, _count in sorted_items[:k]]


def top_k_frequent_heap(nums: list[int], k: int) -> list[int]:
    """
    Better approach:
    - Count frequencies
    - Use a heap helper through nlargest

    Complexity:
    - Time: O(n log k)
    - Space: O(n)

    Debugging steps:
    1. Print the counter
    2. Print the heap candidates
    3. Verify edge cases when k equals number of unique elements
    """
    frequency = Counter(nums)
    return nlargest(k, frequency.keys(), key=frequency.get)


if __name__ == "__main__":
    sample_nums = [2, 7, 11, 15]
    print("Two Sum (bruteforce):", two_sum_bruteforce(sample_nums, 9))
    print("Two Sum (hashmap):", two_sum_hashmap(sample_nums, 9))
    print("Product Except Self:", product_except_self_optimized([1, 2, 3, 4]))
    print("Top K Frequent:", top_k_frequent_heap([1, 1, 1, 2, 2, 3], 2))
