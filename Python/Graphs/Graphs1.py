# Graphs are easily built out of lists and dictionaries

# Ex. 
#    A -> B
#    A -> C
#    B -> C
#    B -> D
#    C -> D
#    D -> C
#    E -> F
#    F -> C


# This graph has six nodes (A-F) and eight arcs.
# It can be represented by the following Python data structure:
# graph = {'A': ['B', 'C'],
#          'B': ['C', 'D'],
#          'C': ['D'],
#          'D': ['C'],
#          'E': ['F'],
#          'F': ['C']}


# Let's write a simple function to determine a path between two nodes.
# It takes a graph and the start and end nodes as arguments.
# It will return a list of nodes (including the start and end nodes) comprising the path.
# When no path can be found, it returns None.
# The same node will not occur more than once on the path returned (i.e. it won't contain cycles).
# The algorithm uses an important technique called backtracking: it tries each possibility in turn until it finds a solution.

def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None
    
#    >>> find_path(graph, 'A', 'D')
#    ['A', 'B', 'C', 'D']
#    >>>

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
    
#    >>> find_all_paths(graph, 'A', 'D')
#    [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]
#    >>>    

# Another variant finds the shortest path
def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
    
    
#Eryk Kopczyński pointed out that these functions are not optimal.
#To the contrary, "this program runs in exponential time, while find_shortest_path can be done in linear time using BFS [Breadth First Search].
#Furthermore a linear BFS is simpler:"
    
# Code by Eryk Kopczyński
    def find_shortest_path(graph, start, end):
        dist = {start: [start]}
        q = deque(start)
        while len(q):
            at = q.popleft()
            for next in graph[at]:
                if next not in dist:
                    dist[next] = [dist[at], next]
                    q.append(next)
        return dist[end]