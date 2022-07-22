def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    ss = []
    list1 = []
    j,k =0,0
    output = []
    for i in range(len(matrix)):
        x = matrix[i]
        for i in range(len(x)):
            list1.append(x[i])
    while k < len(matrix[0]):
        while j < len(list1):
            ss.append(list1[j])
            j += len(matrix[0])
        output.append(ss)
        ss,j = [],0
        k +=1
        j  = k
    return output