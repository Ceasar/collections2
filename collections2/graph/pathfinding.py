

def _tree_search(choose_path, graph, start, goal):
    visited = set()
    paths = set([(start,)])
    while True:
        if len(paths) == 0:
            raise ValueError("goal is unreachable")
        else:
            path = choose_path(paths)
            paths.remove(path)
            end = path[-1]
            if end == goal:
                return path
            else:
                visited.add(end)
                for k in graph[end]:
                    if k not in visited:
                        paths.add(path + (k,))


def bfs(graph, start, goal):
    '''Perform a breadth-first search to the goal.

    >>> graph = {'a': {'w': 14, 'x': 7, 'y': 9}, \
            'b': {'w': 9, 'z': 6}, \
            'w': {'a': 14, 'b': 9, 'y': 2}, \
            'x': {'a': 7, 'y': 10, 'z': 15}, \
            'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11}, \
            'z': {'b': 6, 'x': 15, 'y': 11}}
    >>> bfs(graph, 'a', 'b')
    ('a', 'w', 'b')
    '''
    def choose_path(paths):
        return min(paths, key=len)
    return _tree_search(choose_path, graph, start, goal)


def dfs(graph, start, goal):
    '''Perform a depth-first search to the goal.

    >>> graph = {'a': {'w': 14, 'x': 7, 'y': 9}, \
            'b': {'w': 9, 'z': 6}, \
            'w': {'a': 14, 'b': 9, 'y': 2}, \
            'x': {'a': 7, 'y': 10, 'z': 15}, \
            'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11}, \
            'z': {'b': 6, 'x': 15, 'y': 11}}
    >>> path = dfs(graph, 'a', 'b')
    >>> assert path[0] == 'a'
    >>> assert path[-1] == 'b'
    '''
    def choose_path(paths):
        return list(paths)[0]
    return _tree_search(choose_path, graph, start, goal)


def dijkstra(graph, start, goal, heuristic=lambda x, y: 0):
    '''
    Find the shortest path from start to goal.

    >>> graph = {'a': {'w': 14, 'x': 7, 'y': 9}, \
            'b': {'w': 9, 'z': 6}, \
            'w': {'a': 14, 'b': 9, 'y': 2}, \
            'x': {'a': 7, 'y': 10, 'z': 15}, \
            'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11}, \
            'z': {'b': 6, 'x': 15, 'y': 11}}
    >>> dijkstra(graph,'a','b')
    ('a', 'y', 'w', 'b')

    By supplying a heuristic, you can transform the algorithm into the
    a* search algorithm.
    '''
    def path_cost(path):
        cost = sum(graph[u][v] for u, v in zip(path, path[1:]))
        return cost + heuristic(path[-1], goal)

    def choose_path(paths):
        return min(paths, key=path_cost)
    return _tree_search(choose_path, graph, start, goal)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
