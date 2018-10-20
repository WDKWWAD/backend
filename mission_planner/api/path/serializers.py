from flask_restplus import fields

from mission_planner.api import api

single_point = api.model('Representation of single point', {
    'x': fields.Integer(),
    'y': fields.Integer(),
})

mission_parameters = api.model('Mission parameters', {
    'points': fields.List(fields.Nested(single_point)),
})
