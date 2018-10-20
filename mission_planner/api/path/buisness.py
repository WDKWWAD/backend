import networkx as nx


def compute_path(graph, mission_points):
    SCALE = 8

    path = []

    for i in range(len(mission_points) - 1):
        source_a = '{}_{}'.format(int(mission_points[i]['x'] / SCALE), int(mission_points[i]['y'] / SCALE))
        source_b = '{}_{}'.format(int(mission_points[i + 1]['x'] / SCALE), int(mission_points[i + 1]['y'] / SCALE))
        p = nx.dijkstra_path(graph, source_a, source_b)
        for entry in p:
            path.append({'x': int(entry.split('_')[0]) * SCALE, 'y': int(entry.split('_')[1]) * SCALE})

    return path
