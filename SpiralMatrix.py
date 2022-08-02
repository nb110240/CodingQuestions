def spiralOrder(self, matrix: List[List[int]]) -> List[int]: 
        output = []
        left = 0 
        top = 0
        right = len(matrix[0])
        bottom = len(matrix)
        
        while left< right and top < bottom:
            for i in range(left,right):
                output.append(matrix[top][i])
            top += 1
            for i in range(top,bottom):
                output.append(matrix[i][right-1])
            right -= 1
            if not (left < right and top < bottom): 
                break 
            for i in range(right-1, left -1, -1):
                output.append(matrix[bottom -1][i])
            bottom -= 1
            for i in range (bottom -1, top -1, -1):
                output.append(matrix[i][left])
            left +=1 
        return output
        '''
        ---> 
        1 2 3 4
        5 6 7 8
        9 10 11 12
        13 14 15 16 
        <--- 
        
        1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
        '''
        