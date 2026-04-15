"""
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
- `palindrome_number_math(121) -> True`
- `plus_one([1, 2, 9]) -> [1, 3, 0]`
- `count_primes(10) -> 4`
- `roman_to_integer("MCMXCIV") -> 1994`
- `fraction_to_decimal(1, 3) -> "0.(3)"`
"""


def palindrome_number_string(x: int) -> bool:
    """
    Simple approach:
    - Convert to string
    - Compare with reverse

    Time: O(n)
    Space: O(n)
    """
    return str(x) == str(x)[::-1]


def palindrome_number_math(x: int) -> bool:
    """
    Better math approach:
    - Reverse the number using digits
    - Compare with original

    Debugging steps:
    1. Print digit = x % 10
    2. Print reversed_number each round
    3. Print remaining x after // 10
    """
    if x < 0:
        return False

    original = x
    reversed_number = 0

    while x > 0:
        digit = x % 10
        reversed_number = reversed_number * 10 + digit
        x //= 10

    return original == reversed_number


def reverse_integer(x: int) -> int:
    """
    Reverse the digits of an integer.

    Debugging steps:
    1. Track sign separately
    2. Print digit and reversed_number
    """
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_number = 0

    while x > 0:
        digit = x % 10
        reversed_number = reversed_number * 10 + digit
        x //= 10

    return sign * reversed_number


def plus_one(digits: list[int]) -> list[int]:
    """
    Add one to a number represented as digits.
    """
    result = digits[:]

    for i in range(len(result) - 1, -1, -1):
        if result[i] < 9:
            result[i] += 1
            return result
        result[i] = 0

    return [1] + result


def happy_number(n: int) -> bool:
    """
    A happy number ends in 1 after repeated sum of square of digits.

    Debugging steps:
    1. Print current n
    2. Print seen set
    """
    def next_number(value: int) -> int:
        total = 0
        while value > 0:
            digit = value % 10
            total += digit * digit
            value //= 10
        return total

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = next_number(n)

    return n == 1


def power_of_two_division(n: int) -> bool:
    if n <= 0:
        return False

    while n % 2 == 0:
        n //= 2

    return n == 1


def power_of_two_bitwise(n: int) -> bool:
    """
    A power of two has only one set bit.
    """
    return n > 0 and (n & (n - 1)) == 0


def integer_sqrt(x: int) -> int:
    """
    Find floor(sqrt(x)) using binary search.
    """
    if x < 2:
        return x

    left = 1
    right = x // 2
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == x:
            return mid
        if square < x:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


def power_fast(base: float, exponent: int) -> float:
    """
    Fast exponentiation using divide and conquer.
    """
    if exponent == 0:
        return 1.0

    if exponent < 0:
        return 1 / power_fast(base, -exponent)

    half = power_fast(base, exponent // 2)
    if exponent % 2 == 0:
        return half * half
    return half * half * base


def gcd_euclidean(a: int, b: int) -> int:
    """
    Greatest common divisor using Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)


def lcm_using_gcd(a: int, b: int) -> int:
    """
    Least common multiple using gcd.
    """
    return abs(a * b) // gcd_euclidean(a, b)


def is_prime(n: int) -> bool:
    """
    Prime check up to sqrt(n).
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def count_primes(n: int) -> int:
    """
    Count prime numbers below n using sieve.
    """
    if n <= 2:
        return 0

    is_prime_list = [True] * n
    is_prime_list[0] = False
    is_prime_list[1] = False

    current = 2
    while current * current < n:
        if is_prime_list[current]:
            for multiple in range(current * current, n, current):
                is_prime_list[multiple] = False
        current += 1

    return sum(is_prime_list)


def prime_factors(n: int) -> list[int]:
    """
    Return prime factors in order.
    """
    factors: list[int] = []
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    if n > 1:
        factors.append(n)

    return factors


def missing_number_sum(nums: list[int]) -> int:
    """
    Find missing number using sum formula.
    """
    n = len(nums)
    expected = n * (n + 1) // 2
    return expected - sum(nums)


def single_number_xor(nums: list[int]) -> int:
    """
    Every repeated number cancels out with xor.
    """
    result = 0
    for value in nums:
        result ^= value
    return result


def factorial_trailing_zeroes(n: int) -> int:
    """
    Count factors of 5 in factorial.
    """
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count


def armstrong_number(n: int) -> bool:
    """
    Check if number equals sum of digits powered by number of digits.
    """
    digits = str(n)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == n


def add_digits_loop(num: int) -> int:
    """
    Repeatedly add digits until only one digit remains.

    Debugging steps:
    1. Print current num
    2. Print digit sum after each pass
    """
    while num >= 10:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        num = digit_sum
    return num


def add_digits_math(num: int) -> int:
    """
    Digital root formula.
    """
    if num == 0:
        return 0
    return 1 + (num - 1) % 9


def number_of_one_bits(n: int) -> int:
    """
    Count set bits in a non-negative integer.
    """
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count


def hamming_distance(x: int, y: int) -> int:
    """
    Count differing bit positions between two numbers.
    """
    return number_of_one_bits(x ^ y)


def power_of_three_division(n: int) -> bool:
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1


def perfect_number(num: int) -> bool:
    """
    A perfect number equals the sum of its proper divisors.
    """
    if num <= 1:
        return False

    divisor_sum = 1
    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            divisor_sum += divisor
            if divisor != num // divisor:
                divisor_sum += num // divisor
        divisor += 1

    return divisor_sum == num


def ugly_number(n: int) -> bool:
    """
    Ugly numbers have only 2, 3, and 5 as prime factors.
    """
    if n <= 0:
        return False

    for factor in (2, 3, 5):
        while n % factor == 0:
            n //= factor
    return n == 1


def divide_two_integers(dividend: int, divisor: int) -> int:
    """
    Divide using subtraction by shifted divisors.

    Debugging steps:
    1. Track remaining dividend
    2. Track current shifted divisor and multiple
    3. Apply sign at the end
    """
    if divisor == 0:
        raise ZeroDivisionError("divisor cannot be zero")

    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    dividend = abs(dividend)
    divisor = abs(divisor)
    quotient = 0

    while dividend >= divisor:
        current_divisor = divisor
        multiple = 1
        while dividend >= (current_divisor << 1):
            current_divisor <<= 1
            multiple <<= 1
        dividend -= current_divisor
        quotient += multiple

    return sign * quotient


def fibonacci_iterative(n: int) -> int:
    """
    Return nth Fibonacci number with iterative DP.
    """
    if n <= 1:
        return n

    first = 0
    second = 1
    for _ in range(2, n + 1):
        first, second = second, first + second
    return second


def roman_to_integer(text: str) -> int:
    """
    Convert Roman numeral to integer.
    """
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0

    for index, char in enumerate(text):
        value = values[char]
        if index + 1 < len(text) and value < values[text[index + 1]]:
            total -= value
        else:
            total += value

    return total


def integer_to_roman(num: int) -> str:
    """
    Convert integer to Roman numeral using greedy mapping.
    """
    mapping = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    result: list[str] = []

    for value, symbol in mapping:
        while num >= value:
            result.append(symbol)
            num -= value

    return "".join(result)


def counting_bits(n: int) -> list[int]:
    """
    Return set-bit counts from 0 to n.
    """
    result = [0] * (n + 1)
    for value in range(1, n + 1):
        result[value] = result[value >> 1] + (value & 1)
    return result


def reverse_bits(n: int, bit_size: int = 32) -> int:
    """
    Reverse bits in a fixed-size integer.
    """
    result = 0
    for _ in range(bit_size):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result


def sum_of_two_integers(a: int, b: int) -> int:
    """
    Add numbers using bit manipulation.
    """
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


def power_of_four(n: int) -> bool:
    """
    Check if a number is a power of four.
    """
    return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0


def number_of_steps_to_zero(num: int) -> int:
    """
    Count steps to reduce a number to zero.
    """
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        steps += 1
    return steps


def excel_sheet_column_number(column_title: str) -> int:
    """
    Convert Excel column title to number.
    """
    result = 0
    for char in column_title:
        result = result * 26 + (ord(char) - ord("A") + 1)
    return result


def fraction_to_recurring_decimal(numerator: int, denominator: int) -> str:
    """
    Convert fraction to decimal string and wrap repeating part in parentheses.
    """
    if denominator == 0:
        raise ZeroDivisionError("denominator cannot be zero")
    if numerator == 0:
        return "0"

    sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
    numerator = abs(numerator)
    denominator = abs(denominator)

    integer_part = numerator // denominator
    remainder = numerator % denominator
    if remainder == 0:
        return sign + str(integer_part)

    result = [sign + str(integer_part), "."]
    seen: dict[int, int] = {}

    while remainder != 0:
        if remainder in seen:
            insert_index = seen[remainder]
            result.insert(insert_index, "(")
            result.append(")")
            break

        seen[remainder] = len(result)
        remainder *= 10
        result.append(str(remainder // denominator))
        remainder %= denominator

    return "".join(result)


if __name__ == "__main__":
    print("Palindrome:", palindrome_number_math(121))
    print("Reverse Integer:", reverse_integer(-456))
    print("Plus One:", plus_one([1, 2, 9]))
    print("Happy Number:", happy_number(19))
    print("Power of Two:", power_of_two_bitwise(16))
    print("Integer Sqrt:", integer_sqrt(17))
    print("Power Fast:", power_fast(2, 10))
    print("GCD:", gcd_euclidean(48, 18))
    print("LCM:", lcm_using_gcd(12, 18))
    print("Is Prime:", is_prime(29))
    print("Count Primes:", count_primes(20))
    print("Prime Factors:", prime_factors(84))
    print("Missing Number:", missing_number_sum([3, 0, 1]))
    print("Single Number:", single_number_xor([4, 1, 2, 1, 2]))
    print("Trailing Zeroes:", factorial_trailing_zeroes(25))
    print("Armstrong Number:", armstrong_number(153))
    print("Add Digits:", add_digits_math(38))
    print("Number of 1 Bits:", number_of_one_bits(11))
    print("Hamming Distance:", hamming_distance(1, 4))
    print("Power of Three:", power_of_three_division(27))
    print("Perfect Number:", perfect_number(28))
    print("Ugly Number:", ugly_number(30))
    print("Divide Two Integers:", divide_two_integers(43, 8))
    print("Fibonacci:", fibonacci_iterative(10))
    print("Roman to Integer:", roman_to_integer("MCMXCIV"))
    print("Integer to Roman:", integer_to_roman(1994))
    print("Counting Bits:", counting_bits(5))
    print("Reverse Bits:", reverse_bits(13, 4))
    print("Sum of Two Integers:", sum_of_two_integers(7, 9))
    print("Power of Four:", power_of_four(64))
    print("Steps to Zero:", number_of_steps_to_zero(14))
    print("Excel Column Number:", excel_sheet_column_number("AB"))
    print("Fraction to Decimal:", fraction_to_recurring_decimal(1, 3))
