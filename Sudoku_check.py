correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sudoku(matrix):
    number = [1,2,3,4,5,6,7,8,9]
    n = len(matrix)
    for e in matrix:
        i=0
        while i < n:
            count1 = [0,0,0,0,0,0,0,0,0]
            count2 = [0,0,0,0,0,0,0,0,0]
            j=0
            while j < n:
                p = matrix[i][j]
                if p not in number[:n]:
                    return False
                count1[matrix[i][j]] = count1[matrix[i][j]] + 1
                if count1[matrix[i][j]] > 1:
                    return False
                count2[matrix[j][i]] = count2[matrix[j][i]] + 1
                if count2[matrix[j][i]] > 1:
                    return False
                j += 1
            i += 1
    return True
    
    
#print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False


