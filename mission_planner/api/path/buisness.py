import networkx as nx


def compute_path(graph, mission_points):
    SCALE = 8
    starting_point = [mission_points[0]['x'], mission_points[0]['y']]
    finish_point = [mission_points[-1]['x'], mission_points[-1]['y']]

    source_a = '{}_{}'.format(int(starting_point[0] / SCALE), int(starting_point[1] / SCALE))
    source_b = '{}_{}'.format(int(finish_point[0] / SCALE), int(finish_point[1] / SCALE))
    path = nx.dijkstra_path(graph, source_a, source_b)

    return [{'x': int(entry.split('_')[0]) * SCALE, 'y': int(entry.split('_')[1]) * SCALE} for entry in path]
