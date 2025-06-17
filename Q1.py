import numpy as np

    random = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16],
                   [17, 18, 19, 20]])
# Part 1
    for i in range(random.shape[0]):
         print(random[i, 3 - i])

# Part 2
    for i in range(random.shape[0]):
    print(np.max(random[i]))

# Part 3
    b = random.flatten()
    a = []
    for i in range(random.size):
    if b[i] <= np.mean(b):
        a.append(b[i])
    print(a)

    a = np.array([num for num in b if num <= np.mean(b)])
    print(a)

# Part 4

     

    def numpy_boundary_traversal(matrix):
  

    rows, cols = matrix.shape
    result = []

   
    if rows == 1:
        result.extend(matrix[0])
    
    elif cols == 1:
        result.extend(matrix[:, 0])
    else:
       
        result.extend(matrix[0, :])

        result.extend(matrix[1:rows-1, -1])

        result.extend(matrix[-1, ::-1])

  
        result.extend(matrix[rows-2:0:-1, 0])

    return result
    
    print(numpy_boundary_traversal(random))
