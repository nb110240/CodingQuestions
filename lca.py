class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree (Curr_node):
            if not Curr_node:
                return
            left = recurse_tree(Curr_node.left)
            right = recurse_tree(Curr_node.right)

            mid = Curr_node == p or Curr_node ==q
            if mid + left + right >= 2:
                self.ans = Curr_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans