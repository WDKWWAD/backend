from flask import Flask, Blueprint
from flask_cors import CORS

from mission_planner.api import api
from mission_planner.api.path.service import path_ns

app = Flask(__name__)
CORS(app)


def initialize_app(flask_app):
    app.config['SECRET_KEY'] = 'secret'

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)

    api.add_namespace(path_ns)
    flask_app.register_blueprint(blueprint)


def main():
    initialize_app(app)
    app.run(debug='True')


if __name__ == "__main__":
    main()
