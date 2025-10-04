"""
A prefix sum array (or cumulative sum array) for a given array arr is an array prefix_sum 
where prefix_sum[i] stores the sum of all elements from arr[0] to arr[i].

The real power of prefix sums comes when you need to find the sum of a subarray arr[i...j] (inclusive).

sum(i...j) = prefix_sum[j] - prefix_sum[i-1]

"""

def create_prefix_sum(arr):
    if not arr:
        return []
    
    prefix_sum = [0] * (len(arr))
    prefix_sum[0] = arr[0]

    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

    return prefix_sum

def get_subarray_sum(prefix_sum, start_idx, end_idx):
    if start_idx < 0 or end_idx >= len(prefix_sum):
        return 0
    
    return prefix_sum[end_idx] - prefix_sum[start_idx-1]

if __name__ == "__main__":
    my_array = [1, 2, 3, 4, 5]
    prefix_sum_array = create_prefix_sum(my_array)
    print(f"Array: {my_array}")
    print(f"Prefix sum array: {prefix_sum_array}")
    print(f"Sum of subarray from index 1 to 3: {get_subarray_sum(prefix_sum_array, 1, 3)}\n")
    

