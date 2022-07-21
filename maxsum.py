def getMaxSum(arr, k):
    # Write your code here
    if k > len(arr):
        return -1
    if k == len(arr):
        return sum(arr)
    left = 0
    right = 0
    maxsum = 0
    while right <= len(arr): 
        right = left +k
        subarr = arr[left:right]
        if sum(subarr) >= maxsum:
            maxsum = sum(subarr)
        left += 1
    return maxsum 