"""
A postfix sum array (or suffix sum array) for a given array arr is an array postfix_sum 
where postfix_sum[i] stores the sum of all elements from arr[i] to arr[len(arr)-1].

Let arr = [2, 1, 5, 3, 4]

    postfix_sum[4] = arr[4] = 4

    postfix_sum[3] = arr[3] + postfix_sum[4] = 3 + 4 = 7

    postfix_sum[2] = arr[2] + postfix_sum[3] = 5 + 7 = 12

    postfix_sum[1] = arr[1] + postfix_sum[2] = 1 + 12 = 13

    postfix_sum[0] = arr[0] + postfix_sum[1] = 2 + 13 = 15

So, postfix_sum = [15, 13, 12, 7, 4]

sum(arr[i...j]) = postfix_sum[i] - postfix_sum[j+1]
"""

def create_postfix_sum(arr):
    if not arr:
        return []
    
    n = len(arr)
    postfix_sum = [0] * len(arr)
    postfix_sum[-1] =arr[-1]

    for i in range(n-2, -1, -1):
        postfix_sum[i] = arr[i] + postfix_sum[i+1]
    
    return postfix_sum 

def get_subarray_sum(postfix_sum, start_idx, end_idx):
    if start_idx < 0 or end_idx >= len(postfix_sum):
        return 0
    
    if end_idx == len(postfix_sum) - 1:
        return postfix_sum[start_idx]
    
    return postfix_sum[start_idx] - postfix_sum[end_idx+1]

if __name__ == "__main__":
    my_array = [2, 1, 5, 3, 4]
    postfix_sum_array = create_postfix_sum(my_array)
    print(f"Array: {my_array}")
    print(f"Postfix sum array: {postfix_sum_array}")
    print(f"Sum of subarray from index 1 to 3: {get_subarray_sum(postfix_sum_array, 1, 3)}\n")