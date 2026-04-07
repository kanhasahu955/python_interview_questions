"""
Trees and Graphs
================

Common company-style questions:
1. Binary Tree Level Order Traversal
2. Lowest Common Ancestor of a Binary Tree
3. Number of Islands

Quick input/output examples:
- `level_order_traversal([3, 9, 20, null, null, 15, 7]) -> [[3], [9, 20], [15, 7]]`
- `lowest_common_ancestor(root, 5, 1) -> 3`
- `num_islands([["1","1","0"],["1","0","0"],["0","0","1"]]) -> 2`
"""

from collections import deque


class TreeNode:
    def __init__(self, value: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def level_order_traversal(root: TreeNode | None) -> list[list[int]]:
    """
    Approach:
    - Use BFS with a queue
    - Process one level at a time

    Complexity:
    - Time: O(n)
    - Space: O(n)

    Debugging steps:
    1. Print queue at the start of each level
    2. Print collected level values before appending
    """
    if root is None:
        return []

    result: list[list[int]] = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level: list[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


def lowest_common_ancestor(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    """
    Recursive idea:
    - If current node is p or q, return it
    - Search left and right
    - If both sides return a node, current node is the answer

    Debugging steps:
    1. Print current node value
    2. Print left and right recursive results
    """
    if root is None or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


def number_of_islands(grid: list[list[str]]) -> int:
    """
    Problem:
    Count connected groups of '1' in a grid.

    Approach:
    - Walk through every cell
    - When you find land, run DFS and mark the island visited

    Complexity:
    - Time: O(rows * cols)
    - Space: O(rows * cols) in worst case due to recursion/visited

    Debugging steps:
    1. Print cell coordinates when DFS starts
    2. Print each visited land cell
    3. Verify bounds checks before recursive calls
    """
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited: set[tuple[int, int]] = set()

    def dfs(row: int, col: int) -> None:
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if grid[row][col] != "1" or (row, col) in visited:
            return

        visited.add((row, col))

        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    islands = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and (row, col) not in visited:
                islands += 1
                dfs(row, col)

    return islands
