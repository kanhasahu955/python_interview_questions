"""
Dynamic Programming
===================

Common company-style questions:
1. Climbing Stairs
2. Coin Change
3. Longest Increasing Subsequence

This topic tests:
- pattern recognition
- reuse of subproblem results
- top-down versus bottom-up thinking

Quick input/output examples:
- `climbing_stairs_dp(5) -> 8`
- `coin_change([1, 2, 5], 11) -> 3`
- `longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) -> 4`
"""


def climbing_stairs_recursive(n: int) -> int:
    """
    Simple idea:
    - From step n, you can come from n - 1 or n - 2

    Complexity:
    - Time: O(2^n)
    - Space: O(n)

    Debugging steps:
    1. Print n at each recursive call
    2. Watch repeated subproblems
    """
    if n <= 2:
        return n
    return climbing_stairs_recursive(n - 1) + climbing_stairs_recursive(n - 2)


def climbing_stairs_dp(n: int) -> int:
    """
    Better approach:
    - Build answers from 1 to n

    Complexity:
    - Time: O(n)
    - Space: O(1)
    """
    if n <= 2:
        return n

    first = 1
    second = 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second


def coin_change(coins: list[int], amount: int) -> int:
    """
    Problem:
    Find the minimum number of coins needed to make the amount.

    Approach:
    - dp[current] stores minimum coins needed for current amount
    - Try each coin for each amount

    Complexity:
    - Time: O(amount * len(coins))
    - Space: O(amount)

    Debugging steps:
    1. Print dp array after each outer loop amount
    2. Check impossible states carefully
    """
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for current in range(1, amount + 1):
        for coin in coins:
            if coin <= current:
                dp[current] = min(dp[current], 1 + dp[current - coin])

    return dp[amount] if dp[amount] != amount + 1 else -1


def lis_quadratic(nums: list[int]) -> int:
    """
    Problem:
    Find the length of the longest increasing subsequence.

    Approach:
    - dp[i] = best LIS ending at i
    - Compare nums[i] with every previous nums[j]

    Complexity:
    - Time: O(n^2)
    - Space: O(n)

    Debugging steps:
    1. Print dp after each i
    2. Print candidate transitions j -> i
    """
    if not nums:
        return 0

    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def lis_binary_search(nums: list[int]) -> int:
    """
    Optimized approach:
    - Maintain tails array
    - tails[i] is the smallest possible tail for subsequence length i + 1

    Complexity:
    - Time: O(n log n)
    - Space: O(n)

    Debugging steps:
    1. Print tails after each number
    2. Verify replacement index carefully
    """
    tails: list[int] = []

    for value in nums:
        left = 0
        right = len(tails)

        while left < right:
            middle = (left + right) // 2
            if tails[middle] < value:
                left = middle + 1
            else:
                right = middle

        if left == len(tails):
            tails.append(value)
        else:
            tails[left] = value

    return len(tails)


if __name__ == "__main__":
    print("Climbing Stairs:", climbing_stairs_dp(5))
    print("Coin Change:", coin_change([1, 2, 5], 11))
    print("LIS:", lis_binary_search([10, 9, 2, 5, 3, 7, 101, 18]))
