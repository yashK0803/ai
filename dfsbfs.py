from collections import deque

class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.adj_list = {i: [] for i in range(vertices)}

    def add_edge(self, source: int, destination: int) -> None:
        self.adj_list[source].append(destination)

    def dfs(self, start: int) -> list[int]:
        visited = [False] * self.vertices
        traversal = []

        def dfs_recursive(vertex: int) -> None:
            visited[vertex] = True
            traversal.append(vertex)

            for neighbour in self.adj_list[vertex]:
                if not visited[neighbour]:
                    dfs_recursive(neighbour)

        dfs_recursive(start)
        return traversal

    def bfs(self, start: int) -> list[int]:
        visited = [False] * self.vertices
        traversal = []

        queue = deque([start])
        visited[start] = True

        def bfs_recursive() -> None:
            if not queue:
                return

            vertex = queue.popleft()
            traversal.append(vertex)

            for neighbour in self.adj_list[vertex]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)

            bfs_recursive()

        bfs_recursive()
        return traversal


def main() -> None:
    n = 4
    e = 6

    graph = Graph(n)

    edges = [
        (0, 1),
        (0, 2),
        (1, 2),
        (2, 0),
        (2, 3),
        (3, 3),
    ]

    for source, destination in edges:
        graph.add_edge(source, destination)

    print("Graph: no of nodes, no of edges")
    print(f"n = {n}, e = {e}")

    print("\nEnter adjacent node information")

    for source, destination in edges:
        print(f"{source} -> {destination}")

    dfs_result = graph.dfs(2)
    bfs_result = graph.bfs(2)

    print("\nOutput:")
    print("DFS from vertex 2 -", ", ".join(map(str, dfs_result)))
    print("BFS from vertex 2 -", ", ".join(map(str, bfs_result)))


if __name__ == "__main__":
    main()