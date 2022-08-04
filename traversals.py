def listtoBinaryTrees(vals: List[int]):
    return 

def preOrderTrav(node TreeNode) -> None:
    if node: 
        print(node.val)
        preOrderTrav(node.left)
        preOrderTrav(node.right)
    return

def inOrderTrav(node TreeNode) -> None:
    if node: 
        inOrderTrav(node.left)
        print(node.val)
        inOrderTrav(node.right)
    return

def postOrderTrav(node TreeNode) -> None:
    if node:
        postOrderTrav(node.left)
        postOrderTrav(node.right)
        print(node.val)
    return
