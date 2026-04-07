/*
Stack and Queue
===============

Common company-style questions:
1. Valid Parentheses
2. Daily Temperatures
3. Implement Queue Using Stacks

Quick input/output examples:
- `validParentheses("()[]{}") -> true`
- `dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) -> [1, 1, 4, 2, 1, 1, 0, 0]`
- `queueUsingStacks.push(1), push(2), peek() -> 1`
*/

function validParentheses(expression) {
  const mapping = new Map([
    [")", "("],
    ["]", "["],
    ["}", "{"],
  ]);
  const stack = [];

  for (const char of expression) {
    if (mapping.has(char)) {
      if (!stack.length || stack.pop() !== mapping.get(char)) {
        return false;
      }
    } else {
      stack.push(char);
    }
  }

  return stack.length === 0;
}

function dailyTemperatures(temperatures) {
  const result = new Array(temperatures.length).fill(0);
  const stack = [];

  for (let index = 0; index < temperatures.length; index += 1) {
    while (stack.length && temperatures[stack[stack.length - 1]] < temperatures[index]) {
      const previousIndex = stack.pop();
      result[previousIndex] = index - previousIndex;
    }
    stack.push(index);
  }

  return result;
}

class QueueUsingStacks {
  constructor() {
    this.inStack = [];
    this.outStack = [];
  }

  push(value) {
    this.inStack.push(value);
  }

  transfer() {
    if (!this.outStack.length) {
      while (this.inStack.length) {
        this.outStack.push(this.inStack.pop());
      }
    }
  }

  pop() {
    this.transfer();
    return this.outStack.pop();
  }

  peek() {
    this.transfer();
    return this.outStack[this.outStack.length - 1];
  }

  empty() {
    return this.inStack.length === 0 && this.outStack.length === 0;
  }
}
