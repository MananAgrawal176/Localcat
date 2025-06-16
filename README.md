# Localcat
For uploading assignment for LS

Q1

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


# Q2
    import numpy as np


    arr = np.array([0.03871,9.93639,9.6247,8.2241,7.3135,6.3351,4.5135,5.976,3.25671,2.3672,1.777,2.4232,5.62442,7.82453,9.624231,3.5323,4.92314,6.4890,2.95678,8.87697])

# Part 1
    rounded_arr = np.round(arr, 2)
    print(rounded_arr)

# Part 2: 

    print( np.min(rounded_arr))
    print( np.max(rounded_arr))
    print( np.median(rounded_arr).round(2))

# Part 3
    modified_arr = np.array([x**2 if x < 5 else x for x in rounded_arr])

    print(modified_arr.round(2))

# Part 4
    def numpy_alternate_sort(array):
    sorted_array = np.sort(array)
    result = []

    left = 0
    right = len(sorted_array) - 1

    while left <= right:
        result.append(sorted_array[left])
        left += 1
        if left <= right:
            result.append(sorted_array[right])
            right -= 1

    return np.array(result)


    alt_sorted_arr = numpy_alternate_sort(arr)
    print (alt_sorted_arr.round(2))
   
