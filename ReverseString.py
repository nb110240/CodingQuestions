def reverseWords(self, s: str) -> str:
        out=''
        count = 0
        wrds= s.split(' ')
        for word in wrds:
            if count!= 0:
                out = out + " "
            out = out + (word[::-1])
            count +=1
            
        return out

