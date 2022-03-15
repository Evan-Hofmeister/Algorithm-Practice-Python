# Given sorted array - create sorted array of squares
# The implementation of this problem would look very different for an unsorted array

def square_sort(input_Arr):
    dim = len(input_Arr)
    square = [0] * dim
    left, right = 0, dim-1
    dim_index = dim-1

    while left <= right:
        # Note this is the fastest and most efficient method of squaring an array element
        leftSquare = input_Arr[left] * input_Arr[left]
        rightSquare = input_Arr[right] * input_Arr[right]

        if leftSquare > rightSquare:
            square[dim_index] = leftSquare
            left+=1
        else:
            square[dim_index] = rightSquare
            right-=1
        dim_index-=1
    return square



input_Arr = [-2, -1, 0, 2, 3]
print(square_sort(input_Arr))


