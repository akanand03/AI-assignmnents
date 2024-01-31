from collections import deque

# Define initial and goal states
initial_state = (1, 1, 1, 1, 0, 0, 0, 0)
goal_state = (0, 0, 0, 0, 1, 1, 1, 1)

# Define legal actions
actions = [
    (1, 0, 0, 0, -1, 0, 0, 0),  # Farmer alone
    (1, 1, 0, 0, -1, -1, 0, 0),  # Farmer with wolf
    (1, 0, 1, 0, -1, 0, -1, 0),  # Farmer with goat
    (1, 0, 0, 1, -1, 0, 0, -1)   # Farmer with cabbage
]

visited = set()
queue = deque([initial_state])

while queue:
    current_state = queue.popleft()
    visited.add(current_state)

    # Check if goal state is reached
    if current_state == goal_state:
        print("Goal reached")
        break

    # Generate child states
    for action in actions:
        child_state = tuple(current_state[i] + action[i] for i in range(len(current_state)))

        # Check if child state is valid and not visited
        if all(0 <= x <= 1 for x in child_state[:4]) and all(0 <= x <= 1 for x in child_state[4:]) and child_state not in visited:
            queue.append(child_state)
