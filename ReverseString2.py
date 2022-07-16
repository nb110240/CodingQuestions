def reverseStr(self, s: str, k: int) -> str:
        i = 0
        out = ''
        while i <= len(s):
            
            substring = s[i:(i+k)]
            out = out + substring[::-1] +s[i+k:i+2*k]
            
            i += 2*k
        return out