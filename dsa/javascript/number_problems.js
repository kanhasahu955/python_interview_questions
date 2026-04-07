/*
Number Problems
===============

Common number-related DSA interview questions:
1. Palindrome Number
2. Reverse Integer
3. Plus One
4. Happy Number
5. Power of Two
6. Sqrt(x)
7. Pow(x, n)
8. GCD and LCM
9. Prime Check
10. Count Primes
11. Prime Factorization
12. Missing Number
13. Single Number
14. Factorial Trailing Zeroes
15. Armstrong Number
16. Add Digits
17. Number of 1 Bits
18. Hamming Distance
19. Power of Three
20. Perfect Number
21. Ugly Number
22. Divide Two Integers
23. Fibonacci Number
24. Roman to Integer
25. Integer to Roman
26. Counting Bits
27. Reverse Bits
28. Sum of Two Integers
29. Power of Four
30. Number of Steps to Reduce to Zero
31. Excel Sheet Column Number
32. Fraction to Recurring Decimal

Quick input/output examples:
- `palindromeNumberMath(121) -> true`
- `plusOne([1, 2, 9]) -> [1, 3, 0]`
- `countPrimes(10) -> 4`
- `romanToInteger("MCMXCIV") -> 1994`
- `fractionToDecimal(1, 3) -> "0.(3)"`
*/

function palindromeNumberString(x) {
  const text = String(x);
  return text === [...text].reverse().join("");
}

function palindromeNumberMath(x) {
  if (x < 0) {
    return false;
  }

  const original = x;
  let reversed = 0;

  while (x > 0) {
    const digit = x % 10;
    reversed = reversed * 10 + digit;
    x = Math.floor(x / 10);
  }

  return original === reversed;
}

function reverseInteger(x) {
  const sign = x < 0 ? -1 : 1;
  x = Math.abs(x);
  let reversed = 0;

  while (x > 0) {
    const digit = x % 10;
    reversed = reversed * 10 + digit;
    x = Math.floor(x / 10);
  }

  return sign * reversed;
}

function plusOne(digits) {
  const result = [...digits];

  for (let i = result.length - 1; i >= 0; i -= 1) {
    if (result[i] < 9) {
      result[i] += 1;
      return result;
    }
    result[i] = 0;
  }

  return [1, ...result];
}

function happyNumber(n) {
  function nextNumber(value) {
    let total = 0;
    while (value > 0) {
      const digit = value % 10;
      total += digit * digit;
      value = Math.floor(value / 10);
    }
    return total;
  }

  const seen = new Set();
  while (n !== 1 && !seen.has(n)) {
    seen.add(n);
    n = nextNumber(n);
  }

  return n === 1;
}

function powerOfTwoBitwise(n) {
  return n > 0 && (n & (n - 1)) === 0;
}

function integerSqrt(x) {
  if (x < 2) {
    return x;
  }

  let left = 1;
  let right = Math.floor(x / 2);
  let answer = 0;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const square = mid * mid;

    if (square === x) {
      return mid;
    }

    if (square < x) {
      answer = mid;
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return answer;
}

function powerFast(base, exponent) {
  if (exponent === 0) {
    return 1;
  }

  if (exponent < 0) {
    return 1 / powerFast(base, -exponent);
  }

  const half = powerFast(base, Math.floor(exponent / 2));
  if (exponent % 2 === 0) {
    return half * half;
  }
  return half * half * base;
}

function gcdEuclidean(a, b) {
  a = Math.abs(a);
  b = Math.abs(b);
  while (b !== 0) {
    const temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

function lcmUsingGcd(a, b) {
  return Math.abs(a * b) / gcdEuclidean(a, b);
}

function isPrime(n) {
  if (n < 2) {
    return false;
  }
  if (n === 2) {
    return true;
  }
  if (n % 2 === 0) {
    return false;
  }

  for (let divisor = 3; divisor * divisor <= n; divisor += 2) {
    if (n % divisor === 0) {
      return false;
    }
  }

  return true;
}

function countPrimes(n) {
  if (n <= 2) {
    return 0;
  }

  const primeList = new Array(n).fill(true);
  primeList[0] = false;
  primeList[1] = false;

  for (let current = 2; current * current < n; current += 1) {
    if (primeList[current]) {
      for (let multiple = current * current; multiple < n; multiple += current) {
        primeList[multiple] = false;
      }
    }
  }

  return primeList.filter(Boolean).length;
}

function primeFactors(n) {
  const factors = [];
  let divisor = 2;

  while (divisor * divisor <= n) {
    while (n % divisor === 0) {
      factors.push(divisor);
      n = Math.floor(n / divisor);
    }
    divisor += 1;
  }

  if (n > 1) {
    factors.push(n);
  }

  return factors;
}

function missingNumberSum(nums) {
  const n = nums.length;
  const expected = (n * (n + 1)) / 2;
  const actual = nums.reduce((sum, value) => sum + value, 0);
  return expected - actual;
}

function singleNumberXor(nums) {
  let result = 0;
  for (const value of nums) {
    result ^= value;
  }
  return result;
}

function factorialTrailingZeroes(n) {
  let count = 0;
  while (n > 0) {
    n = Math.floor(n / 5);
    count += n;
  }
  return count;
}

function armstrongNumber(n) {
  const digits = String(n).split("");
  const power = digits.length;
  const total = digits.reduce((sum, digit) => sum + Number(digit) ** power, 0);
  return total === n;
}

function addDigitsLoop(num) {
  while (num >= 10) {
    let digitSum = 0;
    while (num > 0) {
      digitSum += num % 10;
      num = Math.floor(num / 10);
    }
    num = digitSum;
  }
  return num;
}

function addDigitsMath(num) {
  if (num === 0) {
    return 0;
  }
  return 1 + ((num - 1) % 9);
}

function numberOfOneBits(n) {
  let count = 0;
  while (n > 0) {
    count += n & 1;
    n >>= 1;
  }
  return count;
}

function hammingDistance(x, y) {
  return numberOfOneBits(x ^ y);
}

function powerOfThreeDivision(n) {
  if (n <= 0) {
    return false;
  }
  while (n % 3 === 0) {
    n = Math.floor(n / 3);
  }
  return n === 1;
}

function perfectNumber(num) {
  if (num <= 1) {
    return false;
  }

  let divisorSum = 1;
  for (let divisor = 2; divisor * divisor <= num; divisor += 1) {
    if (num % divisor === 0) {
      divisorSum += divisor;
      if (divisor !== Math.floor(num / divisor)) {
        divisorSum += Math.floor(num / divisor);
      }
    }
  }

  return divisorSum === num;
}

function uglyNumber(n) {
  if (n <= 0) {
    return false;
  }

  for (const factor of [2, 3, 5]) {
    while (n % factor === 0) {
      n = Math.floor(n / factor);
    }
  }
  return n === 1;
}

function divideTwoIntegers(dividend, divisor) {
  if (divisor === 0) {
    throw new Error("divisor cannot be zero");
  }

  const sign = (dividend < 0) ^ (divisor < 0) ? -1 : 1;
  dividend = Math.abs(dividend);
  divisor = Math.abs(divisor);
  let quotient = 0;

  while (dividend >= divisor) {
    let currentDivisor = divisor;
    let multiple = 1;
    while (dividend >= (currentDivisor << 1)) {
      currentDivisor <<= 1;
      multiple <<= 1;
    }
    dividend -= currentDivisor;
    quotient += multiple;
  }

  return sign * quotient;
}

function fibonacciIterative(n) {
  if (n <= 1) {
    return n;
  }

  let first = 0;
  let second = 1;
  for (let index = 2; index <= n; index += 1) {
    const current = first + second;
    first = second;
    second = current;
  }
  return second;
}

function romanToInteger(text) {
  const values = new Map([
    ["I", 1],
    ["V", 5],
    ["X", 10],
    ["L", 50],
    ["C", 100],
    ["D", 500],
    ["M", 1000],
  ]);
  let total = 0;

  for (let index = 0; index < text.length; index += 1) {
    const value = values.get(text[index]);
    const nextValue = values.get(text[index + 1]) || 0;
    if (value < nextValue) {
      total -= value;
    } else {
      total += value;
    }
  }

  return total;
}

function integerToRoman(num) {
  const mapping = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"],
  ];
  let result = "";

  for (const [value, symbol] of mapping) {
    while (num >= value) {
      result += symbol;
      num -= value;
    }
  }

  return result;
}

function countingBits(n) {
  const result = new Array(n + 1).fill(0);
  for (let value = 1; value <= n; value += 1) {
    result[value] = result[value >> 1] + (value & 1);
  }
  return result;
}

function reverseBits(n, bitSize = 32) {
  let result = 0;
  for (let index = 0; index < bitSize; index += 1) {
    result = (result << 1) | (n & 1);
    n >>= 1;
  }
  return result >>> 0;
}

function sumOfTwoIntegers(a, b) {
  while (b !== 0) {
    const carry = a & b;
    a = a ^ b;
    b = carry << 1;
  }
  return a;
}

function powerOfFour(n) {
  return n > 0 && (n & (n - 1)) === 0 && (n - 1) % 3 === 0;
}

function numberOfStepsToZero(num) {
  let steps = 0;
  while (num > 0) {
    if (num % 2 === 0) {
      num = Math.floor(num / 2);
    } else {
      num -= 1;
    }
    steps += 1;
  }
  return steps;
}

function excelSheetColumnNumber(columnTitle) {
  let result = 0;
  for (const char of columnTitle) {
    result = result * 26 + (char.charCodeAt(0) - "A".charCodeAt(0) + 1);
  }
  return result;
}

function fractionToRecurringDecimal(numerator, denominator) {
  if (denominator === 0) {
    throw new Error("denominator cannot be zero");
  }
  if (numerator === 0) {
    return "0";
  }

  const sign = (numerator < 0) ^ (denominator < 0) ? "-" : "";
  numerator = Math.abs(numerator);
  denominator = Math.abs(denominator);

  const integerPart = Math.floor(numerator / denominator);
  let remainder = numerator % denominator;
  if (remainder === 0) {
    return sign + String(integerPart);
  }

  const result = [sign + String(integerPart), "."];
  const seen = new Map();

  while (remainder !== 0) {
    if (seen.has(remainder)) {
      result.splice(seen.get(remainder), 0, "(");
      result.push(")");
      break;
    }

    seen.set(remainder, result.length);
    remainder *= 10;
    result.push(String(Math.floor(remainder / denominator)));
    remainder %= denominator;
  }

  return result.join("");
}

console.log("Palindrome:", palindromeNumberMath(121));
console.log("Reverse Integer:", reverseInteger(-456));
console.log("Plus One:", plusOne([1, 2, 9]));
console.log("Happy Number:", happyNumber(19));
console.log("Power of Two:", powerOfTwoBitwise(16));
console.log("Integer Sqrt:", integerSqrt(17));
console.log("Power Fast:", powerFast(2, 10));
console.log("GCD:", gcdEuclidean(48, 18));
console.log("LCM:", lcmUsingGcd(12, 18));
console.log("Is Prime:", isPrime(29));
console.log("Count Primes:", countPrimes(20));
console.log("Prime Factors:", primeFactors(84));
console.log("Missing Number:", missingNumberSum([3, 0, 1]));
console.log("Single Number:", singleNumberXor([4, 1, 2, 1, 2]));
console.log("Trailing Zeroes:", factorialTrailingZeroes(25));
console.log("Armstrong Number:", armstrongNumber(153));
console.log("Add Digits:", addDigitsMath(38));
console.log("Number of 1 Bits:", numberOfOneBits(11));
console.log("Hamming Distance:", hammingDistance(1, 4));
console.log("Power of Three:", powerOfThreeDivision(27));
console.log("Perfect Number:", perfectNumber(28));
console.log("Ugly Number:", uglyNumber(30));
console.log("Divide Two Integers:", divideTwoIntegers(43, 8));
console.log("Fibonacci:", fibonacciIterative(10));
console.log("Roman to Integer:", romanToInteger("MCMXCIV"));
console.log("Integer to Roman:", integerToRoman(1994));
console.log("Counting Bits:", countingBits(5));
console.log("Reverse Bits:", reverseBits(13, 4));
console.log("Sum of Two Integers:", sumOfTwoIntegers(7, 9));
console.log("Power of Four:", powerOfFour(64));
console.log("Steps to Zero:", numberOfStepsToZero(14));
console.log("Excel Column Number:", excelSheetColumnNumber("AB"));
console.log("Fraction to Decimal:", fractionToRecurringDecimal(1, 3));
