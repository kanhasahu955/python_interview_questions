/*
Trees and Graphs
================

Common company-style questions:
1. Binary Tree Level Order Traversal
2. Lowest Common Ancestor
3. Number of Islands

Quick input/output examples:
- `levelOrderTraversal([3, 9, 20, null, null, 15, 7]) -> [[3], [9, 20], [15, 7]]`
- `lowestCommonAncestor(root, 5, 1) -> 3`
- `numIslands([["1","1","0"],["1","0","0"],["0","0","1"]]) -> 2`
*/

class TreeNode {
  constructor(value = 0, left = null, right = null) {
    this.value = value;
    this.left = left;
    this.right = right;
  }
}

function levelOrderTraversal(root) {
  if (!root) {
    return [];
  }

  const result = [];
  const queue = [root];

  while (queue.length) {
    const levelSize = queue.length;
    const level = [];

    for (let i = 0; i < levelSize; i += 1) {
      const node = queue.shift();
      level.push(node.value);

      if (node.left) {
        queue.push(node.left);
      }
      if (node.right) {
        queue.push(node.right);
      }
    }

    result.push(level);
  }

  return result;
}

function lowestCommonAncestor(root, p, q) {
  if (!root || root === p || root === q) {
    return root;
  }

  const left = lowestCommonAncestor(root.left, p, q);
  const right = lowestCommonAncestor(root.right, p, q);

  if (left && right) {
    return root;
  }

  return left || right;
}

function numberOfIslands(grid) {
  if (!grid.length) {
    return 0;
  }

  const rows = grid.length;
  const cols = grid[0].length;
  const visited = new Set();

  function dfs(row, col) {
    const key = `${row},${col}`;
    if (row < 0 || row >= rows || col < 0 || col >= cols) {
      return;
    }
    if (grid[row][col] !== "1" || visited.has(key)) {
      return;
    }

    visited.add(key);
    dfs(row + 1, col);
    dfs(row - 1, col);
    dfs(row, col + 1);
    dfs(row, col - 1);
  }

  let islands = 0;
  for (let row = 0; row < rows; row += 1) {
    for (let col = 0; col < cols; col += 1) {
      const key = `${row},${col}`;
      if (grid[row][col] === "1" && !visited.has(key)) {
        islands += 1;
        dfs(row, col);
      }
    }
  }

  return islands;
}
