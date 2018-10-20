import math
import networkx as nx
import numpy as np
from PIL import Image

SCALE = 8
N = int(2048 / SCALE)
SCALE_TO_METERS = 26.6666

im = Image.open('mission_planner/assets/example1.png')
im = im.convert('L')
image_pixels = np.asarray(im)


def get_pixel_value(x, y):
    return image_pixels[x, y]


def get_height(x, y):  # return meters
    return (image_pixels[x, y] - 67) * SCALE_TO_METERS - 3000


def get_distance_to_drive(a_x, a_y, b_x, b_y):
    height_difference = get_height(a_x, a_y) - get_height(b_x, b_y)  # in meters
    return math.sqrt(height_difference ** 2 + ((((b_x - a_x) + (b_y - a_y)) * 100) ** 2))


def get_weight(a_x, a_y, b_x, b_y):
    height_difference = get_height(a_x, a_y) - get_height(b_x, b_y)  # in meters
    distance_to_drive = get_distance_to_drive(a_x, a_y, b_x, b_y)
    punishment_or_gain_for_height = 100 if height_difference > 0 else -5
    return distance_to_drive * punishment_or_gain_for_height


def add_edge_with_weight(graph, a_x, a_y, b_x, b_y):
    weight = get_weight(a_x * SCALE, a_y * SCALE, b_x * SCALE, b_y * SCALE)
    weight += 10000  # This will prevent Dijkstra to work on negative weights
    graph.add_edge('{}_{}'.format(a_x, a_y), '{}_{}'.format(b_x, b_y), weight=weight)


def get_graph():
    graph = nx.DiGraph()
    for _y in range(1, N - 1):
        for _x in range(1, N - 1):
            add_edge_with_weight(graph, _x, _y, _x + 1, _y)
            add_edge_with_weight(graph, _x + 1, _y, _x, _y)
            add_edge_with_weight(graph, _x, _y, _x, _y + 1)
            add_edge_with_weight(graph, _x, _y + 1, _x, _y)
    return graph
