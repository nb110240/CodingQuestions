"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None
"""
def isLeaf(node):
    if not node:
        return False
    if not node.left and not node.right:
        return True
    return False

def sum_of_left_leaves(root):
    """
    Write your code here
    :type root: TreeNode
    :rtype: int
    """
    Lsum = 0
    if root is not None:
        if isLeaf(root.left):
            Lsum += root.left.val
        else:          
            Lsum += sum_of_left_leaves(root.left)
        Lsum += sum_of_left_leaves(root.right)
    return Lsum
root = input_binary_tree()
sum = sum_of_left_leaves(root)

print(sum)