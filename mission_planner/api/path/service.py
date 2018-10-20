from flask import request
from flask_restplus import Resource

from mission_planner.api import api
from mission_planner.api.path import serializers
from mission_planner.api.path.buisness import compute_path
from mission_planner.graph import get_graph

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


