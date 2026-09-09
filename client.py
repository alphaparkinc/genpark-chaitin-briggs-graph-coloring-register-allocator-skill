class ChaitinBriggsRegisterAllocator:
    """Chaitin-Briggs Graph Coloring Register Allocator."""
    def __init__(self, k_registers):
        self.k = k_registers
        self.adj = {}
        self.nodes = set()

    def add_interference(self, u, v):
        self.nodes.add(u)
        self.nodes.add(v)
        if u not in self.adj: self.adj[u] = set()
        if v not in self.adj: self.adj[v] = set()
        if u != v:
            self.adj[u].add(v)
            self.adj[v].add(u)

    def allocate(self):
        graph = {u: set(neighbors) for u, neighbors in self.adj.items()}
        for n in self.nodes:
            if n not in graph:
                graph[n] = set()

        stack = []
        spilled = set()

        while graph:
            low_degree = [n for n, neighbors in graph.items() if len(neighbors) < self.k]
            if low_degree:
                node = low_degree[0]
                stack.append(node)
                for neighbor in graph[node]:
                    graph[neighbor].remove(node)
                del graph[node]
            else:
                spill_candidate = max(graph.keys(), key=lambda n: len(graph[n]))
                stack.append(spill_candidate)
                for neighbor in graph[spill_candidate]:
                    graph[neighbor].remove(spill_candidate)
                del graph[spill_candidate]

        coloring = {}
        while stack:
            node = stack.pop()
            neighbor_colors = {coloring[neighbor] for neighbor in self.adj.get(node, set()) if neighbor in coloring}
            chosen_color = None
            for c in range(self.k):
                if c not in neighbor_colors:
                    chosen_color = c
                    break
            if chosen_color is not None:
                coloring[node] = chosen_color
            else:
                spilled.add(node)

        return {
            'success': len(spilled) == 0,
            'k': self.k,
            'coloring': coloring,
            'spilled': list(spilled)
        }
