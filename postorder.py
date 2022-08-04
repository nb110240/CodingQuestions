def postorder(self, root: 'Node') -> List[int]:
    #recursively
        output = []
        def dfs(node):
            if not node: 
                return 
            for i in node.children:
                dfs(i)
            output.append(node.val)
        dfs(root)
        
        return output