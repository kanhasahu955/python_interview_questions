"""
Stack and Queue
===============

Common company-style questions:
1. Valid Parentheses
2. Daily Temperatures
3. Implement Queue Using Stacks

Quick input/output examples:
- `valid_parentheses("()[]{}") -> True`
- `daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) -> [1, 1, 4, 2, 1, 1, 0, 0]`
- `QueueUsingStacks().push(1), push(2), peek() -> 1`
"""


def valid_parentheses(expression: str) -> bool:
    """
    Approach:
    - Push opening brackets onto stack
    - On closing bracket, pop and compare

    Complexity:
    - Time: O(n)
    - Space: O(n)

    Debugging steps:
    1. Print current character and stack
    2. Check mismatched closing brackets carefully
    """
    mapping = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []

    for char in expression:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False

    return len(stack) == 0


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    Problem:
    For each day, find how many days you must wait until a warmer temperature.

    Approach:
    - Use a monotonic decreasing stack of indices
    - When current temperature is warmer, resolve previous days

    Complexity:
    - Time: O(n)
    - Space: O(n)

    Debugging steps:
    1. Print stack indices and their temperatures
    2. Print result updates when popping
    """
    result = [0] * len(temperatures)
    stack: list[int] = []

    for index, temperature in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temperature:
            previous_index = stack.pop()
            result[previous_index] = index - previous_index
        stack.append(index)

    return result


class QueueUsingStacks:
    """
    Idea:
    - in_stack handles pushes
    - out_stack handles pops

    Debugging steps:
    1. Print both stacks after each operation
    2. During pop or peek, move elements only when out_stack is empty
    """

    def __init__(self) -> None:
        self.in_stack: list[int] = []
        self.out_stack: list[int] = []

    def push(self, value: int) -> None:
        self.in_stack.append(value)

    def _transfer(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self._transfer()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._transfer()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
