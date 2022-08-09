# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return validate(root)

def validate(node, low=-math.inf, high=math.inf):
    # 1. Base Case: Empty trees are valid BSTs
    if not node:
        return True
    # 2. The current node's value must be between low and high
    if node.val <= low or node.val >= high:
        return False

    # 3. Check if the left and right subtree must also be valid
    return (validate(node.right, node.val, high) and
            validate(node.left, low, node.val))
            