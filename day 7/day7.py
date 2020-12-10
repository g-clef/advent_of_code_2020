import networkx
import re

data = [line.strip().strip(".") for line in open("input.txt").readlines()if line.strip()]

bag_name_re = re.compile(r'(\w+ \w+) bag[s]?')
numbered_bag_re = re.compile(r'\s?(\d) (\w+ \w+) bag[s.]?')


def build_graph(data):
    graph = networkx.DiGraph()
    for line in data:
        base, contents = line.split("contain")
        base_color = bag_name_re.match(base).groups()[0]
        graph.add_node(base_color)
        for content in contents.split(","):
            match = numbered_bag_re.match(content)
            if match:
                number, kind = match.groups()
                graph.add_node(kind)
                graph.add_edge(base_color, kind, weight=int(number))
    return graph


def traverse_graph(graph, start_node, depth, reverse=True):
    return {node[1] for node in networkx.bfs_edges(graph, source=start_node, depth_limit=depth, reverse=reverse) if node[1] != start_node}


bags = build_graph(data)
# part 1: answer 248
possible_containers = traverse_graph(bags, "shiny gold", bags.number_of_nodes(), reverse=True)
print(f"containers {len(possible_containers)}")


# part 2: answer: 57281
def find_weight(graph, target_node):
    return 1 + sum(graph.get_edge_data(target_node, child)['weight'] * find_weight(graph, child) for child in graph.successors(target_node))


def find_from_base(graph, target_node):
    # treat the base node as different...we're not counting the base node in our calculations
    return sum(graph.get_edge_data(target_node, child)['weight'] * find_weight(graph, child) for child in graph.successors(target_node))


print(find_from_base(bags, "shiny gold"))
