# Q2
import numpy as np


arr = np.array([0.03871,9.93639,9.6247,8.2241,7.3135,6.3351,4.5135,5.976,3.25671,2.3672,1.777,2.4232,5.62442,7.82453,9.624231,3.5323,4.92314,6.4890,2.95678,8.87697])

# Part 1
rounded_arr = np.round(arr, 2)
print(rounded_arr)

print("="*100)

# Part 2: 

print( np.min(rounded_arr))
print( np.max(rounded_arr))
print( np.median(rounded_arr).round(2))

print("="*100)

# Part 3
modified_arr = np.array([x**2 if x < 5 else x for x in rounded_arr])

print(modified_arr.round(2))

print("="*100)

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
