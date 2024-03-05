import heapq
import math
import networkx as nx
import numpy as np


def generate(data):
    size = np.random.randint(9, 15)

    values = [int(x) for x in np.random.choice(100, size, replace=False)]

    heap = Heap(values)

    data["params"]["graph"] = heap.to_dot()

    data["params"]["inserted_values"] = get_inserted_values_html_string(heap)

    data["params"]["removed_values"] = get_removed_values_html_string(heap)

    return data


def get_inserted_values_html_string(heap):
    html_str = []

    correct_vals = heap.find_last_inserted_values()

    for i in sorted(heap.values):
        if i in correct_vals:
            html_str.append(
                """<pl-answer correct='true'>{}</pl-answer>""".format(i)
            )
        else:
            html_str.append(
                """<pl-answer>{}</pl-answer>""".format(i)
            )

    return "\n".join(html_str)


def get_removed_values_html_string(heap):
    html_str = []

    new_heap = heap.copy()

    correct_vals = new_heap.remove_min()[1]

    for i in sorted(heap.values):
        if i in correct_vals:
            html_str.append(
                """<pl-answer correct='true'>{}</pl-answer>""".format(i)
            )
        else:
            html_str.append(
                """<pl-answer>{}</pl-answer>""".format(i)
            )

    return "\n".join(html_str)


class Heap(object):
    """ Binary heap structure.

    Values are stored in 0-indexed array.
    """

    def __init__(self, values):
        """ Construct the heap array from an arbitrary list of values.
        """
        self.values = values.copy()

        heapq.heapify(self.values)
        
        if self.values[0] in self.find_last_inserted_values():
            self._swap(1, 2)
            self.heapifyDown(3 - self.max_priority_child(0))

    def copy(self):
        return Heap(self.values.copy())

    @property
    def last_idx(self):
        """ Last valid index of the array.
        """
        return self.size - 1

    @property
    def size(self):
        """ Size of the heap.
        """
        return len(self.values)

    def draw(self):
        """ Draw heap using matplotlib.
        """
        G = self.to_graph()

        node_map = dict(zip(range(self.size), self.values))

        nx.draw_networkx(
            G,
            labels=node_map,
            pos=nx.nx_agraph.graphviz_layout(G, prog="dot"),
            with_labels=True,
        )

    def get_parent_idx(self, idx):
        """ Get array index of parent of idx.
        """
        return math.floor((idx - 1) / 2)

    def get_child_idxs(self, idx):
        """ Get the array index of left and right children of idx.
        """
        return 2 * idx + 1, 2 * idx + 2

    def get_child_values(self, idx):
        """ Return values of childrent of idx.
        """
        lc_idx, rc_idx = self.get_child_idxs(idx)

        values = []

        if self.is_valid_idx(lc_idx):
            values.append(self.values[lc_idx])

        if self.is_valid_idx(rc_idx):
            values.append(self.values[rc_idx])

        return values

    def find_last_inserted_values(self):
        """ Return all possible values which could have been last inserted into heap.
        """
        values = []

        idx = self.last_idx

        while True:
            parent_idx = self.get_parent_idx(idx)

            if parent_idx < 0:
                break

            if self.values[idx] != min(self.get_child_values(parent_idx)):
                break

            values.append(self.values[idx])

            idx = parent_idx

        values.append(self.values[idx])

        return values

    def is_valid_idx(self, idx):
        return (idx >= 0) and (idx <= self.last_idx)
        
    def max_priority_child(self, idx):
        if 2 * idx + 2 >= len(self.values) or self.values[2 * idx + 1] < self.values[2 * idx + 2]:
            return 2 * idx + 1
        return 2 * idx + 2
        
    def heapifyDown(self, idx):
        if 2 * idx + 1 < len(self.values):
            m = self.max_priority_child(idx)
            
            if self.values[m] < self.values[idx]:
                self._swap(m, idx)
                self.heapifyDown(m)

    def remove_min(self):
        """ Remove the minimum element of the heap and return its value and values of keys modified in heapify.
        """
        # Root and last element are swapped
        values = [self.values[0], self.values[self.last_idx]]

        self._swap(0, self.last_idx)

        # Remove last element
        min_val = self.values.pop(self.last_idx)

        # Heapify down tracking values
        idx = 0

        child_vals = self.get_child_values(idx)

        while (len(child_vals) > 0) and (self.values[idx] > min(child_vals)):
            lc_idx, rc_idx = self.get_child_idxs(idx)

            if child_vals[0] == min(child_vals):
                new_idx = lc_idx

            else:
                new_idx = rc_idx

            self._swap(idx, new_idx)

            values.append(self.values[idx])

            idx = new_idx

            child_vals = self.get_child_values(idx)

        return min_val, values

    def to_dot(self):
        """ Convert heap to dot reprensetation.
        """
        G = self.to_graph()

        return nx.nx_agraph.to_agraph(G).string()

    def to_graph(self):
        """ Convert the heap to a DiGraph representing complete tree.
        """
        G = nx.DiGraph()

        # Add nodes to graph and label by value
        for idx in range(self.size):
            G.add_node(idx, label=self.values[idx])

        # Add edges to graph
        for idx in range(len(self.values)):
            lc_idx, rc_idx = self.get_child_idxs(idx)

            if self.is_valid_idx(lc_idx):
                G.add_edge(idx, lc_idx)

            if self.is_valid_idx(rc_idx):
                G.add_edge(idx, rc_idx)

        return G

    def _swap(self, a, b):
        """ Swap two values of array in place.
        """
        temp = self.values[a]

        self.values[a] = self.values[b]

        self.values[b] = temp
