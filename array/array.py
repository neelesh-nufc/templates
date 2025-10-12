from collections import Counter

def solve_with_hashing(arr):
    # 1. Use a dictionary to store counts or seen elements
    # Example 1: Count frequencies
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1
    # Or more concisely:
    # counts = Counter(arr)

    # Example 2: Store seen elements for quick lookup
    seen = set() # Use a set for just presence, dict for key-value
    for x in arr:
        if x in seen:
            # Duplicate found!
            pass
        seen.add(x)

    # 2. Iterate through the array (often multiple times)
    # for i in range(len(arr)):
    #     # Do something with arr[i]

    # 3. Two-pointer approach (often for sorted arrays, but can apply to some unsorted)
    # left, right = 0, len(arr) - 1
    # while left < right:
    #     # Compare arr[left] and arr[right]
    #     if arr[left] + arr[right] == target:
    #         # Found a pair
    #         pass
    #     elif arr[left] + arr[right] < target:
    #         left += 1
    #     else:
    #         right -= 1

    # 4. Sliding Window (for subarrays/subsequences)
    # window_start = 0
    # for window_end in range(len(arr)):
    #     # Add arr[window_end] to window
    #     # While window condition is violated (e.g., sum > K, too many distinct chars):
    #     #   Remove arr[window_start] from window
    #     #   window_start += 1
    #     # Update result (e.g., max_length = max(max_length, window_end - window_start + 1))

    return # result