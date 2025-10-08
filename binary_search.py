"""
Binary search is an efficient technique to find the target in sorted array.

Finding the First/Last Occurrence: If there are duplicate elements, 
you might need to adjust the while loop condition and how you update left/right to ensure you find the very first or very last instance of the target.

Finding the Smallest/Largest Element Greater/Smaller Than Target: 
This often involves slightly different left/right updates and a final check after the while loop terminates.

Search Space Definition: The left <= right template typically uses an inclusive [left, right] range. 

Sometimes, you might see left < right with an exclusive [left, right) range, 
which changes the mid calculation and left/right updates. Stick with one consistent approach.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Element not found

if __name__ == "__main__":
    my_list = [2, 4, 6, 8, 10, 12, 14]
    target = 10
    print(f"List: {my_list}")
    print(f"Target: {target}")
    print(f"Index of {target}: {binary_search(my_list, target)}\n")