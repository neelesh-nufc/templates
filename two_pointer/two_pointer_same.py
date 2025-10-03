"""
Two pointers used to solve problem in sorted list, It involves left or right that itirate through the data based on certain
rules or condition.

When to use:
    - The input list is sorted.
    - You need to find a pair, triplet or subarray based on certain condition.
    - You need to process elements from both side to middle.

This the template foe two pointer same direction or fast/slow pointer:

Common usecase: Removing duplicates (in-place) from a sorted array, finding the middle of a linked list, 
detecting cycles in a linked list, finding the nth node from the end of a linked list. 
(While often applied to linked lists, it has array applications too).
"""
def remove_duplicates_sorted_array(nums):
    if not nums:
        return 0
    
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1

if __name__ == "__main__":
    my_list = [1, 1, 2, 2, 2, 3, 4, 4, 5]
    print(f"List: {my_list}")
    print(f"Length after removing duplicates: {my_list[:remove_duplicates_sorted_array(my_list)]}\n")
