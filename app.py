from flask import Flask
from flask_restful import Resource, Api
# __name__ = '__main__'
app = Flask(__name__) #app
api = Api(app)

class HealthCheckResource(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'name': 'john'}

class UserResource(Resource):
    def put(self):
        return {'age': 25}

api.add_resource(UserResource, '/user')
api.add_resource(HealthCheckResource, '/health-check')

if __name__ == '__main__':
    app.run(debug=True)