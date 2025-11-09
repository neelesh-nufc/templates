def solve_activity_selection(intervals):
    # 1. Sort by finish times (the core greedy choice)
    #    If finish times are equal, sorting by start times can be a tie-breaker,
    #    but often not strictly necessary for correctness of this specific greedy.
    intervals.sort(key=lambda x: x[1])

    count = 0
    last_finish_time = float('-inf') # Or intervals[0][1] if intervals is guaranteed non-empty

    for start, end in intervals:
        # 2. Make a greedy choice: If the current interval's start time
        #    is after or equal to the last chosen interval's finish time,
        #    then it doesn't overlap.
        if start >= last_finish_time:
            count += 1
            last_finish_time = end # Update the finish time of the last selected activity

    return count


############################################################################################
# Example Usage:
# intervals = [[1, 3], [2, 4], [3, 5], [0, 6]]
# print(solve_activity_selection(intervals)) # Output: 2 (e.g., [1,3], [3,5])

# LeetCode 435 Specific (return number of intervals to remove):
def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1]) # Sort by end times

    end = intervals[0][1]
    count = 1 # Number of non-overlapping intervals

    for i in range(1, len(intervals)):
        if intervals[i][0] >= end: # If current interval starts after or at the end of the last non-overlapping interval
            count += 1
            end = intervals[i][1] # Update the end time

    return len(intervals) - count # Total intervals - non-overlapping intervals