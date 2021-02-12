A = [3, 8, 9, 7, 6]
K = 3

array_len = len(A)
# check if array is empty (no movement)
if array_len == 0:
    print(A)
else:
    # evaluate when K=0 or K is divisible by array_len (no movement)
    if K==0 or K%array_len == 0:
        print(A)
    else:
        # compute for the number of shifts
        no_of_shifts = K % array_len
    
        # define the output array; set the number of elements = to the given array
        resulting_array = [0] * array_len

        # shift the elements based on the computed number of shifts
        for i in range(array_len):
            if i + no_of_shifts >= array_len:
                # subtract the array length from the index reference when it reaches the array length
                resulting_array[i + no_of_shifts - array_len] = A[i]
            else:
                resulting_array[i + no_of_shifts] = A[i]
        
        print(resulting_array)