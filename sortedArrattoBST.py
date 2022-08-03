def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helperfunc(left,right):
            if left > right:
                return None
            mid = (left+right) //2
            root = TreeNode(nums[mid])
            root.left = helperfunc(left,mid-1)
            root.right = helperfunc(mid+1,right)
            return root
        return helperfunc(0,len(nums)-1)