from flask_restplus import fields

from mission_planner.api import api

in__single_point = api.model('Representation of single input point', {
    'x': fields.Integer(),
    'y': fields.Integer(),
})

out__single_point = api.model('Representation of single output point', {
    'x': fields.Integer(),
    'y': fields.Integer(),
    'z': fields.Integer(),
})

mission_parameters = api.model('Mission parameters', {
    'points': fields.List(fields.Nested(in__single_point)),
})

mission_result = api.model('Result of the mission', {
    'path': fields.List(fields.Nested(out__single_point)),
    'hypsometric_profile': fields.List(fields.Float),
    'total_distance': fields.Float(),
})
