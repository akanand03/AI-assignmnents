import random
import numpy as np

class GoldExplorer:
    def __init__(self, N, X, charging_location, gold_location):
        self.N = N
        self.X = X
        self.charging_location = charging_location
        self.gold_location = gold_location
        self.visited = set()
        self.current_location = (0, 0)
        self.battery = X
        self.total_rooms_visited = 0
        self.decision_location = None

    def is_valid_move(self, x, y):
        return 0 <= x < self.N and 0 <= y < self.N

    def initialize_environment(self):
        grid = np.zeros((self.N, self.N), dtype=object)
        for x in range(self.N):
            for y in range(self.N):
                neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]  # All potential neighbors
                valid_neighbors = [n for n in neighbors if 0 <= n[0] < self.N and 0 <= n[1] < self.N]
                grid[x, y] = valid_neighbors
        grid[0, 0].append(self.charging_location)  # Add charging station to entry point
        grid[self.gold_location] = "GOLD"  # Mark pot of gold location
        return grid

    def explore_room(self, grid):
        x, y = self.current_location
        self.visited.add((x, y))
        if grid[x, y] == "GOLD":
            return "found", True
        elif self.battery <= 1:
            return "recharge", False
        else:
            unvisited_neighbors = [n for n in grid[x, y] if n not in self.visited]
            if unvisited_neighbors:
                next_room = random.choice(unvisited_neighbors)
            else:
                next_room = random.choice(grid[x, y])
            self.battery -= 1
            return next_room, False

    def find_pot_of_gold(self):
        grid = self.initialize_environment()
        found_gold = False

        while not found_gold:
            next_action, found_gold = self.explore_room(grid)
            if next_action == "move":
                self.current_location = next_action
            elif next_action == "recharge":
                self.charge()

        return self.total_rooms_visited, self.decision_location

    def charge(self):
        print(f"Charging at room: {self.charging_location}")
        self.battery = self.X
        self.decision_location = self.current_location

    def start(self):
        print("Starting the exploration.")
        self.find_pot_of_gold()
        print(f"Total rooms visited: {self.total_rooms_visited}")
        if self.decision_location:
            print(f"Charging decision made at room: {self.decision_location}")


# Example usage:
N = 5
X = 15
charging_location = (2, 2)
gold_location = (4, 3)

gold_explorer = GoldExplorer(N, X, charging_location, gold_location)
gold_explorer.start()
