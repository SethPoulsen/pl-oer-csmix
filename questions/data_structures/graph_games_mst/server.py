from collections import defaultdict

import functools
import io
import itertools
import networkx as nx
import random


def generate(data):
    # Max weights
    G_max = generate_question_graph()

    data["params"]["graph_max"] = get_graphviz_graph(G_max).string()

    max_weights = get_max_weights(G_max)

    data["params"]["max_question_html"] = []

    for e in sorted(get_question_edges(G_max)):
        label = "weight({0}, {1}) $=$".format(*e)

        name = "max_edge_{0}_{1}".format(*e)

        data["params"]["max_question_html"].append(get_integer_question_html(label, name, 1))

        data["correct_answers"][name] = max_weights[e]

    data["params"]["max_question_html"] = "\n".join(data["params"]["max_question_html"])

    # Unique weights
    G_unique = generate_question_graph()

    data["params"]["graph_unique_json"] = nx.node_link_data(G_unique)

    data["params"]["graph_unique"] = get_graphviz_graph(G_unique).string()

    data["params"]["unique_question_html"] = []

    for e in sorted(get_question_edges(G_unique)):
        label = "weight({0}, {1}) $=$".format(*e)

        name = "unique_edge_{0}_{1}".format(*e)

        data["params"]["unique_question_html"].append(get_integer_question_html(label, name, 1))

    data["params"]["unique_question_html"] = "\n".join(data["params"]["unique_question_html"])

    return data


def grade(data):
    G = nx.node_link_graph(data["params"]["graph_unique_json"])

    submitted_weights = {}

    for e in get_question_edges(G):
        name = "unique_edge_{0}_{1}".format(*e)

        submitted_weights[e] = data["submitted_answers"][name]

    max_weights = get_max_weights(G)

    used_weights = set()

    tot = 0
    for e in sorted(submitted_weights, key=lambda x: submitted_weights[x], reverse=True):
        name = "unique_edge_{0}_{1}".format(*e)

        w = submitted_weights[e]

        if w in used_weights:
            score = 0

        elif w > max_weights[e]:
            score = 0

        else:
            best_weight = max_weights[e]

            while best_weight in used_weights:
                best_weight -= 1

            if w == best_weight:
                score = 1
                tot += 1

            else:
                score = 0

        used_weights.add(w)

        data["partial_scores"][name] = {}

        data["partial_scores"][name]["score"] = score
    
    data["score"] = data["score"]/2 + (tot/len(max_weights))


def get_integer_question_html(label, name, weight):
    return """<pl-integer-input answers-name="{0}" label="{1}" weight={2}></pl-integer-input>""".format(
        name, label, weight
    )


def node_cycle_to_edges(cycle):
    """ Convert a list of nodes in a cycle to a list of edges.

    Parameters
    ----------
        cycle: list of nodes in the cycle.

    Returns:
        set of edges in the cycle where edges are represented as sets
    """
    edges = set()
    size = len(cycle)
    for i in range(size):
        u = cycle[i]
        v = cycle[(i + 1) % size]
        e = frozenset((u, v))
        edges.add(e)
    return set(edges)


def get_all_cycles(G):
    """ Get all single cycles from the graph.

    Parameters
    ----------
        G: (nx.Graph) Graph to find cycles in.

    Returns
    -------
        list of cycles represented as list of tuples of edges
    """
    basis = [node_cycle_to_edges(x) for x in nx.cycle_basis(G)]
    cycles = set([frozenset(x) for x in basis])
    for i in range(2, len(basis) + 1):
        for x in itertools.combinations(basis, i):
            c = functools.reduce(set.symmetric_difference, x)
            node_count = defaultdict(int)
            for u, v in c:
                node_count[u] += 1
                node_count[v] += 1
            if max(node_count.values()) <= 2:
                cycles.add(frozenset(c))
    return [sorted([tuple(sorted(y)) for y in x]) for x in cycles]


def generate_unweighted_graph():
    """ Generate unweigted graph that matches topology of 2019W1 final.
    """
    G = nx.Graph()
    G.add_edge("A", "B")
    G.add_edge("A", "C")
    G.add_edge("A", "F")
    G.add_edge("B", "C")
    G.add_edge("B", "C")
    G.add_edge("B", "D")
    G.add_edge("C", "D")
    G.add_edge("C", "E")
    G.add_edge("C", "F")
    G.add_edge("D", "E")
    G.add_edge("E", "F")
    return G


def generate_original_question_graph():
    """ Generate graph form 2019W1 final exam
    """
    G = generate_unweighted_graph()
    G.edges[("A", "C")]["weight"] = 8
    G.edges[("A", "F")]["weight"] = 4
    G.edges[("B", "D")]["weight"] = 7
    G.edges[("C", "D")]["weight"] = 10
    G.edges[("E", "F")]["weight"] = 6
    return G


def generate_weighted_graph():
    """ Generate a randomly weighted graph.
    """
    G = generate_unweighted_graph()
    for e in G.edges():
        G.edges[e]["weight"] = random.randint(0, 10)
    return G


def generate_question_graph():
    """ Generate a graph for the question by finding an MST and removing weights.
    """
    G = generate_weighted_graph()
    for u, v, _ in nx.minimum_spanning_edges(G):
        del G.edges[(u, v)]["weight"]
    return G


def get_question_edges(G):
    for e in G.edges:
        if "weight" not in G.edges[e]:
            yield e


def get_max_edge_weights(G):
    """ For all single cycles in the graph find the maximum weight that could be assigned to a missing edge.

    The main idea is that we can set the missing weights to be less than the biggest weight on the cycle for the MST.

    Parameters
    ----------
        G: (nx.Graph) Graph to compute weights from.

    Returns
    -------
        weights: (dict) Dictionary of lists with max weights on each cycle the edge is included in.
    """
    weights = defaultdict(list)
    for c in get_all_cycles(G):
        w = [G.edges[e]["weight"] for e in c if "weight" in G.edges[e]]
        for e in c:
            if "weight" not in G.edges[e]:
                weights[e].append(max(w))
    return weights


def get_max_weights(G):
    """ Get the maximum weight we could assign to missing edges to guarantee they form an MST.

    Parameters
    ----------
        G: (nx.Graph) Graph to compute weights from.

    Returns
    -------
        weights: (dict) Dictionary of scalars indicating max possible weight for edges in the MST.
    """
    weights = {}
    all_weights = get_max_edge_weights(G)
    for e in all_weights:
        w = min(all_weights[e]) - 1
        weights[e] = w
        # Make sure both directions included
        weights[(e[1], e[0])] = w
    return weights


def get_unique_max_weights(G):
    """ Get the maximum unique weights we could assign to missing edges to guarantee they form an MST.

    This differs from `get_max_weights` in that all weights are unique.

    Parameters
    ----------
        G: (nx.Graph) Graph to compute weights from.

    Returns
    -------
        weights: (dict) Dictionary of scalars indicating max possible unique weight for edges in the MST.
    """
    weights = {}
    all_weights = get_max_edge_weights(G)
    for e in all_weights:
        w = min(all_weights[e]) - 1
        while w in weights.values():
            w -= 1
        weights[e] = w
    return weights


def add_weights(G, weights):
    """ Add weights to graph.

    Parameters
    ----------
        G: (nx.Graph) Graph to annotate
        weights: (dict) Dictionary mapping edges to weights
    """
    for e in weights:
        G.edges[e]["weight"] = weights[e]


def get_graphviz_graph(G):
    """ Convert the networkx graph to a pygraphviz graph for export.

    Edges without weights will be drawn in bold.

    Parameters
    ----------
        G: (nx.Graph) Graph to convert

    Returns:
        pygraphviz.Graph
    """
    G = G.copy()
    for e in G.edges():
        if "weight" in G.edges[e]:
            G.edges[e]["label"] = G.edges[e]["weight"]
            G.edges[e]["fontsize"] = 18
        else:
            G.edges[e]["style"] = "bold"
            G.edges[e]["penwidth"] = 8
        G.edges[e]["len"] = 1.2
    for n in G.nodes():
        G.nodes[n]["shape"] = "circle"
    return nx.nx_agraph.to_agraph(G)


def write_graph_to_file(G, out_file):
    """ Write graph to image file.

    Edges without weights will be drawn in bold.
    """
    A = get_graphviz_graph(G)
    A.draw(out_file, prog="neato")
