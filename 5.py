import heapq

def knapsack_a_star(profits, weights, capacity):
    n = len(profits)
    solution_vector = [-1] * n
    current_index = 0
    current_weight = 0
    current_profit = 0
    current_best_profit = float('-inf')
    current_best_solution = [0] * n

    def fractional_knapsack(remaining_capacity, items):
        total_profit = 0
        for i in range(len(items)):
            if remaining_capacity <= 0:x
                break
            if items[i][1] <= remaining_capacity:
                total_profit += items[i][0]
                remaining_capacity -= items[i][1]
            else:
                fraction = remaining_capacity / items[i][1]
                total_profit += items[i][0] * fraction
                break
        return total_profit

    def recursive_search(current_index, current_weight, current_profit, solution_vector):
        nonlocal current_best_profit, current_best_solution

        if current_index == n:
            if current_weight <= capacity and current_profit > current_best_profit:
                current_best_profit = current_profit
                current_best_solution = solution_vector.copy()
            return

        # Don't take the item
        solution_vector[current_index] = 0
        recursive_search(current_index + 1, current_weight, current_profit, solution_vector)

        # Take the item
        if current_weight + weights[current_index] <= capacity:
            solution_vector[current_index] = 1
            recursive_search(current_index + 1,
                             current_weight + weights[current_index],
                             current_profit + profits[current_index],
                             solution_vector)

    recursive_search(current_index, current_weight, current_profit, solution_vector)
    return current_best_solution, current_best_profit

# Example usage:
profits = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
solution, profit = knapsack_a_star(profits, weights, capacity)
print("Solution vector:", solution)
print("Max profit:", profit)
