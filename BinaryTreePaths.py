def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        all_path = []
        self.helpermeth(root,[],all_path)
        return all_path
    
    
    def helpermeth(self,root,cur_path,all_path):
            if not root:
                return
            cur_path.append(str(root.val))
            if not root.left and not root.right:
                all_path.append('->'.join(cur_path))
            self.helpermeth(root.left,cur_path,all_path)
            self.helpermeth(root.right,cur_path,all_path)
            cur_path.pop()