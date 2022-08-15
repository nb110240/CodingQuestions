class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        '''
        i = 0
        if max(nums) != len(nums):
            return len(nums)
        while i <= len(nums):
            if i not in nums:
                return i
            i +=1
            