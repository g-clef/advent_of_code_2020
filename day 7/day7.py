import networkx
import re

data = [line.strip().strip(".") for line in open("input.txt").readlines()]

bag_name_re = re.compile(r'(\w+ \w+) bag[s]?')
numbered_bag_re = re.compile(r'\s?(\d) (\w+ \w+) bag[s.]?')


def build_graph(data):
    graph = networkx.DiGraph()
    for line in data:
        if not line:
            continue
        base, contents = line.split("contain")
        base_color = bag_name_re.match(base).groups()[0]
        if base_color not in graph:
            graph.add_node(base_color)
        for content in contents.split(","):
            match = numbered_bag_re.match(content)
            if match:
                number, kind = match.groups()
                if kind not in graph:
                    graph.add_node(kind)
                graph.add_edge(base_color, kind, weight=int(number))
    return graph


def traverse_graph(graph, start_node, depth, reverse=True):
    containers = set()
    for node in networkx.bfs_edges(graph, source=start_node, depth_limit=depth, reverse=reverse):
        if node[1] == start_node:
            continue
        containers.add(node[1])
    return containers


bags = build_graph(data)
kinds_of_bags = bags.number_of_nodes()
print(f"total # of bags {kinds_of_bags}")
# part 1: answer 248
possible_containers = traverse_graph(bags, "shiny gold", kinds_of_bags, reverse=True)
print(f"containers {len(possible_containers)}")

# part 2: answer: 57281


def find_weight(graph, target_node):
    children = graph.successors(target_node)
    child_weights = 0
    for child in children:
        weight = graph.get_edge_data(target_node, child)['weight']
        child_weights += weight*find_weight(graph, child)
    return 1 + child_weights


def find_from_base(graph, target_node):
    # treat the base node as different...we're not counting the base node in our calculations
    total = 0
    for child in graph.successors(target_node):
        weight = graph.get_edge_data(target_node, child)['weight']
        total += weight*find_weight(graph, child)
    return total


result = find_from_base(bags, "shiny gold")
print(f"part 2 {result}")
