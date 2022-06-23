from flask import Flask
from flask_restful import Api
# __name__ = '__main__'
from routes import set_routes


app: Flask = Flask(__name__) #app
api: Api = Api(app)
set_routes(api)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

