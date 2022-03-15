# Given positive array and value k, find max sum of contiguius subarray of size k
Input = [1,2,1,4,3,2,1,6,1]

# Brute force solution - checking sum of all subarrays (O(N*K) time complexity)
def max_subarray_size_k(k, input_Arr):
    max_sum = 0
    subset_sum = 0

    for i in range(len(input_Arr)-k+1):
        subset_sum = 0
        for j in range(i,i+k):
            subset_sum += input_Arr[j]
        max_sum = max(max_sum, subset_sum)
    return max_sum

print(max_subarray_size_k(3, Input))

# We can improve on the brute force method by implementing a sliding window method.
# This reduces time complexity since we are not repeatedly summing over the same values

def max_subarray_size_k_window(k, input_Arr):
    max_sum, win_sum, win_start = 0, 0, 0

    for win_end in range(len(input_Arr)):
        win_sum += input_Arr[win_end]

        if win_end >= k-1:
            max_sum = max(max_sum, win_sum)
            win_sum -= input_Arr[win_start]
            win_start += 1
    return(max_sum)

print(max_subarray_size_k_window(3, Input))
