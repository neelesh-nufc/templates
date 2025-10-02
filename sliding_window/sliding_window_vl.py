"""
Objective: Unlike the fixed window size where k is constant, here the window's size can grow or shrink dynamically based on
certain condition.

Ask:
- Find smallest/largest subarray/substring that satisfies a given condition 
-  Find a subarray with max/min number of distinct character/ elements within certain constraint

Core Idea:
Expand window right point -> check condition -> shrink left pointer -> update result -> repeat 
"""

def smallest_subarray_with_given_sum(s, arr):
    if not arr:
        return 0
    
    window_sum = 0 
    min_length = float('inf')
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    return min_length if min_length != float('inf') else 0


if __name__ == "__main__":
    my_array = [2, 1, 5, 2, 3, 2]
    s = 7
    print(f"Array: {my_array}")
    print(f"Smallest subarray with sum greater than or equal to {s} is: {smallest_subarray_with_given_sum(s, my_array)}\n") 