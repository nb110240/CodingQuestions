def doubletree(root):
    if root == None:
        return
    doubletree(root.left)
    doubletree(root.right)
    temp = root.left
    root.left = TreeNode(root.val)
    root.left.left = temp
    return root