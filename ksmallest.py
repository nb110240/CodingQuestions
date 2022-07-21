def Ksmallest(array,k):
    if k > len(array) or k<0:
        return -1
    newarr = []
    for i in range(k):
        smallest = min(array)
        newarr.append(smallest)
    return newarr[-1]

    '''
        arr = sorted(nums)
        return arr[k-1]
        
    '''



    
    