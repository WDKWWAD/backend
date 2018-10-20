import networkx as nx
from flask import request
from flask_restplus import Resource

from mission_planner.api import api
from mission_planner.api.path import serializers
from mission_planner.api.path.buisness import compute_path

path_ns = api.namespace('path')


@path_ns.route('')
class Path(Resource):

    @staticmethod
    @api.expect(serializers.mission_parameters)
    def post():
        mission_parameters = request.json
        mission_points = mission_parameters['points']

        graph = get_graph()

        path = compute_path(graph, mission_points)

        return path, 200


def get_graph():
    SCALE = 8
    N = int(2048 / SCALE)
    graph = nx.DiGraph()
    for _y in range(1, N):
        for _x in range(1, N):
            # TODO: Calculate weights properly
            graph.add_edge('{}_{}'.format(_x, _y), '{}_{}'.format(_x + 1, _y), weight=1)
            graph.add_edge('{}_{}'.format(_x + 1, _y), '{}_{}'.format(_x, _y), weight=1)
            graph.add_edge('{}_{}'.format(_x, _y), '{}_{}'.format(_x, _y + 1), weight=1)
            graph.add_edge('{}_{}'.format(_x, _y + 1), '{}_{}'.format(_x, _y), weight=1)
    return graph
