
def convertToBinary(num):
    # Write your code here
    out = ''
    x =0
    while num > 0:
        x= num %2
        out = out + str(x) 
        num = num //2
    out = out[::-1]
    return out