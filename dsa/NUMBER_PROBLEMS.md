# Number Related DSA Problems

This file focuses only on number-based DSA and interview math problems.

These are very common in coding rounds for experienced developers because they test:

- logic with digits
- modulo and division
- bit manipulation
- math optimization
- binary search on answers
- cycle detection

## Core Number Problems

### 1. Palindrome Number
Check if a number reads the same from left to right and right to left.

Example:
- `121` -> palindrome
- `123` -> not palindrome

What it tests:
- digit extraction
- reverse-number logic

### 2. Reverse Integer
Reverse the digits of a number.

Example:
- `123` -> `321`
- `-456` -> `-654`

What it tests:
- modulo
- integer division
- sign handling

### 3. Plus One
Given digits like `[1, 2, 9]`, return `[1, 3, 0]`.

Input:
- `[1, 2, 9]`

Output:
- `[1, 3, 0]`

What it tests:
- carry logic
- array updates from right to left

### 4. Happy Number
Repeatedly replace the number with the sum of squares of digits.
If it ends in `1`, it is happy.

Input:
- `19`

Output:
- `true`  (1² + 9² = 82 → 8² + 2² = 68 → 6² + 8² = 100 → 1² = 1)

What it tests:
- cycle detection
- digit processing

### 5. Power of Two
Check if a number is a power of two.

Input:
- `16`

Output:
- `true`

Input:
- `18`

Output:
- `false`

What it tests:
- division logic
- bitwise thinking

### 6. Integer Square Root
Find the floor value of square root without using built-in sqrt.

Input:
- `10`

Output:
- `3`

Input:
- `25`

Output:
- `5`

What it tests:
- binary search on number space

### 7. Pow(x, n)
Compute `x` raised to `n`.

Input:
- `x = 2.0`, `n = 10`

Output:
- `1024.0`

Input:
- `x = 2.0`, `n = -2`

Output:
- `0.25`

What it tests:
- exponentiation by squaring
- recursive or iterative math optimization

### 8. GCD and LCM
Find:
- greatest common divisor
- least common multiple

Input:
- `a = 12`, `b = 18`

Output:
- GCD: `6`
- LCM: `36`

What it tests:
- Euclidean algorithm
- number relationships

### 9. Prime Check
Check if a number is prime.

Input:
- `7`

Output:
- `true`

Input:
- `12`

Output:
- `false`

What it tests:
- efficient divisor checking
- stopping at square root

### 10. Count Primes
Count primes smaller than `n`.

Input:
- `10`

Output:
- `4`  (primes: 2, 3, 5, 7)

What it tests:
- sieve of Eratosthenes
- number marking patterns

### 11. Prime Factorization
Break a number into prime factors.

Example:
- `84` -> `[2, 2, 3, 7]`

What it tests:
- repeated division
- factor reduction

### 12. Missing Number
Array contains values from `0` to `n`, with one missing.

Input:
- `[3, 0, 1]`

Output:
- `2`

What it tests:
- sum formula
- xor approach

### 13. Single Number
Every number appears twice except one.

Input:
- `[4, 1, 2, 1, 2]`

Output:
- `4`

What it tests:
- xor cancellation

### 14. Factorial Trailing Zeroes
Count zeros at the end of factorial result.

Input:
- `5`

Output:
- `1`  (5! = 120, one trailing zero)

Input:
- `25`

Output:
- `6`

What it tests:
- counting powers of five

### 15. Armstrong Number
Check if the number is equal to the sum of its digits powered by digit count.

Input:
- `153`

Output:
- `true`  (1³ + 5³ + 3³ = 1 + 125 + 27 = 153)

Input:
- `123`

Output:
- `false`

What it tests:
- digit loops
- power handling

### 16. Add Digits
Keep adding digits until only one digit remains.

Example:
- `38` -> `3 + 8 = 11` -> `1 + 1 = 2`

What it tests:
- repeated digit reduction
- digital root pattern

### 17. Number of 1 Bits
Count how many set bits are present in the binary form of a number.

Input:
- `11`  (binary: `1011`)

Output:
- `3`

What it tests:
- bitwise operators
- binary reasoning

### 18. Hamming Distance
Count how many bit positions differ between two numbers.

Input:
- `x = 1`, `y = 4`

Output:
- `2`  (1 = 0001, 4 = 0100 → two differing bits)

What it tests:
- xor usage
- bit counting

### 19. Power of Three
Check whether a number can be written as `3^k`.

Input:
- `27`

Output:
- `true`  (3³ = 27)

Input:
- `45`

Output:
- `false`

What it tests:
- repeated division
- power recognition

### 20. Perfect Number
Check if a number is equal to the sum of its proper divisors.

Example:
- `28` -> `1 + 2 + 4 + 7 + 14 = 28`

What it tests:
- divisor traversal
- square root optimization

### 21. Ugly Number
Check if the prime factors are only `2`, `3`, and `5`.

Input:
- `6`

Output:
- `true`  (6 = 2 × 3)

Input:
- `14`

Output:
- `false`  (14 = 2 × 7, factor 7 is not allowed)

What it tests:
- repeated factor division
- factor filtering

### 22. Divide Two Integers
Divide without directly using built-in division logic in the core idea.

Input:
- `dividend = 10`, `divisor = 3`

Output:
- `3`

Input:
- `dividend = -7`, `divisor = 2`

Output:
- `-3`

What it tests:
- subtraction by doubles
- shifting and quotient building

### 23. Fibonacci Number
Return the nth Fibonacci number.

Input:
- `6`

Output:
- `8`  (sequence: 0, 1, 1, 2, 3, 5, 8)

What it tests:
- recurrence relation
- iterative DP
- recursion to iteration optimization

### 24. Roman to Integer
Convert a Roman numeral string into an integer.

Input:
- `"MCMXCIV"`

Output:
- `1994`

Input:
- `"III"`

Output:
- `3`

What it tests:
- symbol mapping
- left-to-right parsing rules

### 25. Integer to Roman
Convert an integer into Roman numeral form.

Input:
- `1994`

Output:
- `"MCMXCIV"`

Input:
- `58`

Output:
- `"LVIII"`

What it tests:
- greedy value selection
- ordered mapping

### 26. Counting Bits
For every number from `0` to `n`, return the count of set bits.

Input:
- `5`

Output:
- `[0, 1, 1, 2, 1, 2]`  (0→0, 1→1, 2→10, 3→11, 4→100, 5→101)

What it tests:
- DP over bits
- reuse of previous result

### 27. Reverse Bits
Reverse the binary bits of a number.

Input:
- `43261596`  (binary: `00000010100101000001111010011100`)

Output:
- `964176192`  (binary: `00111001011110000010100101000000`)

What it tests:
- shifting
- bit extraction

### 28. Sum of Two Integers
Add two integers without using the `+` operator in the main idea.

Input:
- `a = 1`, `b = 2`

Output:
- `3`

Input:
- `a = -2`, `b = 3`

Output:
- `1`

What it tests:
- xor
- carry with bit operations

### 29. Power of Four
Check if a number is a valid power of four.

Input:
- `16`

Output:
- `true`  (4² = 16)

Input:
- `5`

Output:
- `false`

What it tests:
- power filtering
- bit and modulo patterns

### 30. Number of Steps to Reduce to Zero
If number is even divide by 2, else subtract 1, until it becomes zero.

Input:
- `14`

Output:
- `6`  (14→7→6→3→2→1→0)

What it tests:
- parity checks
- loop counting

### 31. Excel Sheet Column Number
Convert Excel column names like `AB` into a number.

Input:
- `"A"`

Output:
- `1`

Input:
- `"AB"`

Output:
- `28`

What it tests:
- base-26 style conversion
- character math

### 32. Fraction to Recurring Decimal
Convert a fraction into decimal form and mark repeating parts.

Input:
- `numerator = 1`, `denominator = 3`

Output:
- `"0.(3)"`

Input:
- `numerator = 4`, `denominator = 333`

Output:
- `"0.(012)"`

What it tests:
- remainder tracking
- map-based cycle detection

## Best Preparation Order

1. Palindrome Number
2. Reverse Integer
3. Plus One
4. Power of Two
5. GCD and LCM
6. Prime Check
7. Prime Factorization
8. Happy Number
9. Missing Number
10. Single Number
11. Sqrt(x)
12. Pow(x, n)
13. Count Primes
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

## Debugging Pattern For Number Problems

When debugging number questions:

1. Print the current number.
2. Print the extracted digit using `% 10`.
3. Print the remaining number after `// 10` or `Math.floor(n / 10)`.
4. Print intermediate result after every update.
5. For cycle problems, print the visited set.
6. For binary search problems, print `left`, `right`, and `mid`.
7. For bit problems, print binary representation if needed.

## Code Files

- `python/number_problems.py`
- `javascript/number_problems.js`
