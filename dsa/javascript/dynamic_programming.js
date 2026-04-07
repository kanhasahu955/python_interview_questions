/*
Dynamic Programming
===================

Common company-style questions:
1. Climbing Stairs
2. Coin Change
3. Longest Increasing Subsequence

Quick input/output examples:
- `climbingStairsDp(5) -> 8`
- `coinChange([1, 2, 5], 11) -> 3`
- `longestIncreasingSubsequence([10, 9, 2, 5, 3, 7, 101, 18]) -> 4`
*/

function climbingStairsRecursive(n) {
  if (n <= 2) {
    return n;
  }
  return climbingStairsRecursive(n - 1) + climbingStairsRecursive(n - 2);
}

function climbingStairsDp(n) {
  if (n <= 2) {
    return n;
  }

  let first = 1;
  let second = 2;

  for (let step = 3; step <= n; step += 1) {
    const current = first + second;
    first = second;
    second = current;
  }

  return second;
}

function coinChange(coins, amount) {
  const dp = new Array(amount + 1).fill(amount + 1);
  dp[0] = 0;

  for (let current = 1; current <= amount; current += 1) {
    for (const coin of coins) {
      if (coin <= current) {
        dp[current] = Math.min(dp[current], 1 + dp[current - coin]);
      }
    }
  }

  return dp[amount] === amount + 1 ? -1 : dp[amount];
}

function lisQuadratic(nums) {
  if (!nums.length) {
    return 0;
  }

  const dp = new Array(nums.length).fill(1);

  for (let i = 0; i < nums.length; i += 1) {
    for (let j = 0; j < i; j += 1) {
      if (nums[j] < nums[i]) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
  }

  return Math.max(...dp);
}

function lisBinarySearch(nums) {
  /*
  Debugging steps:
  1. Print tails after every number
  2. Check binary search boundaries carefully
  */
  const tails = [];

  for (const value of nums) {
    let left = 0;
    let right = tails.length;

    while (left < right) {
      const middle = Math.floor((left + right) / 2);
      if (tails[middle] < value) {
        left = middle + 1;
      } else {
        right = middle;
      }
    }

    if (left === tails.length) {
      tails.push(value);
    } else {
      tails[left] = value;
    }
  }

  return tails.length;
}

console.log("Climbing Stairs:", climbingStairsDp(5));
console.log("Coin Change:", coinChange([1, 2, 5], 11));
console.log("LIS:", lisBinarySearch([10, 9, 2, 5, 3, 7, 101, 18]));
