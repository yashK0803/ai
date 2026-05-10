import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.adj_list[u].append((weight, v))
        self.adj_list[v].append((weight, u))

    def prim_mst(self, start=0):
        visited = [False] * self.vertices

        min_heap = [(0, start, -1)]

        mst_edges = []
        total_cost = 0

        while min_heap and len(mst_edges) < self.vertices - 1:
            weight, current, parent = heapq.heappop(min_heap)

            if visited[current]:
                continue

            visited[current] = True
            total_cost += weight

            if parent != -1:
                mst_edges.append((parent, current, weight))

            for next_weight, neighbor in self.adj_list[current]:
                if not visited[neighbor]:
                    heapq.heappush(
                        min_heap,
                        (next_weight, neighbor, current)
                    )

        return mst_edges, total_cost


def main():
    vertices = 5

    graph = Graph(vertices)

    edges = [
        (0, 1, 2),
        (0, 3, 6),
        (1, 2, 3),
        (1, 3, 8),
        (1, 4, 5),
        (2, 4, 7),
        (3, 4, 9),
    ]

    for u, v, weight in edges:
        graph.add_edge(u, v, weight)

    mst_edges, total_cost = graph.prim_mst()

    print("Prim's Algorithm for Minimum Spanning Tree")

    print("Edges in the graph:")
    for u, v, weight in edges:
        print(f"{u} -- {v} == {weight}")

    print("\nEdges in the Minimum Spanning Tree:")
    for u, v, weight in mst_edges:
        print(f"{u} -- {v} == {weight}")

    print(f"\nTotal cost of MST: {total_cost}")


if __name__ == "__main__":
    main()