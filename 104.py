# 104
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

def maxDepth(root):
    if root is None: return 0

    right_height = maxDepth(root.right)
    left_height = maxDepth(root.left)

    return max(right_height, left_height) + 1
