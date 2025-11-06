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