# Given sorted array, remove all duplicates and return length of new array

input_Arr = [2, 3, 3, 3, 6, 9]

def remove_dups(input_Arr):
    next_non_dup, i = 0, 0
    while(i < len(input_Arr)-1):
        if input_Arr[next_non_dup] != input_Arr[i+1]:
            input_Arr[next_non_dup] = input_Arr[i]
            next_non_dup+=1
        i+=1
    return input_Arr, next_non_dup+1

print(remove_dups(input_Arr))