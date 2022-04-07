# src/__init__.py

from email import message
import resource
from flask import Flask, jsonify
from flask_restx import Resource, Api

app = Flask(__name__)

api = Api(app)

# set config
app.config.from_object('src.config.DevelopmentConfig') # new

# x = (1/0)

class Ping(Resource):
    def get(self):
        return {'status': 'success', 'message': 'pong!'}


api.add_resource(Ping, '/ping')
