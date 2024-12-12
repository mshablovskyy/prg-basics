def ff(matrix):
    elements = []
    rows = len(matrix)
    colums = len(matrix[0])
    new_matrix = []
    for row in matrix:
        for item in row:
            elements.append(item)
    y = 0
    for i in range(colums):
        new_matrix.append([])
    for r in range(rows):
        for c in range(colums):
            new_matrix[c].append(elements[y])
            y +=1
            
    
    return new_matrix

def xf(matrix):
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            print(matrix[j][i], end=" ")
        print()
        
def yf(matrix):
    for row in ff(matrix):
        for i in row:
            print(i, end=" ")
        print()
        
def f(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        new_matrix.append([])
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            new_matrix[i].append(matrix[j][i])
    return new_matrix
        
        
            
        
            
            
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9],
          [10,11,12]]
tm = f(matrix)
print(tm)
for r in tm:
        print(r)
