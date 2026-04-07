"""
Strings and Sliding Window
==========================

Common company-style questions:
1. Valid Anagram
2. Group Anagrams
3. Longest Substring Without Repeating Characters
4. Minimum Window Substring
5. Longest Palindromic Substring
6. Valid Palindrome
7. Longest Common Prefix
8. Find All Anagrams in a String
9. Permutation in String
10. Count Palindromic Substrings
11. Encode and Decode Strings

This topic tests:
- frequency maps
- pointer movement
- substring optimization

Quick input/output examples:
- `valid_anagram_count("listen", "silent") -> True`
- `group_anagrams(["eat", "tea", "ate"]) -> [["eat", "tea", "ate"]]`
- `longest_unique_substring_window("abcabcbb") -> 3`
- `minimum_window_substring("ADOBECODEBANC", "ABC") -> "BANC"`
- `longest_palindromic_substring("babad") -> "bab" or "aba"`
- `valid_palindrome("A man, a plan, a canal: Panama") -> True`
- `longest_common_prefix(["flower", "flow", "flight"]) -> "fl"`
- `find_all_anagrams("cbaebabacd", "abc") -> [0, 6]`
- `permutation_in_string("ab", "eidbaooo") -> True`
- `count_palindromic_substrings("aaa") -> 6`
- `encode_strings(["leet", "code"]) -> "4#leet4#code"`
- `decode_string("3[a2[c]]") -> "accaccacc"`
"""

from collections import Counter, defaultdict


def valid_anagram_sort(s: str, t: str) -> bool:
    """
    Approach:
    - Sort both strings
    - Compare them

    Complexity:
    - Time: O(n log n)
    - Space: O(n)

    Debugging steps:
    1. Print sorted versions of both strings
    2. Check lengths before sorting
    """
    return sorted(s) == sorted(t)


def valid_anagram_count(s: str, t: str) -> bool:
    """
    Better approach:
    - Count characters in both strings
    - Compare counters

    Complexity:
    - Time: O(n)
    - Space: O(n)
    """
    return Counter(s) == Counter(t)


def group_anagrams(words: list[str]) -> list[list[str]]:
    """
    Group words that are anagrams of each other.

    Approach:
    - Use sorted word as key
    - Append original word to that group

    Complexity:
    - Time: O(n * k log k)
    - Space: O(n * k)

    Debugging steps:
    1. Print each word and its normalized key
    2. Print the map after insertion
    """
    groups: dict[str, list[str]] = {}
    for word in words:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())


def longest_unique_substring_bruteforce(text: str) -> int:
    """
    Approach:
    - Check every substring
    - Keep the longest one with unique characters

    Complexity:
    - Time: O(n^3)
    - Space: O(n)

    Debugging steps:
    1. Print current substring
    2. Print set length versus substring length
    """
    best = 0
    for left in range(len(text)):
        for right in range(left, len(text)):
            current = text[left : right + 1]
            if len(set(current)) == len(current):
                best = max(best, len(current))
    return best


def longest_unique_substring_window(text: str) -> int:
    """
    Optimized sliding window:
    - Expand right pointer
    - Shrink left pointer until the window becomes unique

    Complexity:
    - Time: O(n)
    - Space: O(n)

    Debugging steps:
    1. Print left, right, current character
    2. Print window counts when shrinking
    3. Track when best answer changes
    """
    seen: dict[str, int] = {}
    left = 0
    best = 0

    for right, char in enumerate(text):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        best = max(best, right - left + 1)

    return best


def minimum_window_substring(source: str, target: str) -> str:
    """
    Problem:
    Find the smallest substring of source containing all characters of target.

    Core idea:
    - need = required character counts
    - have = counts inside current window
    - Expand right until valid
    - Shrink left while still valid

    Complexity:
    - Time: O(n)
    - Space: O(n)

    Debugging steps:
    1. Print need and window maps
    2. Track formed count against required count
    3. Print best window updates
    """
    if not source or not target:
        return ""

    need = Counter(target)
    window = defaultdict(int)
    formed = 0
    required = len(need)
    left = 0
    best_length = float("inf")
    best_range = (0, 0)

    for right, char in enumerate(source):
        window[char] += 1
        if char in need and window[char] == need[char]:
            formed += 1

        while formed == required:
            if right - left + 1 < best_length:
                best_length = right - left + 1
                best_range = (left, right)

            left_char = source[left]
            window[left_char] -= 1
            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1
            left += 1

    if best_length == float("inf"):
        return ""
    start, end = best_range
    return source[start : end + 1]


def longest_palindromic_substring(text: str) -> str:
    """
    Expand around every possible center.

    Complexity:
    - Time: O(n^2)
    - Space: O(1)

    Debugging steps:
    1. Print left and right center
    2. Print substring while expanding
    """
    if not text:
        return ""

    best = ""

    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(text) and text[left] == text[right]:
            left -= 1
            right += 1
        return text[left + 1 : right]

    for index in range(len(text)):
        odd = expand(index, index)
        even = expand(index, index + 1)
        current = odd if len(odd) > len(even) else even
        if len(current) > len(best):
            best = current

    return best


def valid_palindrome(text: str) -> bool:
    """
    Ignore non-alphanumeric characters and compare from both ends.
    """
    left = 0
    right = len(text) - 1

    while left < right:
        while left < right and not text[left].isalnum():
            left += 1
        while left < right and not text[right].isalnum():
            right -= 1

        if text[left].lower() != text[right].lower():
            return False

        left += 1
        right -= 1

    return True


def longest_common_prefix(words: list[str]) -> str:
    """
    Compare characters position by position.
    """
    if not words:
        return ""

    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def find_all_anagrams(source: str, target: str) -> list[int]:
    """
    Return all start indices where an anagram of target appears.
    """
    if len(target) > len(source):
        return []

    target_count = Counter(target)
    window = Counter(source[: len(target)])
    result: list[int] = []

    if window == target_count:
        result.append(0)

    for right in range(len(target), len(source)):
        window[source[right]] += 1
        left_char = source[right - len(target)]
        window[left_char] -= 1
        if window[left_char] == 0:
            del window[left_char]
        if window == target_count:
            result.append(right - len(target) + 1)

    return result


def permutation_in_string(pattern: str, text: str) -> bool:
    """
    Check whether any permutation of pattern exists in text.
    """
    return len(find_all_anagrams(text, pattern)) > 0


def count_palindromic_substrings(text: str) -> int:
    """
    Count all palindromic substrings by expanding around centers.
    """
    count = 0

    def expand(left: int, right: int) -> int:
        local_count = 0
        while left >= 0 and right < len(text) and text[left] == text[right]:
            local_count += 1
            left -= 1
            right += 1
        return local_count

    for index in range(len(text)):
        count += expand(index, index)
        count += expand(index, index + 1)

    return count


def encode_strings(strings: list[str]) -> str:
    """
    Encode a list of strings using length prefixes.
    """
    return "".join(f"{len(item)}#{item}" for item in strings)


def decode_strings(encoded: str) -> list[str]:
    """
    Decode a length-prefixed encoded string.
    """
    result: list[str] = []
    index = 0

    while index < len(encoded):
        separator = index
        while encoded[separator] != "#":
            separator += 1
        length = int(encoded[index:separator])
        start = separator + 1
        end = start + length
        result.append(encoded[start:end])
        index = end

    return result


def longest_repeating_character_replacement(text: str, k: int) -> int:
    """
    Find the longest window that can become one repeating character
    after at most k replacements.
    """
    counts: dict[str, int] = defaultdict(int)
    left = 0
    best = 0
    max_frequency = 0

    for right, char in enumerate(text):
        counts[char] += 1
        max_frequency = max(max_frequency, counts[char])

        while (right - left + 1) - max_frequency > k:
            counts[text[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best


def zigzag_conversion(text: str, num_rows: int) -> str:
    """
    Arrange text in zigzag order and read row by row.
    """
    if num_rows == 1 or num_rows >= len(text):
        return text

    rows = [""] * num_rows
    current_row = 0
    direction = 1

    for char in text:
        rows[current_row] += char
        if current_row == 0:
            direction = 1
        elif current_row == num_rows - 1:
            direction = -1
        current_row += direction

    return "".join(rows)


def string_to_integer_atoi(text: str) -> int:
    """
    Parse string into integer while handling spaces and sign.
    """
    text = text.lstrip()
    if not text:
        return 0

    sign = 1
    index = 0
    if text[index] in "+-":
        sign = -1 if text[index] == "-" else 1
        index += 1

    result = 0
    while index < len(text) and text[index].isdigit():
        result = result * 10 + int(text[index])
        index += 1

    result *= sign
    lower_bound = -(2**31)
    upper_bound = 2**31 - 1
    return max(lower_bound, min(upper_bound, result))


def implement_strstr(haystack: str, needle: str) -> int:
    """
    Return the first index of needle in haystack.
    """
    if needle == "":
        return 0

    for start in range(len(haystack) - len(needle) + 1):
        if haystack[start : start + len(needle)] == needle:
            return start
    return -1


def decode_string(text: str) -> str:
    """
    Decode nested repeat expressions like 3[a2[c]].
    """
    stack: list[tuple[str, int]] = []
    current_string = ""
    current_number = 0

    for char in text:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char == "[":
            stack.append((current_string, current_number))
            current_string = ""
            current_number = 0
        elif char == "]":
            previous_string, repeat_count = stack.pop()
            current_string = previous_string + current_string * repeat_count
        else:
            current_string += char

    return current_string


def substring_with_concatenation_of_all_words(text: str, words: list[str]) -> list[int]:
    """
    Find start indices where all words appear exactly once without gaps.
    """
    if not text or not words:
        return []

    word_length = len(words[0])
    total_words = len(words)
    total_length = word_length * total_words
    target = Counter(words)
    result: list[int] = []

    for offset in range(word_length):
        left = offset
        seen: dict[str, int] = defaultdict(int)
        used_words = 0

        for right in range(offset, len(text) - word_length + 1, word_length):
            word = text[right : right + word_length]
            if word in target:
                seen[word] += 1
                used_words += 1

                while seen[word] > target[word]:
                    left_word = text[left : left + word_length]
                    seen[left_word] -= 1
                    used_words -= 1
                    left += word_length

                if used_words == total_words:
                    result.append(left)
                    left_word = text[left : left + word_length]
                    seen[left_word] -= 1
                    used_words -= 1
                    left += word_length
            else:
                seen.clear()
                used_words = 0
                left = right + word_length

    valid_limit = len(text) - total_length
    return [index for index in result if index <= valid_limit]


if __name__ == "__main__":
    print("Valid Anagram:", valid_anagram_count("listen", "silent"))
    print("Group Anagrams:", group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print("Longest Unique Substring:", longest_unique_substring_window("abcabcbb"))
    print("Minimum Window Substring:", minimum_window_substring("ADOBECODEBANC", "ABC"))
    print("Longest Palindromic Substring:", longest_palindromic_substring("babad"))
    print("Valid Palindrome:", valid_palindrome("A man, a plan, a canal: Panama"))
    print("Longest Common Prefix:", longest_common_prefix(["flower", "flow", "flight"]))
    print("Find All Anagrams:", find_all_anagrams("cbaebabacd", "abc"))
    print("Permutation In String:", permutation_in_string("ab", "eidbaooo"))
    print("Count Palindromic Substrings:", count_palindromic_substrings("aaa"))
    encoded = encode_strings(["leet", "code", "python"])
    print("Encode Strings:", encoded)
    print("Decode Strings:", decode_strings(encoded))
    print("Longest Repeating Character Replacement:", longest_repeating_character_replacement("AABABBA", 1))
    print("Zigzag Conversion:", zigzag_conversion("PAYPALISHIRING", 3))
    print("String to Integer:", string_to_integer_atoi("   -42"))
    print("Implement strStr:", implement_strstr("sadbutsad", "sad"))
    print("Decode String:", decode_string("3[a2[c]]"))
    print(
        "Substring With Concatenation:",
        substring_with_concatenation_of_all_words("barfoothefoobarman", ["foo", "bar"]),
    )
