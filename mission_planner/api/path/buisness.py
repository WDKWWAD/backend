import networkx as nx

from mission_planner.graph import get_distance_to_drive, get_pixel_value, get_height

SCALE = 8


def get_total_distance(path):
    total = 0
    for i in range(len(path) - 1):
        total += get_distance_to_drive(path[i]['x'], path[i]['y'], path[i + 1]['x'], path[i + 1]['y'])
    return total


def get_hypsometric_profile(path):
    return [get_height(point['x'], point['y']) for point in path]


def compute_path(graph, mission_points):
    path = []
    total_distance = 0

    for i in range(len(mission_points) - 1):
        source_a = '{}_{}'.format(int(mission_points[i]['x'] / SCALE), int(mission_points[i]['y'] / SCALE))
        source_b = '{}_{}'.format(int(mission_points[i + 1]['x'] / SCALE), int(mission_points[i + 1]['y'] / SCALE))
        p = nx.dijkstra_path(graph, source_a, source_b)
        for entry in p:
            x = int(entry.split('_')[0]) * SCALE
            y = int(entry.split('_')[1]) * SCALE
            path.append({'x': x, 'y': y, 'z': get_pixel_value(x, y)})
        total_distance += get_total_distance(path)

    hypsometric_profile = get_hypsometric_profile(path)

    return path, hypsometric_profile, total_distance
