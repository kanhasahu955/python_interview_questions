"""
Tuple and Two-Pointer Problems
==============================

Problems that return pairs/triplets/quadruplets as tuples,
and problems solved with two-pointer or multi-pointer technique.

Quick input/output examples:
- `two_sum_ii([2,7,11,15], 9) -> [1,2]`
- `three_sum([-1,0,1,2,-1,-4]) -> [[-1,-1,2],[-1,0,1]]`
- `three_sum_closest([-1,2,1,-4], 1) -> 2`
- `four_sum([1,0,-1,0,-2,2], 0) -> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`
- `container_with_most_water([1,8,6,2,5,4,8,3,7]) -> 49`
- `trap([0,1,0,2,1,0,1,3,2,1,2,1]) -> 6`
- `three_sum_closest([-1,2,1,-4], 1) -> 2`
- `merge_intervals([[1,3],[2,6],[8,10],[15,18]]) -> [[1,6],[8,10],[15,18]]`
- `subarray_sum_equals_k([1,1,1], 2) -> 2`
"""

import heapq
from collections import defaultdict


# ---------------------------------------------------------------------------
# 1. Two Sum (hash map — baseline)
# ---------------------------------------------------------------------------

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Problem:
    Return indices of two numbers that sum to target.

    Input:  [2, 7, 11, 15], target=9
    Output: [0, 1]

    Approach:
    - Hash map: value -> index
    - For each number, check if complement exists

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print current number and its complement
    2. Print map state before insertion
    """
    seen: dict[int, int] = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index
    return []


# ---------------------------------------------------------------------------
# 2. Two Sum II – Sorted Array
# ---------------------------------------------------------------------------

def two_sum_ii(numbers: list[int], target: int) -> list[int]:
    """
    Problem:
    Array is sorted. Return 1-indexed pair whose sum equals target.

    Input:  [2, 7, 11, 15], target=9
    Output: [1, 2]

    Approach:
    - Two pointers from both ends
    - Move left up if sum too small, right down if too large

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print left, right, and current sum at each step
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        if current_sum < target:
            left += 1
        else:
            right -= 1
    return []


# ---------------------------------------------------------------------------
# 3. 3Sum
# ---------------------------------------------------------------------------

def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Problem:
    Find all unique triplets that sum to zero.

    Input:  [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]

    Approach:
    - Sort array
    - Fix one element, use two pointers for the remaining pair
    - Skip duplicates at every level

    Complexity: Time O(n²), Space O(1) extra

    Debugging steps:
    1. Print the fixed element and two pointer values each iteration
    2. Print when a duplicate is skipped
    """
    nums.sort()
    result: list[list[int]] = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # skip duplicate fixed element

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# ---------------------------------------------------------------------------
# 4. 3Sum Closest
# ---------------------------------------------------------------------------

def three_sum_closest(nums: list[int], target: int) -> int:
    """
    Problem:
    Find the triplet sum closest to target.

    Input:  [-1, 2, 1, -4], target=1
    Output: 2

    Approach:
    - Sort, fix one, two pointers for rest
    - Update closest sum if current is nearer to target

    Complexity: Time O(n²), Space O(1)

    Debugging steps:
    1. Print current triplet sum and distance from target
    2. Print when closest is updated
    """
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(current_sum - target) < abs(closest - target):
                closest = current_sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum

    return closest


# ---------------------------------------------------------------------------
# 5. 4Sum
# ---------------------------------------------------------------------------

def four_sum(nums: list[int], target: int) -> list[list[int]]:
    """
    Problem:
    Find all unique quadruplets that sum to target.

    Input:  [1, 0, -1, 0, -2, 2], target=0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

    Approach:
    - Sort, two outer loops fix two elements
    - Two pointers for remaining pair
    - Skip duplicates at every level

    Complexity: Time O(n³), Space O(1) extra

    Debugging steps:
    1. Print i, j fixed elements and pointer values each iteration
    2. Print when outer or inner duplicates are skipped
    """
    nums.sort()
    result: list[list[int]] = []
    n = len(nums)

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result


# ---------------------------------------------------------------------------
# 6. Pair with Target Sum (Two Pointer on sorted)
# ---------------------------------------------------------------------------

def pair_with_target_sum(arr: list[int], target: int) -> list[int]:
    """
    Problem:
    Given a sorted array, return indices of the pair that sums to target.

    Input:  [1, 2, 3, 4, 6], target=6
    Output: [1, 3]

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print left, right, and current sum each step
    """
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        if current_sum < target:
            left += 1
        else:
            right -= 1
    return []


# ---------------------------------------------------------------------------
# 7. Count Pairs with Given Sum
# ---------------------------------------------------------------------------

def count_pairs_with_sum(arr: list[int], target: int) -> int:
    """
    Problem:
    Count all pairs whose sum equals target.

    Input:  [1, 5, 7, -1, 5], target=6
    Output: 3

    Approach:
    - Frequency map
    - For each element check if (target - element) exists with remaining count

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print current element and its complement frequency
    """
    frequency: dict[int, int] = defaultdict(int)
    count = 0
    for number in arr:
        complement = target - number
        count += frequency[complement]
        frequency[number] += 1
    return count


# ---------------------------------------------------------------------------
# 8. Subarray with Given Sum (all positive)
# ---------------------------------------------------------------------------

def subarray_with_given_sum(arr: list[int], target: int) -> list[int]:
    """
    Problem:
    Find start and end index (0-indexed) of a contiguous subarray that sums to target.
    All elements are positive.

    Input:  [1, 4, 20, 3, 10, 5], target=33
    Output: [2, 4]   (20+3+10 = 33)

    Approach:
    - Sliding window: expand right, shrink left when sum exceeds target

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print window [left, right] and current sum at each step
    """
    left = 0
    current_sum = 0
    for right in range(len(arr)):
        current_sum += arr[right]
        while current_sum > target and left < right:
            current_sum -= arr[left]
            left += 1
        if current_sum == target:
            return [left, right]
    return []


# ---------------------------------------------------------------------------
# 9. Subarray Sum Equals K
# ---------------------------------------------------------------------------

def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    """
    Problem:
    Count the number of subarrays whose sum equals k (array may have negatives).

    Input:  [1, 1, 1], k=2
    Output: 2

    Input:  [1, 2, 3], k=3
    Output: 2

    Approach:
    - Prefix sum + hash map
    - If (prefix_sum - k) was seen before, subarrays ending here contribute

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print prefix sum and (prefix_sum - k) at each step
    2. Print map lookup result
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
# 10. Container with Most Water
# ---------------------------------------------------------------------------

def container_with_most_water(height: list[int]) -> int:
    """
    Problem:
    Find two lines forming a container that holds the most water.

    Input:  [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49

    Approach:
    - Two pointers from both ends
    - Always move the pointer with the shorter height inward

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print left, right, and current area each step
    2. Print which pointer moves and why
    """
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        current_area = width * min(height[left], height[right])
        max_area = max(max_area, current_area)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# ---------------------------------------------------------------------------
# 11. Trapping Rain Water
# ---------------------------------------------------------------------------

def trap_prefix_arrays(height: list[int]) -> int:
    """
    Problem:
    Calculate total water trapped between walls.

    Input:  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    Output: 6

    Approach:
    - Compute max height to the left and right of each position
    - Water at i = min(left_max[i], right_max[i]) - height[i]

    Complexity: Time O(n), Space O(n)
    """
    n = len(height)
    if n == 0:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    return sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))


def trap(height: list[int]) -> int:
    """
    Optimized approach using two pointers — O(1) extra space.

    Debugging steps:
    1. Print left, right, left_max, right_max, and water added each step
    2. Confirm the pointer with smaller max moves inward
    """
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water


# ---------------------------------------------------------------------------
# 12. Boats to Save People
# ---------------------------------------------------------------------------

def num_rescue_boats(people: list[int], limit: int) -> int:
    """
    Problem:
    Minimum boats where each carries at most 2 people with total weight ≤ limit.

    Input:  [1, 2, 2, 3], limit=3
    Output: 3

    Approach:
    - Sort, use two pointers
    - If lightest + heaviest ≤ limit, both go; else heaviest goes alone

    Complexity: Time O(n log n), Space O(1)

    Debugging steps:
    1. Print light, heavy, and whether they share a boat each iteration
    """
    people.sort()
    light, heavy = 0, len(people) - 1
    boats = 0

    while light <= heavy:
        if people[light] + people[heavy] <= limit:
            light += 1
        heavy -= 1
        boats += 1

    return boats


# ---------------------------------------------------------------------------
# 13. Valid Triangle Number
# ---------------------------------------------------------------------------

def triangle_number(nums: list[int]) -> int:
    """
    Problem:
    Count triplets that can form a valid triangle.

    Input:  [2, 2, 3, 4]
    Output: 3

    Approach:
    - Sort, fix the largest element (rightmost)
    - Use two pointers on the left portion
    - If nums[left] + nums[mid] > nums[right]: all pairs from left to mid work

    Complexity: Time O(n²), Space O(1)

    Debugging steps:
    1. Print left, mid, fixed right and the comparison result
    """
    nums.sort()
    count = 0

    for right in range(len(nums) - 1, 1, -1):
        left, mid = 0, right - 1
        while left < mid:
            if nums[left] + nums[mid] > nums[right]:
                count += mid - left
                mid -= 1
            else:
                left += 1

    return count


# ---------------------------------------------------------------------------
# 14. Minimum Size Subarray Sum
# ---------------------------------------------------------------------------

def min_subarray_len(target: int, nums: list[int]) -> int:
    """
    Problem:
    Find the minimal length subarray with sum >= target.

    Input:  target=7, nums=[2,3,1,2,4,3]
    Output: 2   (subarray [4,3])

    Approach:
    - Sliding window: grow right, shrink left while sum >= target

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print window bounds and current sum when shrinking
    """
    left = 0
    current_sum = 0
    min_len = float("inf")

    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if min_len == float("inf") else int(min_len)


# ---------------------------------------------------------------------------
# 15. Sort Colors (Dutch National Flag)
# ---------------------------------------------------------------------------

def sort_colors(nums: list[int]) -> None:
    """
    Problem:
    Sort array of 0s, 1s, and 2s in place in a single pass.

    Input:  [2, 0, 2, 1, 1, 0]
    Output: [0, 0, 1, 1, 2, 2]

    Approach:
    - Three pointers: low (boundary of 0s), mid (current), high (boundary of 2s)
    - Swap and advance depending on nums[mid]

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print low, mid, high, and array state at each swap
    """
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# ---------------------------------------------------------------------------
# 16. Move Zeros
# ---------------------------------------------------------------------------

def move_zeroes(nums: list[int]) -> None:
    """
    Problem:
    Move all zeros to the end, preserving relative order of non-zero elements.

    Input:  [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]

    Approach:
    - Write pointer tracks next position for non-zero
    - Swap non-zero with write position

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print write pointer and the element being moved
    """
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1


# ---------------------------------------------------------------------------
# 17. Remove Duplicates from Sorted Array (keep one)
# ---------------------------------------------------------------------------

def remove_duplicates(nums: list[int]) -> int:
    """
    Problem:
    Remove duplicates in place. Return count of unique elements.

    Input:  [1, 1, 2, 3, 3]
    Output: 3   (array prefix: [1, 2, 3])

    Approach:
    - Slow pointer k tracks next write position
    - Fast pointer scans; write when value changes

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print k and the new unique value being written
    """
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k


# ---------------------------------------------------------------------------
# 18. Remove Duplicates II (allow at most 2)
# ---------------------------------------------------------------------------

def remove_duplicates_ii(nums: list[int]) -> int:
    """
    Problem:
    Each element may appear at most twice. Remove excess in place.

    Input:  [1, 1, 1, 2, 2, 3]
    Output: 5   (array prefix: [1, 1, 2, 2, 3])

    Approach:
    - Write pointer k starts at 2
    - Allow element if nums[i] != nums[k-2]

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print k and nums[i] when writing or skipping
    """
    k = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1
    return k


# ---------------------------------------------------------------------------
# 19. Merge Intervals
# ---------------------------------------------------------------------------

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Problem:
    Merge all overlapping intervals.

    Input:  [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]

    Approach:
    - Sort by start time
    - Merge if current start <= previous end

    Complexity: Time O(n log n), Space O(n)

    Debugging steps:
    1. Print each interval and whether it merges with the previous
    """
    intervals.sort(key=lambda x: x[0])
    merged: list[list[int]] = []

    for interval in intervals:
        if merged and interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)

    return merged


# ---------------------------------------------------------------------------
# 20. Insert Interval
# ---------------------------------------------------------------------------

def insert_interval(
    intervals: list[list[int]], new_interval: list[int]
) -> list[list[int]]:
    """
    Problem:
    Insert new_interval into sorted non-overlapping intervals and merge.

    Input:  [[1,3],[6,9]], newInterval=[2,5]
    Output: [[1,5],[6,9]]

    Approach:
    - Add all intervals ending before new_interval starts
    - Merge all overlapping intervals into new_interval
    - Add remaining intervals

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print phase transitions (before, during, after new interval)
    """
    result: list[list[int]] = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    result.append(new_interval)

    while i < n:
        result.append(intervals[i])
        i += 1

    return result


# ---------------------------------------------------------------------------
# 21. Non-Overlapping Intervals
# ---------------------------------------------------------------------------

def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    """
    Problem:
    Return the minimum number of intervals to remove so none overlap.

    Input:  [[1,2],[2,3],[3,4],[1,3]]
    Output: 1

    Approach:
    - Sort by end time
    - Greedily keep intervals with earliest end
    - Count those that must be removed

    Complexity: Time O(n log n), Space O(1)

    Debugging steps:
    1. Print current interval and last kept end time
    """
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    remove_count = 0
    last_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < last_end:
            remove_count += 1
        else:
            last_end = intervals[i][1]

    return remove_count


# ---------------------------------------------------------------------------
# 22. Meeting Rooms (can attend all?)
# ---------------------------------------------------------------------------

def can_attend_meetings(intervals: list[list[int]]) -> bool:
    """
    Problem:
    Return True if a person can attend all meetings (no overlap).

    Input:  [[0,30],[5,10],[15,20]]
    Output: False

    Approach:
    - Sort by start time
    - Check if any interval starts before the previous one ends

    Complexity: Time O(n log n), Space O(1)

    Debugging steps:
    1. Print adjacent interval pair when overlap found
    """
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


# ---------------------------------------------------------------------------
# 23. Meeting Rooms II (minimum rooms needed)
# ---------------------------------------------------------------------------

def min_meeting_rooms(intervals: list[list[int]]) -> int:
    """
    Problem:
    Find minimum number of conference rooms required.

    Input:  [[0,30],[5,10],[15,20]]
    Output: 2

    Approach:
    - Min-heap tracking end times of ongoing meetings
    - For each meeting: if earliest-ending room is free, reuse it

    Complexity: Time O(n log n), Space O(n)

    Debugging steps:
    1. Print heap state after each push/pop
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    heap: list[int] = []

    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)
        else:
            heapq.heappush(heap, end)

    return len(heap)


# ---------------------------------------------------------------------------
# 24. K-diff Pairs in an Array
# ---------------------------------------------------------------------------

def find_k_diff_pairs(nums: list[int], k: int) -> int:
    """
    Problem:
    Count unique k-diff pairs (i, j) where |nums[i] - nums[j]| = k.

    Input:  [3, 1, 4, 1, 5], k=2
    Output: 2   (pairs: (1,3) and (3,5))

    Input:  [1, 2, 3, 4, 5], k=1
    Output: 4

    Approach:
    - Frequency map
    - For k > 0: check if num + k exists
    - For k = 0: check if frequency > 1

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print each num and whether its pair exists
    """
    if k < 0:
        return 0

    frequency: dict[int, int] = defaultdict(int)
    for num in nums:
        frequency[num] += 1

    count = 0
    for num in frequency:
        if k == 0:
            if frequency[num] > 1:
                count += 1
        else:
            if num + k in frequency:
                count += 1

    return count


# ---------------------------------------------------------------------------
# 25. Longest Mountain in Array
# ---------------------------------------------------------------------------

def longest_mountain(arr: list[int]) -> int:
    """
    Problem:
    Find the length of the longest mountain subarray.
    A mountain increases then decreases (at least one element on each side).

    Input:  [2, 1, 4, 7, 3, 2, 5]
    Output: 5   (mountain: [1,4,7,3,2])

    Input:  [2, 2, 2]
    Output: 0

    Approach:
    - Two pointers: left starts at 0
    - From left, find peak, then find valley
    - Track length of the mountain found

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print the peak index and the mountain boundaries
    """
    n = len(arr)
    left = 0
    result = 0

    while left + 2 < n:
        right = left + 1
        if arr[right - 1] < arr[right]:
            while right + 1 < n and arr[right] < arr[right + 1]:
                right += 1
            if right + 1 < n and arr[right] > arr[right + 1]:
                while right + 1 < n and arr[right] > arr[right + 1]:
                    right += 1
                result = max(result, right - left + 1)
            left = right
        else:
            left += 1

    return result


# ---------------------------------------------------------------------------
# 26. Two Sum Less Than K
# ---------------------------------------------------------------------------

def two_sum_less_than_k(nums: list[int], k: int) -> int:
    """
    Problem:
    Return the maximum sum of a pair where sum < k. Return -1 if no pair exists.

    Input:  [34, 23, 1, 24, 75, 33, 54, 8], k=60
    Output: 58   (pair 34+24=58)

    Input:  [10, 20, 30], k=15
    Output: -1

    Approach:
    - Sort, two pointers from both ends
    - Track max valid sum

    Complexity: Time O(n log n), Space O(1)

    Debugging steps:
    1. Print left, right, sum, and current max at each step
    """
    nums.sort()
    left, right = 0, len(nums) - 1
    best = -1

    while left < right:
        current = nums[left] + nums[right]
        if current < k:
            best = max(best, current)
            left += 1
        else:
            right -= 1

    return best


# ---------------------------------------------------------------------------
# 27. Count Subarrays with Product Less Than K
# ---------------------------------------------------------------------------

def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
    """
    Problem:
    Count contiguous subarrays whose product is strictly less than k.

    Input:  [10, 5, 2, 6], k=100
    Output: 8

    Explanation:
    Subarrays: [10],[5],[2],[6],[10,5],[5,2],[2,6],[5,2,6] — all have product < 100

    Approach:
    - Sliding window with running product
    - Shrink from left when product >= k
    - Count = right - left + 1 for every valid window end

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print left, right, current product, and count added each step
    """
    if k <= 1:
        return 0

    product = 1
    left = 0
    count = 0

    for right in range(len(nums)):
        product *= nums[right]
        while product >= k and left <= right:
            product //= nums[left]
            left += 1
        count += right - left + 1

    return count


# ---------------------------------------------------------------------------
# 28. Max Consecutive Ones III
# ---------------------------------------------------------------------------

def longest_ones(nums: list[int], k: int) -> int:
    """
    Problem:
    Find the maximum number of consecutive 1s after flipping at most k zeros.

    Input:  [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2
    Output: 6

    Input:  [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3
    Output: 10

    Approach:
    - Sliding window: track number of zeros in the window
    - Shrink from left when zeros exceed k

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print window size and zero count at each step
    """
    left = 0
    zero_count = 0
    best = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        best = max(best, right - left + 1)

    return best


# ---------------------------------------------------------------------------
# 29. Longest Subarray of 1s After Deleting One Element
# ---------------------------------------------------------------------------

def longest_subarray(nums: list[int]) -> int:
    """
    Problem:
    Delete exactly one element. Return length of the longest subarray of 1s.

    Input:  [1, 1, 0, 1]
    Output: 3

    Input:  [0, 1, 1, 1, 0, 1, 1, 0, 1]
    Output: 5

    Approach:
    - Sliding window: track zeros in window
    - At most 1 zero allowed (for the deleted element)
    - Answer is window_size - 1 (subtract the deleted element)

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print window and zero count when shrinking
    """
    left = 0
    zero_count = 0
    best = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        best = max(best, right - left)  # subtract 1 for the deleted element

    return best


# ---------------------------------------------------------------------------
# 30. Fruit Into Baskets (Longest Subarray with at Most 2 Distinct Values)
# ---------------------------------------------------------------------------

def total_fruit(fruits: list[int]) -> int:
    """
    Problem:
    You have two baskets, each can hold only one type of fruit.
    Find the maximum number of fruits you can pick in a contiguous sequence.

    Input:  [1, 2, 1]
    Output: 3

    Input:  [0, 1, 2, 2]
    Output: 3

    Input:  [1, 2, 3, 2, 2]
    Output: 4

    Approach:
    - Sliding window with a frequency map
    - Shrink from left when more than 2 distinct fruits exist

    Complexity: Time O(n), Space O(1) — map holds at most 3 entries

    Debugging steps:
    1. Print basket map after each add/remove
    2. Print window size when answer updates
    """
    basket: dict[int, int] = defaultdict(int)
    left = 0
    best = 0

    for right in range(len(fruits)):
        basket[fruits[right]] += 1
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1
        best = max(best, right - left + 1)

    return best


# ---------------------------------------------------------------------------
# 31. Minimum Window Subsequence
# ---------------------------------------------------------------------------

def min_window_subsequence(source: str, target: str) -> str:
    """
    Problem:
    Find the shortest substring in source such that target appears as a subsequence.

    Input:  source="abcdebdde", target="bde"
    Output: "bcde"

    Input:  source="jmeqksfrsdcmsiwvaovztaqenprpvnbstl", target="u"
    Output: ""

    Approach:
    - Two pointers: walk source forward matching target left to right
    - When full match found, walk backward to tighten the window
    - Track minimum window seen

    Complexity: Time O(n * m), Space O(1)

    Debugging steps:
    1. Print source pointer and target pointer during forward scan
    2. Print window when a match is tightened
    """
    best = ""
    i = 0

    while i < len(source):
        # Forward: match all characters of target in order
        t = 0
        while i < len(source) and t < len(target):
            if source[i] == target[t]:
                t += 1
            i += 1

        if t < len(target):
            break  # target not matched

        # Backward: shrink window from the right end
        j = i - 1
        t = len(target) - 1
        while t >= 0:
            if source[j] == target[t]:
                t -= 1
            j -= 1

        window = source[j + 1: i]
        if not best or len(window) < len(best):
            best = window
        i = j + 2  # restart from just after window start

    return best


# ---------------------------------------------------------------------------
# 32. Maximum Points You Can Obtain from Cards
# ---------------------------------------------------------------------------

def max_score(card_points: list[int], k: int) -> int:
    """
    Problem:
    Pick exactly k cards from either end of the row to maximize total points.

    Input:  [1, 2, 3, 4, 5, 6, 1], k=3
    Output: 12   (pick 1,6,5 from right)

    Input:  [2, 2, 2], k=2
    Output: 4

    Approach:
    - Total = sum of entire array - minimum subarray of length (n - k)
    - Sliding window of fixed size (n - k) to find the minimum

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print window sum as it slides
    2. Print min_window_sum when updated
    """
    n = len(card_points)
    window_size = n - k
    window_sum = sum(card_points[:window_size])
    min_sum = window_sum
    total = sum(card_points)

    for i in range(window_size, n):
        window_sum += card_points[i] - card_points[i - window_size]
        min_sum = min(min_sum, window_sum)

    return total - min_sum


# ---------------------------------------------------------------------------
# 33. Longest Continuous Subarray with Absolute Diff ≤ Limit
# ---------------------------------------------------------------------------

from collections import deque


def longest_subarray_with_limit(nums: list[int], limit: int) -> int:
    """
    Problem:
    Return the size of the longest subarray where |max - min| <= limit.

    Input:  [8, 2, 4, 7], limit=4
    Output: 2

    Input:  [10, 1, 2, 4, 7, 2], limit=5
    Output: 4

    Approach:
    - Two monotonic deques: one for max, one for min
    - Shrink left when max - min > limit

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print max_deque and min_deque after each update
    2. Print window when shrinking
    """
    max_dq: deque[int] = deque()  # decreasing — front is max
    min_dq: deque[int] = deque()  # increasing — front is min
    left = 0
    best = 0

    for right in range(len(nums)):
        while max_dq and nums[max_dq[-1]] <= nums[right]:
            max_dq.pop()
        max_dq.append(right)

        while min_dq and nums[min_dq[-1]] >= nums[right]:
            min_dq.pop()
        min_dq.append(right)

        while nums[max_dq[0]] - nums[min_dq[0]] > limit:
            left += 1
            if max_dq[0] < left:
                max_dq.popleft()
            if min_dq[0] < left:
                min_dq.popleft()

        best = max(best, right - left + 1)

    return best


# ---------------------------------------------------------------------------
# 34. Number of Subarrays with Bounded Maximum
# ---------------------------------------------------------------------------

def num_subarray_bounded_max(nums: list[int], left_bound: int, right_bound: int) -> int:
    """
    Problem:
    Count subarrays where the maximum element is between left_bound and right_bound.

    Input:  [2, 1, 4, 3], L=2, R=3
    Output: 3

    Approach:
    - Count subarrays with max <= R  minus  subarrays with max <= L-1
    - Helper: count subarrays with all elements <= bound

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print count at each step in helper
    """
    def count_at_most(bound: int) -> int:
        count = 0
        current = 0
        for num in nums:
            current = current + 1 if num <= bound else 0
            count += current
        return count

    return count_at_most(right_bound) - count_at_most(left_bound - 1)


# ---------------------------------------------------------------------------
# 35. 3Sum with Multiplicity
# ---------------------------------------------------------------------------

def three_sum_multi(arr: list[int], target: int) -> int:
    """
    Problem:
    Count tuples (i, j, k) where i < j < k and arr[i]+arr[j]+arr[k] == target.
    Return the answer modulo 10^9 + 7.

    Input:  [1, 1, 2, 2, 3, 3, 4, 4, 5, 5], target=8
    Output: 20

    Approach:
    - Count frequencies of each value
    - Enumerate all combinations of (a, b, c) with a <= b <= c
    - Apply combinatorics based on whether values are equal

    Complexity: Time O(target²), Space O(target)

    Debugging steps:
    1. Print each (a, b, c) combination and its count
    """
    MOD = 10 ** 9 + 7
    count: dict[int, int] = defaultdict(int)
    for num in arr:
        count[num] += 1

    result = 0
    keys = sorted(count)

    for i, a in enumerate(keys):
        for j, b in enumerate(keys):
            if b < a:
                continue
            c = target - a - b
            if c < b:
                break
            if c not in count:
                continue

            if a == b == c:
                n = count[a]
                result += n * (n - 1) * (n - 2) // 6
            elif a == b:
                n = count[a]
                result += n * (n - 1) // 2 * count[c]
            elif b == c:
                n = count[b]
                result += count[a] * n * (n - 1) // 2
            else:
                result += count[a] * count[b] * count[c]

    return result % MOD


# ---------------------------------------------------------------------------
# 36. Squares of a Sorted Array
# ---------------------------------------------------------------------------

def sorted_squares(nums: list[int]) -> list[int]:
    """
    Problem:
    Given a sorted array, return sorted squares of each element.

    Input:  [-4, -1, 0, 3, 10]
    Output: [0, 1, 9, 16, 100]

    Input:  [-7, -3, 2, 3, 11]
    Output: [4, 9, 9, 49, 121]

    Approach:
    - Two pointers from both ends
    - Largest square is always at one end
    - Fill result from right to left

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print left, right, and chosen square at each step
    """
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1

    while left <= right:
        sq_left = nums[left] ** 2
        sq_right = nums[right] ** 2
        if sq_left > sq_right:
            result[pos] = sq_left
            left += 1
        else:
            result[pos] = sq_right
            right -= 1
        pos -= 1

    return result


# ---------------------------------------------------------------------------
# 37. Minimum Difference Between Highest and Lowest of K Scores
# ---------------------------------------------------------------------------

def minimum_difference(nums: list[int], k: int) -> int:
    """
    Problem:
    Choose k elements from nums. Return the minimum difference between
    the largest and smallest of those k elements.

    Input:  [90, 2, 85, 3], k=3
    Output: 83   (pick 90,85,3 → 90-3=87; or pick 90,85,2 → 88; best: 2,3,85 → 83)

    Input:  [9, 4, 1, 7], k=2
    Output: 2

    Approach:
    - Sort, then use a sliding window of size k
    - Answer is min of (nums[i+k-1] - nums[i]) for all valid i

    Complexity: Time O(n log n), Space O(1)

    Debugging steps:
    1. Print window endpoints and difference at each step
    """
    nums.sort()
    best = float("inf")
    for i in range(len(nums) - k + 1):
        best = min(best, nums[i + k - 1] - nums[i])
    return int(best)


# ---------------------------------------------------------------------------
# 38. Find All Anagrams in a String (Tuple of Start Indices)
# ---------------------------------------------------------------------------

def find_anagrams(s: str, p: str) -> list[int]:
    """
    Problem:
    Return all start indices in s where an anagram of p begins.

    Input:  s="cbaebabacd", p="abc"
    Output: [0, 6]

    Input:  s="abab", p="ab"
    Output: [0, 1, 2]

    Approach:
    - Fixed-size sliding window of length len(p)
    - Compare character frequency maps

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print window frequency map and target map after each slide
    """
    from collections import Counter
    if len(p) > len(s):
        return []

    p_count = Counter(p)
    window = Counter(s[:len(p)])
    result = []

    if window == p_count:
        result.append(0)

    for i in range(len(p), len(s)):
        window[s[i]] += 1
        left_char = s[i - len(p)]
        window[left_char] -= 1
        if window[left_char] == 0:
            del window[left_char]
        if window == p_count:
            result.append(i - len(p) + 1)

    return result


# ---------------------------------------------------------------------------
# 39. Partition Array Such That Maximum Difference ≤ K
# ---------------------------------------------------------------------------

def partition_array(nums: list[int], k: int) -> int:
    """
    Problem:
    Partition nums into the minimum number of subsequences such that the
    difference between max and min of each subsequence is at most k.

    Input:  [3, 6, 1, 2, 5], k=2
    Output: 2   (subsequences: [1,2,3] and [5,6])

    Input:  [1, 2, 3], k=1
    Output: 2   (subsequences: [1,2] and [3])

    Approach:
    - Sort the array
    - Greedily extend the current subsequence while max-min <= k
    - Start a new group when difference exceeds k

    Complexity: Time O(n log n), Space O(1)

    Debugging steps:
    1. Print group start and current element when a new group begins
    """
    nums.sort()
    groups = 1
    group_start = nums[0]

    for num in nums[1:]:
        if num - group_start > k:
            groups += 1
            group_start = num

    return groups


# ---------------------------------------------------------------------------
# 40. Longest Turbulent Subarray
# ---------------------------------------------------------------------------

def max_turbulence_size(arr: list[int]) -> int:
    """
    Problem:
    Return the length of the longest turbulent subarray.
    Turbulent: arr[i] > arr[i+1] < arr[i+2] or arr[i] < arr[i+1] > arr[i+2]

    Input:  [9, 4, 2, 10, 7, 8, 8, 1, 9]
    Output: 5   (subarray [4, 2, 10, 7, 8])

    Input:  [4, 8, 12, 16]
    Output: 2

    Approach:
    - Two pointers: left starts at 0
    - Extend right as long as the alternating sign condition holds
    - Reset when consecutive elements are equal or sign doesn't alternate

    Complexity: Time O(n), Space O(1)

    Debugging steps:
    1. Print sign at each step (+1 or -1)
    2. Print window reset conditions
    """
    n = len(arr)
    if n < 2:
        return n

    best = 1
    left = 0

    for right in range(1, n):
        cmp = (arr[right] > arr[right - 1]) - (arr[right] < arr[right - 1])
        if cmp == 0:
            left = right
        elif right > 1:
            prev_cmp = (arr[right - 1] > arr[right - 2]) - (arr[right - 1] < arr[right - 2])
            if cmp == prev_cmp:
                left = right - 1
        best = max(best, right - left + 1)

    return best


# ---------------------------------------------------------------------------
# 39. Maximum Erasure Value (Longest Subarray with Unique Elements Sum)
# ---------------------------------------------------------------------------

def maximum_unique_subarray(nums: list[int]) -> int:
    """
    Problem:
    Return the maximum sum of a subarray that contains only unique elements.

    Input:  [4, 2, 4, 5, 6]
    Output: 17   (subarray [2, 4, 5, 6])

    Input:  [5, 2, 1, 2, 5, 2, 1, 2, 5]
    Output: 8    (subarray [5, 2, 1] or [1, 2, 5])

    Approach:
    - Sliding window with a Set
    - Shrink from left when a duplicate enters
    - Track running sum

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print set contents and running sum at each step
    """
    seen: set[int] = set()
    left = 0
    current_sum = 0
    best = 0

    for right in range(len(nums)):
        while nums[right] in seen:
            seen.discard(nums[left])
            current_sum -= nums[left]
            left += 1
        seen.add(nums[right])
        current_sum += nums[right]
        best = max(best, current_sum)

    return best


# ---------------------------------------------------------------------------
# 40. Maximum Sum of Two Non-Overlapping Subarrays
# ---------------------------------------------------------------------------

def max_sum_two_no_overlap(nums: list[int], first_len: int, second_len: int) -> int:
    """
    Problem:
    Find maximum sum of two non-overlapping subarrays of lengths first_len and second_len.

    Input:  [0, 6, 5, 2, 2, 5, 1, 9, 4], first_len=1, second_len=2
    Output: 20   (subarrays [9] and [6, 5])

    Input:  [3, 8, 1, 3, 2, 1, 8, 9, 0], first_len=3, second_len=2
    Output: 29

    Approach:
    - Build prefix sums
    - Two passes: in each pass fix one window and find best of the other

    Complexity: Time O(n), Space O(n)

    Debugging steps:
    1. Print prefix sums
    2. Print max_first / max_second as they update
    """
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    def window_sum(left: int, right: int) -> int:
        return prefix[right] - prefix[left]

    best = 0

    # Case 1: first_len window comes before second_len window
    max_first = 0
    for i in range(first_len + second_len, n + 1):
        max_first = max(max_first, window_sum(i - first_len - second_len, i - second_len))
        best = max(best, max_first + window_sum(i - second_len, i))

    # Case 2: second_len window comes before first_len window
    max_second = 0
    for i in range(first_len + second_len, n + 1):
        max_second = max(max_second, window_sum(i - first_len - second_len, i - first_len))
        best = max(best, max_second + window_sum(i - first_len, i))

    return best
