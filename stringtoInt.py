def stringtoInt(self, s: str) -> int:
    # Can the input be null - NO 
    # what do we return if the string is empty - return 0
    # can the input be negative - Yes
    # output has to be of type Integer
   
    sign = 1
    output = 0
    for i in range(len(s)):
         # ignore leading whitespaces
        if s[i] == " ": 
            continue
        # check to see if the number is negative or positive
        if s[i] == '-':
            sign = -1
        # check if the input is valid aka a number between 0-9
        if s[i] >= '0' and s[i] <= '9':
            output = (output*10) + (ord(s[i]) - ord('0'))
        return output * sign

'''
def myAtoi(self, s: str) -> int:
        sign = 1
        output = 0
        words = 0
        pos_limit = (2**(31) -1)
        neg_limit = -(2**(31))
        for i in range(len(s)):
            # ignore leading whitespaces
            if s[i] == " ": 
                continue
            # check to see if the number is negative or positive
            if s[i] == '-':
                sign = -1
            # check if the input is valid aka a number between 0-9
            if s[i] >= '0' and s[i] <= '9':
                output = (output*10) + (ord(s[i]) - ord('0'))
            #handling the case where there are words before
            elif s[i] >= 'a' and s[i] <= 'z': 
                words = 1   
            if output == 0 and words ==1:
                return 0
            if output > pos_limit: 
                output = pos_limit
            if output < neg_limit:
                output = neg_limit 
                
        return (output * sign)
'''