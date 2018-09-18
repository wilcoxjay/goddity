import networkx as nx

import goddity

from typing import Tuple, Sequence, Any

V = Tuple[int, int]
E = Tuple[V, V]

class State(goddity.State[E]):
    def __init__(self, graph: nx.DiGraph[V], src: V, dst: V) -> None:
        self.graph: nx.DiGraph[V] = nx.DiGraph(graph)
        assert src in graph
        assert dst in graph

        self.src = src
        self.dst = dst

        self.visited = {n: float('inf') for n in graph}
        self.visited[src] = 0

    def heuristic(self) -> Sequence[E]:
        return list(self.graph.out_edges(n for n, cost
                                    in self.visited.items()
                                    if cost != float('inf')))

    def render_action(self, edge: E) -> str:
        (u,v) = edge
        return '{} -> {}'.format(u,v)

    def step(self, edge: E) -> None:
        (u,v) = edge
        assert u in self.graph
        self.visited[v] = min(self.visited[v], self.visited[u] + 1)


graph: nx.DiGraph[V] = nx.grid_graph([4,4])
graph.remove_node((2,2))
graph.remove_node((1,2))

state = State(graph, (0,0), (3,3))
print('hello')

if __name__ == '__main__':
    print("HELLOE")
    goddity.run_app(state)
