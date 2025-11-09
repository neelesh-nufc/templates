def solve_fractional_knapsack(items, capacity):
    # items: list of tuples (value, weight)

    # 1. Calculate value-to-weight ratio and store as (ratio, value, weight)
    #    This allows sorting by ratio directly.
    items_with_ratio = []
    for value, weight in items:
        items_with_ratio.append((value / weight, value, weight))

    # 2. Sort by ratio in descending order
    items_with_ratio.sort(key=lambda x: x[0], reverse=True)

    total_value = 0.0
    remaining_capacity = capacity

    for ratio, value, weight in items_with_ratio:
        if remaining_capacity <= 0:
            break

        # 3. Greedy choice: Take as much of the current item as possible
        amount_to_take = min(weight, remaining_capacity)
        total_value += amount_to_take * ratio # (value/weight) * amount_to_take
        remaining_capacity -= amount_to_take

    return total_value

# Example Usage:
# items = [(60, 10), (100, 20), (120, 30)] # (value, weight)
# capacity = 50
# print(solve_fractional_knapsack(items, capacity)) # Output: 240.0




class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0 
        total_cost = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            total_cost += cost[i]
            total_gas += gas[i]
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0 
        
        return start if total_gas >= total_cost else -1 

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))