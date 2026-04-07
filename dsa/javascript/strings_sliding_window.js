/*
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

Quick input/output examples:
- validAnagramCount("listen", "silent") -> true
- groupAnagrams(["eat", "tea", "ate"]) -> [["eat", "tea", "ate"]]
- longestUniqueSubstringWindow("abcabcbb") -> 3
- minimumWindowSubstring("ADOBECODEBANC", "ABC") -> "BANC"
- longestPalindromicSubstring("babad") -> "bab" or "aba"
- validPalindrome("A man, a plan, a canal: Panama") -> true
- longestCommonPrefix(["flower", "flow", "flight"]) -> "fl"
- findAllAnagrams("cbaebabacd", "abc") -> [0, 6]
- permutationInString("ab", "eidbaooo") -> true
- countPalindromicSubstrings("aaa") -> 6
- encodeStrings(["leet", "code"]) -> "4#leet4#code"
- decodeString("3[a2[c]]") -> "accaccacc"
*/

function validAnagramSort(s, t) {
  return [...s].sort().join("") === [...t].sort().join("");
}

function validAnagramCount(s, t) {
  if (s.length !== t.length) {
    return false;
  }

  const count = new Map();
  for (const char of s) {
    count.set(char, (count.get(char) || 0) + 1);
  }

  for (const char of t) {
    if (!count.has(char)) {
      return false;
    }
    count.set(char, count.get(char) - 1);
    if (count.get(char) === 0) {
      count.delete(char);
    }
  }

  return count.size === 0;
}

function groupAnagrams(words) {
  const groups = new Map();

  for (const word of words) {
    const key = [...word].sort().join("");
    if (!groups.has(key)) {
      groups.set(key, []);
    }
    groups.get(key).push(word);
  }

  return [...groups.values()];
}

function longestUniqueSubstringWindow(text) {
  /*
  Debugging steps:
  1. Print left, right, current char
  2. Print map after updates
  */
  const seen = new Map();
  let left = 0;
  let best = 0;

  for (let right = 0; right < text.length; right += 1) {
    const char = text[right];
    if (seen.has(char) && seen.get(char) >= left) {
      left = seen.get(char) + 1;
    }
    seen.set(char, right);
    best = Math.max(best, right - left + 1);
  }

  return best;
}

function minimumWindowSubstring(source, target) {
  if (!source || !target) {
    return "";
  }

  const need = new Map();
  for (const char of target) {
    need.set(char, (need.get(char) || 0) + 1);
  }

  const window = new Map();
  let formed = 0;
  const required = need.size;
  let left = 0;
  let bestLength = Infinity;
  let bestStart = 0;

  for (let right = 0; right < source.length; right += 1) {
    const char = source[right];
    window.set(char, (window.get(char) || 0) + 1);

    if (need.has(char) && window.get(char) === need.get(char)) {
      formed += 1;
    }

    while (formed === required) {
      if (right - left + 1 < bestLength) {
        bestLength = right - left + 1;
        bestStart = left;
      }

      const leftChar = source[left];
      window.set(leftChar, window.get(leftChar) - 1);
      if (need.has(leftChar) && window.get(leftChar) < need.get(leftChar)) {
        formed -= 1;
      }
      left += 1;
    }
  }

  return bestLength === Infinity ? "" : source.slice(bestStart, bestStart + bestLength);
}

function longestPalindromicSubstring(text) {
  if (!text) {
    return "";
  }

  let best = "";

  function expand(left, right) {
    while (left >= 0 && right < text.length && text[left] === text[right]) {
      left -= 1;
      right += 1;
    }
    return text.slice(left + 1, right);
  }

  for (let index = 0; index < text.length; index += 1) {
    const odd = expand(index, index);
    const even = expand(index, index + 1);
    const current = odd.length > even.length ? odd : even;
    if (current.length > best.length) {
      best = current;
    }
  }

  return best;
}

function validPalindrome(text) {
  let left = 0;
  let right = text.length - 1;

  while (left < right) {
    while (left < right && !/[a-z0-9]/i.test(text[left])) {
      left += 1;
    }
    while (left < right && !/[a-z0-9]/i.test(text[right])) {
      right -= 1;
    }

    if (text[left].toLowerCase() !== text[right].toLowerCase()) {
      return false;
    }

    left += 1;
    right -= 1;
  }

  return true;
}

function longestCommonPrefix(words) {
  if (!words.length) {
    return "";
  }

  let prefix = words[0];
  for (let index = 1; index < words.length; index += 1) {
    while (!words[index].startsWith(prefix)) {
      prefix = prefix.slice(0, -1);
      if (!prefix) {
        return "";
      }
    }
  }

  return prefix;
}

function findAllAnagrams(source, target) {
  if (target.length > source.length) {
    return [];
  }

  const need = new Map();
  const window = new Map();
  const result = [];

  for (const char of target) {
    need.set(char, (need.get(char) || 0) + 1);
  }

  function sameCounts() {
    if (need.size !== window.size) {
      return false;
    }
    for (const [key, value] of need.entries()) {
      if (window.get(key) !== value) {
        return false;
      }
    }
    return true;
  }

  for (let index = 0; index < target.length; index += 1) {
    const char = source[index];
    window.set(char, (window.get(char) || 0) + 1);
  }

  if (sameCounts()) {
    result.push(0);
  }

  for (let right = target.length; right < source.length; right += 1) {
    const addChar = source[right];
    window.set(addChar, (window.get(addChar) || 0) + 1);

    const removeChar = source[right - target.length];
    window.set(removeChar, window.get(removeChar) - 1);
    if (window.get(removeChar) === 0) {
      window.delete(removeChar);
    }

    if (sameCounts()) {
      result.push(right - target.length + 1);
    }
  }

  return result;
}

function permutationInString(pattern, text) {
  return findAllAnagrams(text, pattern).length > 0;
}

function countPalindromicSubstrings(text) {
  let count = 0;

  function expand(left, right) {
    let localCount = 0;
    while (left >= 0 && right < text.length && text[left] === text[right]) {
      localCount += 1;
      left -= 1;
      right += 1;
    }
    return localCount;
  }

  for (let index = 0; index < text.length; index += 1) {
    count += expand(index, index);
    count += expand(index, index + 1);
  }

  return count;
}

function encodeStrings(strings) {
  return strings.map((item) => `${item.length}#${item}`).join("");
}

function decodeStrings(encoded) {
  const result = [];
  let index = 0;

  while (index < encoded.length) {
    let separator = index;
    while (encoded[separator] !== "#") {
      separator += 1;
    }
    const length = Number(encoded.slice(index, separator));
    const start = separator + 1;
    const end = start + length;
    result.push(encoded.slice(start, end));
    index = end;
  }

  return result;
}

function longestRepeatingCharacterReplacement(text, k) {
  const counts = new Map();
  let left = 0;
  let best = 0;
  let maxFrequency = 0;

  for (let right = 0; right < text.length; right += 1) {
    const char = text[right];
    counts.set(char, (counts.get(char) || 0) + 1);
    maxFrequency = Math.max(maxFrequency, counts.get(char));

    while (right - left + 1 - maxFrequency > k) {
      const leftChar = text[left];
      counts.set(leftChar, counts.get(leftChar) - 1);
      left += 1;
    }

    best = Math.max(best, right - left + 1);
  }

  return best;
}

function zigzagConversion(text, numRows) {
  if (numRows === 1 || numRows >= text.length) {
    return text;
  }

  const rows = new Array(numRows).fill("");
  let currentRow = 0;
  let direction = 1;

  for (const char of text) {
    rows[currentRow] += char;
    if (currentRow === 0) {
      direction = 1;
    } else if (currentRow === numRows - 1) {
      direction = -1;
    }
    currentRow += direction;
  }

  return rows.join("");
}

function stringToIntegerAtoi(text) {
  text = text.trimStart();
  if (!text) {
    return 0;
  }

  let sign = 1;
  let index = 0;
  if (text[index] === "+" || text[index] === "-") {
    sign = text[index] === "-" ? -1 : 1;
    index += 1;
  }

  let result = 0;
  while (index < text.length && /\d/.test(text[index])) {
    result = result * 10 + Number(text[index]);
    index += 1;
  }

  result *= sign;
  const lowerBound = -(2 ** 31);
  const upperBound = 2 ** 31 - 1;
  return Math.max(lowerBound, Math.min(upperBound, result));
}

function implementStrStr(haystack, needle) {
  if (needle === "") {
    return 0;
  }

  for (let start = 0; start <= haystack.length - needle.length; start += 1) {
    if (haystack.slice(start, start + needle.length) === needle) {
      return start;
    }
  }
  return -1;
}

function decodeString(text) {
  const stack = [];
  let currentString = "";
  let currentNumber = 0;

  for (const char of text) {
    if (/\d/.test(char)) {
      currentNumber = currentNumber * 10 + Number(char);
    } else if (char === "[") {
      stack.push([currentString, currentNumber]);
      currentString = "";
      currentNumber = 0;
    } else if (char === "]") {
      const [previousString, repeatCount] = stack.pop();
      currentString = previousString + currentString.repeat(repeatCount);
    } else {
      currentString += char;
    }
  }

  return currentString;
}

function substringWithConcatenationOfAllWords(text, words) {
  if (!text || !words.length) {
    return [];
  }

  const wordLength = words[0].length;
  const totalWords = words.length;
  const totalLength = wordLength * totalWords;
  const target = new Map();
  const result = [];

  for (const word of words) {
    target.set(word, (target.get(word) || 0) + 1);
  }

  for (let offset = 0; offset < wordLength; offset += 1) {
    let left = offset;
    const seen = new Map();
    let usedWords = 0;

    for (let right = offset; right <= text.length - wordLength; right += wordLength) {
      const word = text.slice(right, right + wordLength);

      if (target.has(word)) {
        seen.set(word, (seen.get(word) || 0) + 1);
        usedWords += 1;

        while (seen.get(word) > target.get(word)) {
          const leftWord = text.slice(left, left + wordLength);
          seen.set(leftWord, seen.get(leftWord) - 1);
          usedWords -= 1;
          left += wordLength;
        }

        if (usedWords === totalWords) {
          result.push(left);
          const leftWord = text.slice(left, left + wordLength);
          seen.set(leftWord, seen.get(leftWord) - 1);
          usedWords -= 1;
          left += wordLength;
        }
      } else {
        seen.clear();
        usedWords = 0;
        left = right + wordLength;
      }
    }
  }

  return result.filter((index) => index <= text.length - totalLength);
}

console.log("Valid Anagram:", validAnagramCount("listen", "silent"));
console.log("Group Anagrams:", groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
console.log("Longest Unique Substring:", longestUniqueSubstringWindow("abcabcbb"));
console.log("Minimum Window:", minimumWindowSubstring("ADOBECODEBANC", "ABC"));
console.log("Longest Palindromic Substring:", longestPalindromicSubstring("babad"));
console.log("Valid Palindrome:", validPalindrome("A man, a plan, a canal: Panama"));
console.log("Longest Common Prefix:", longestCommonPrefix(["flower", "flow", "flight"]));
console.log("Find All Anagrams:", findAllAnagrams("cbaebabacd", "abc"));
console.log("Permutation In String:", permutationInString("ab", "eidbaooo"));
console.log("Count Palindromic Substrings:", countPalindromicSubstrings("aaa"));
const encoded = encodeStrings(["leet", "code", "python"]);
console.log("Encode Strings:", encoded);
console.log("Decode Strings:", decodeStrings(encoded));
console.log("Longest Repeating Character Replacement:", longestRepeatingCharacterReplacement("AABABBA", 1));
console.log("Zigzag Conversion:", zigzagConversion("PAYPALISHIRING", 3));
console.log("String to Integer:", stringToIntegerAtoi("   -42"));
console.log("Implement strStr:", implementStrStr("sadbutsad", "sad"));
console.log("Decode String:", decodeString("3[a2[c]]"));
console.log(
  "Substring With Concatenation:",
  substringWithConcatenationOfAllWords("barfoothefoobarman", ["foo", "bar"])
);
