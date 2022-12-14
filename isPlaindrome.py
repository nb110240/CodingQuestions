class Solution:
    def isPalindrome(self, x: int) -> bool:
        pl = str(x)
        st = 0
        end = len(pl)-1
        while (st <= end):
            if pl[st] != pl[end]:
                return False
            st += 1
            end -= 1
        return True
