# 226
# https://leetcode.com/problems/invert-binary-tree/

def invertTree(root):
    if root is None: return None
        
    right = self.invertTree(root.right)
    left = self.invertTree(root.left)
        
    root.right = left
    root.left = right
        
    return root
