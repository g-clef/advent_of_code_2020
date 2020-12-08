import networkx
import re
import math

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
                graph.add_edge(base_color, kind, weight=number)
    return graph


def traverse_graph(graph, start_node, depth, reverse=True):
    containers = set()
    for node in networkx.bfs_edges(graph, source=start_node, depth_limit=depth, reverse=reverse):
        if node[1] == start_node:
            continue
        containers.add(node[1])
    return containers


def traverse_graph_weights(graph, base_node):
    total = 0
    paths = list()
    for node in networkx.algorithms.dag.descendants(graph, base_node):
        print(f"testing {node}")
        if graph.out_degree(node) == 0:
            # this is a leaf, can compute from here:
            paths.extend(networkx.all_shortest_paths(graph, base_node, node))
    print(f"paths is {paths}")
    for path in paths:
        # path will be a list of nodes. walk that list in pairs to get the edges & their weights
        path.reverse()
        print(f"path is {path}")
        path_weight = 1
        for pair_counter in range(len(path)-1):
            start_node = path[pair_counter + 1]
            end_node = path[pair_counter]
            print(f"edge is {start_node} to {end_node}")
            weight = int(graph.get_edge_data(start_node, end_node)['weight'])
            print(f"weight is {weight}")
            # this is the weight of the contents
            path_weight = weight*(1 + path_weight)
            print(f"total so far {path_weight}")
        total += path_weight
    return total


test_data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


bags = build_graph(data)
kinds_of_bags = bags.number_of_nodes()
print(f"total # of bags {kinds_of_bags}")
# part 1: answer 248
possible_containers = traverse_graph(bags, "shiny gold", kinds_of_bags, reverse=True)
print(f"containers {len(possible_containers)}")
# part 2:

test_data2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

bags2 = build_graph(test_data.split("\n"))

possible_containers2 = traverse_graph_weights(bags2, "shiny gold")
print(possible_containers2)
