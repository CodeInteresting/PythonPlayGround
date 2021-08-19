# Dijkstra Algorithm

graph = {}  # Dict
graph["MusicBook"] = {"BlackDisc": 5, "Poster": 0}
graph["BlackDisc"] = {"BassGuitar": 15, "Drum": 20}
graph["Poster"] = {"BassGuitar": 30, "Drum": 35}
graph["BassGuitar"] = {"Piano": 20}
graph["Drum"] = {"Piano": 10}
graph["Piano"] = {}

costs = {}  # Dict
infinity = float("inf")  # positive infinity
costs["MusicBook"] = 0
costs["BlackDisc"] = infinity
costs["Poster"] = infinity
costs["BassGuitar"] = infinity
costs["Drum"] = infinity
costs["Piano"] = infinity

# Processed Node won't be processed again.
# Processed Node means that the lowest cost from start to that node
# has been determined
processed_nodes = set()

# Trace the previous node of current node
parents = {}


def find_lowest_cost_node():
    lowestCost = infinity
    nodeFound = None
    for node, cost in costs.items():
        if (node not in processed_nodes) and (cost < lowestCost):
            lowestCost = cost
            nodeFound = node
    return nodeFound


def dijkstra_algo():
    lowest_cost_node = "MusicBook"  # hard code
    while lowest_cost_node is not None:
        neighbours = graph[lowest_cost_node]
        for node, cost in neighbours.items():
            newCost = costs[lowest_cost_node] + cost
            if newCost < costs[node]:
                costs[node] = newCost
                parents[node] = lowest_cost_node
        processed_nodes.add(lowest_cost_node)
        lowest_cost_node = find_lowest_cost_node()


dijkstra_algo()
print(parents)
