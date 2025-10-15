"""
Backtracking is an algorithm technique for solving problems by trying to build a solution incrementally.
Whenever a partial solution cannot be completed into a valid solution, the algorithm "backtracks" to previous state
by undoing the last step and trying a different path.

It is used for a problem where you need to find all possible solutions.

Explore: Try to extend the current partial solution
Check: if the current partial solution is valid.
Backtrack: undo the last step and try a different path.
"""

def perumutation(nums):
    result = []

    def backtrack(curr_permutation, remaining_nums):
        # Base Case: If the current permutation is complete, add it to results
        if not remaining_nums:
            result.append(curr_permutation[:])
            return 
        
        for i in range(len(remaining_nums)):
            # Choose: Pick a number
            num = remaining_nums[i]
            curr_permutation.append(num)

            # Explore: Recursively call with the chosen number removed 
            backtrack(curr_permutation, remaining_nums[:i] + remaining_nums[i+1:])

            # Unchoose (Backtrack): Remove the number to try other options
            curr_permutation.pop()

    backtrack([], nums)
    return result

if __name__ == "__main__":
    my_list = [1, 2, 3]
    print(f"List: {my_list}")
    print(f"Permutations: {perumutation(my_list)}\n")
    
                          