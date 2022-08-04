def printbinaryTree(self, root: TreeNode) -> None:
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.val,end = " ")
    printbinaryTree(root.left)
    printbinaryTree(root.right)
