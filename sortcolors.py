def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0
        second = 0 
        last = len(nums) -1
        temp = None
        
        while second <= last:
            if nums[second] == 0:
                temp = nums[second]
                nums[second] = nums[first]
                nums[first] = temp
                first += 1
                second += 1
            elif nums[second] == 1:
                second += 1
            else:
                temp = nums[second]
                nums[second] = nums[last]
                nums[last] = temp
                last -= 1
        return nums 