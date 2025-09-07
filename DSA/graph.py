class Graph:
    def __init__(self, routes : tuple):
        self.routes = routes
        self.graph_dict = {}

        for start, end in self.routes:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path = []):

        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []

        for node in self.graph_dict:
            if node not in path:
                new_path = get_paths(node , end, path)
                for p in new_path:  
                    paths.append(p)

        return paths

if __name__ == '__main__':
    routes = [
        ("mumbai", "Paris"),
        ("mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "Turkey"),
        ("Dubai", "Turkey")
    ]

    Graph = Graph(routes)
    start = "Mumbai"
    end = "Mumbai"
    print(Graph.get_paths(start, end))