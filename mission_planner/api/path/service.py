from flask import request
from flask_restplus import Resource

from mission_planner.api import api
from mission_planner.api.path import serializers

path_ns = api.namespace('path')


@path_ns.route('')
class Path(Resource):

    @staticmethod
    @api.expect(serializers.mission_parameters)
    def post():
        mission_parameters = request.json
        x = mission_parameters['x']
        y = mission_parameters['y']
        return (x, y), 200
