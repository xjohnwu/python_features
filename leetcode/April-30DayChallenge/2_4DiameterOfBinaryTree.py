"""
Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the
length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""


import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        local_max, global_max = self.diameter(root)
        return global_max

    def diameter(self, root: TreeNode) -> (int, int):  # local_max, global_max
        if root is None:
            return 0, 0
        l_max, global_max = self.diameter(root.left)
        r_max, global_max = self.diameter(root.right)
        return max(l_max, r_max) + 1, max(global_max, l_max + r_max)


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)


@pytest.mark.parametrize("tree_node, expected", [
    (t, 3),
])
def test_solution(tree_node, expected):
    s = Solution()
    assert s.diameterOfBinaryTree(tree_node) == expected
