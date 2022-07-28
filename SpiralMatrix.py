def spiralOrder(self, matrix: List[List[int]]) -> List[int]: 
        output = []
        #keeping track of elements that have been appended. 
        
        
    
        # we could first append the first row of the matrix
        # increase the column by 1 
        for j in range(len(matrix)):
            output.append(matrix[0][j])
        # the we traverse down the last column 
        for i in range(1,len(matrix[0])):
            output.append(matrix[i][j])
        #left the last row 
        while j < 0:
            j -= 1
            output.append(matrix[i][j])
            
        # second iteration you go up one less position 
        
        
        '''
        ---> 
        1 2 3 4
        5 6 7 8
        9 10 11 12
        13 14 15 16 
        <--- 
        
        1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
        '''
        