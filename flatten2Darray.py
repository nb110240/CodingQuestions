def flattenArray(array):
    if array is None:
        return []
    n = len(array)
    m= len(array[0])
    flat = [0] * (n*m)
    for i in range(n):
        for j in range(m):
            flat[i * m+ j] = array[i][j]
    return flat




     
