class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = sorted(nums)
        i = 0
        while i < len(a)-1:
            if a[i] != a[i+1]:
                return a[i]
            i +=2
        return a[len(a)-1]