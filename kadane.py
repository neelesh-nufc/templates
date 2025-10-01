"""
Object: Find the maximum sum of a continuous subarray within 1D array of numbers.

Time complexity: O(n)

Core Idea: Keep track of two main variable:

1. curr_max
2. global_max
"""

def kadanes_algorithm(arr):
    if not arr:
        return 0
    
    #initialize curr_max and global_max with first element
    curr_max = arr[0]
    global_max = arr[0]
 
    for i in range(1, len(arr)): # for num in arr[1:]:
        curr_max = max(arr[i], curr_max + arr[i])
        global_max = max(global_max, curr_max)

    return global_max

if __name__ == "__main__":
    my_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Array: {my_array}")
    print(f"Maximum contiguous sum is: {kadanes_algorithm(my_array)}\n")