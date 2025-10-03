"""
Two pointers used to solve problem in sorted list, It involves left or right that itirate through the data based on certain
rules or condition.

When to use:
    - The input list is sorted.
    - You need to find a pair, triplet or subarray based on certain condition.
    - You need to process elements from both side to middle.

This the template foe two pointer opps direction:
Common usecase: Finding pairs with a specific sum, finding palindromes, 
reversing an array/string in-place, removing duplicates in a sorted array.
"""

def two_pointer_sorted(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []  # No pair found

if __name__ == "__main__":
    my_list = [1, 3, 6, 8, 11, 15]
    target = 9
    print(f"List: {my_list}")
    print(f"Target: {target}")
    print(f"Pair indices: {two_pointer_sorted(my_list, target)}\n")