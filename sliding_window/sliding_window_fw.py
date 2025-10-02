"""
Objective: Efficiently process a contiguous subarray or substring of a fixed and variable length.
When the problem specifies 'fixed length', it mean we are looking a subarray or substring of a constant length
- Find max/min sum( or product, avg, etc) of subarray or substring with specific length
- Count occurences of a specific pattern (of length k)


Core Idea: Imagine a window of specific size that 'slides' over your array.
"""

def max_subarray_sum_fixed_window(arr, k):
    if not arr or len(arr) < k or k <= 0:
        return 0
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    window_start = 0

    for window_end in range(k, len(arr)):
        window_sum += arr[window_end] - arr[window_start]
        max_sum = max(max_sum, window_sum)
        window_start += 1

    return max_sum

if __name__ == "__main__":
    my_array = [2, 1, 5, 1, 3, 2]
    k = 3
    print(f"Array: {my_array}")
    print(f"Maximum sum of a subarray of size {k} is: {max_subarray_sum_fixed_window(my_array, k)}\n")
    

