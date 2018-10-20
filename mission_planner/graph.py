import math
import networkx as nx
import numpy as np
from PIL import Image

SCALE = 8
MAGIC_NUMBER = 100

im = Image.open("assets/example1.png")
im = im.convert('L')
image_pixels = np.asarray(im)


def get_height(x, y):
    return image_pixels[x, y] * MAGIC_NUMBER


def get_weight(a_x, a_y, b_x, b_y):
    return math.sqrt((get_height(a_x, a_y) - get_height(b_x, b_y)) ** 2 +
                     ((b_x * 100 - a_x * 100) + (b_y * 100 - a_y * 100)) ** 2)


def add_edge_with_weight(graph, a_x, a_y, b_x, b_y):
    weight = get_weight(a_x * SCALE, a_y * SCALE, b_x * SCALE, b_y * SCALE)
    graph.add_edge('{}_{}'.format(a_x, a_y), '{}_{}'.format(b_x, b_y), weight=weight)


def get_graph():
    N = int(2048 / SCALE)
    graph = nx.DiGraph()
    for _y in range(1, N - 1):
        for _x in range(1, N - 1):
            add_edge_with_weight(graph, _x, _y, _x + 1, _y)
            add_edge_with_weight(graph, _x + 1, _y, _x, _y)
            add_edge_with_weight(graph, _x, _y, _x, _y + 1)
            add_edge_with_weight(graph, _x, _y + 1, _x, _y)
    return graph
