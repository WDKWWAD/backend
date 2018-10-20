from flask_restplus import fields

from mission_planner.api import api

mission_parameters = api.model('Mission parameters', {
    'x': fields.Float(),
    'y': fields.Float()
})
