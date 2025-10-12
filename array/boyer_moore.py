"""
Boyer Moore is the algorithm to find the majority element in an array that have N/2 occurence
"""

def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        # count += (1 if num == candidate else -1)
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

if __name__ == "__main__":
    my_list = [2, 2, 1, 1, 1, 2, 2]
    print(f"List: {my_list}")
    print(f"Majority element: {majority_element(my_list)}\n")