def kadanes_algorithm(arr):
    """
    Implementation of Kadane's Algorithm to find the maximum sum of a contiguous subarray.

    This algorithm efficiently finds the maximum sum in O(n) time complexity
    and O(1) space complexity.

    Args:
        arr: A list of integers. Can contain positive, negative, and zero values.

    Returns:
        The maximum sum of a contiguous subarray.
        Returns 0 if the input array is empty.
        If all numbers are negative, it returns the largest (least negative) number.
    """
    # Handle the edge case of an empty array.
    if not arr:
        return 0

    # Initialize max_so_far to track the maximum sum found anywhere in the array.
    # Initialize current_max to track the maximum sum of the subarray ending at the current position.
    # Start with the first element of the array.
    max_so_far = arr[0]
    current_max = arr[0]

    # Iterate through the array starting from the second element.
    for num in arr[1:]:
        # For each element, we have two choices:
        # 1. Extend the previous subarray by adding the current number.
        # 2. Start a new subarray from the current number.
        # We choose the one that gives a larger sum.
        current_max = max(num, current_max + num)

        # Update the overall maximum sum if the current subarray's sum is greater.
        max_so_far = max(max_so_far, current_max)

    return max_so_far

# --- Example Usage ---
if __name__ == "__main__":
    # Example 1: Mixed positive and negative numbers
    my_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Array: {my_array}")
    # The contiguous subarray with the largest sum is [4, -1, 2, 1], which sums to 6.
    print(f"Maximum contiguous sum is: {kadanes_algorithm(my_array)}\n")

    # Example 2: All negative numbers
    my_array_neg = [-5, -1, -3, -2]
    print(f"Array: {my_array_neg}")
    # The "maximum" sum is the largest (least negative) number itself.
    print(f"Maximum contiguous sum is: {kadanes_algorithm(my_array_neg)}\n")