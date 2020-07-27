
def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot_position = int(abs(len(arr)/2))
        pivot = arr[pivot_position]
        left_arr = [i for i in arr if i < pivot]
        right_arr = [i for i in arr if i > pivot]
        return qsort(left_arr) + [pivot] + qsort(right_arr)


# input_sample = [10, 5, 8, 1, 20, 100, 32, 874, 6, 1, 2, 2]
# output_sample = qsort(input_sample)

# print('first test')
# print(input_sample)
# print('\n')
# print(output_sample)


input_sample = [10, 5]
output_sample = qsort(input_sample)

print(input_sample)
print('\n')
print(output_sample)
