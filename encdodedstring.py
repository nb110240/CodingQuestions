def getDecodedString(encoded):
    '''
    # Write your code here
    out = ''
    num = 0
    st = ''
    i =0
    while i <= len(encoded) -1:
        if(encoded[i] > '0' and encoded[i] < '9'):
            num = int(encoded[i])
        elif encoded[i] == '[':
            while encoded[i+1] != ']':
                if(encoded[i] > '0' and encoded[i] < '9'):
                    continue
                i += 1
                st = st + (encoded[i])
            i +=1        
        else:
            out = out + (encoded[i])
        i +=1
    if st != '':
        for i in range(int(num)):
            out = out + (st)  
    return out 
    '''
    def getrep(stack):
        count = ""
        repstr = ""
        # Get string part
        while len(stack)>0 and stack[-1] != "[":
            repstr = stack.pop() + repstr
        if len(stack) > 0 and stack[-1] == "[":
            stack.pop()
        
        # Get number part
        while stack and not stack[-1].isalpha() and stack[-1]!="[":
            count = stack.pop() + count
        return int(count), repstr

    stack = []
    for c in encoded:
        if c=="]":
            count, repstr = getrep(stack)
            stack.append(repstr*count)
        else:
            stack.append(c)
    return "".join(stack)