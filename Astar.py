import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f


def manhattan_distance(state, goal_positions):
    distance = 0

    for i in range(3):
        for j in range(3):
            value = state[i][j]

            if value != 0:
                goal_i, goal_j = goal_positions[value]
                distance += abs(i - goal_i) + abs(j - goal_j)

    return distance


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

    return -1, -1


def generate_neighbors(state):
    neighbors = []

    x, y = find_blank(state)

    directions = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right"),
    ]

    for dx, dy, move in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]

            new_state[x][y], new_state[nx][ny] = (
                new_state[nx][ny],
                new_state[x][y],
            )

            neighbors.append((tuple(tuple(row) for row in new_state), move))

    return neighbors


def reconstruct_path(node):
    path = []

    while node is not None:
        path.append((node.move, node.state))
        node = node.parent

    return list(reversed(path))


def a_star(start_state, goal_state):
    goal_positions = {}

    for i in range(3):
        for j in range(3):
            if goal_state[i][j] != 0:
                goal_positions[goal_state[i][j]] = (i, j)

    open_list = []

    start_node = PuzzleNode(
        start_state,
        None,
        "Start",
        0,
        manhattan_distance(start_state, goal_positions),
    )

    heapq.heappush(open_list, start_node)

    best_cost = {start_state: 0}

    while open_list:
        current = heapq.heappop(open_list)

        if current.state == goal_state:
            return reconstruct_path(current)

        for neighbor_state, move in generate_neighbors(current.state):
            new_g = current.g + 1

            if (
                neighbor_state not in best_cost
                or new_g < best_cost[neighbor_state]
            ):
                best_cost[neighbor_state] = new_g

                new_h = manhattan_distance(
                    neighbor_state,
                    goal_positions,
                )

                neighbor_node = PuzzleNode(
                    neighbor_state,
                    current,
                    move,
                    new_g,
                    new_h,
                )

                heapq.heappush(open_list, neighbor_node)

    return None


def print_state(state):
    for row in state:
        print(" ".join("_" if value == 0 else str(value) for value in row))


def main():
    start_state = (
        (1, 2, 3),
        (0, 4, 6),
        (7, 5, 8),
    )

    goal_state = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 0),
    )

    print("Input:")
    print("Start State:")
    print_state(start_state)

    print("Goal State:")
    print_state(goal_state)

    solution_path = a_star(start_state, goal_state)

    if solution_path is None:
        print("\nNo solution found.")
        return

    print("\nSolution Path:")

    for step, (move, state) in enumerate(solution_path):
        print(f"Step {step} ({move}):")
        print_state(state)
        print()

    print(f"Total moves required: {len(solution_path) - 1}")


if __name__ == "__main__":
    main()