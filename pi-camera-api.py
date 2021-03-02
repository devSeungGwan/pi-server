from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('./capture')
class Capture(Resource):
    def get(self):
        return {"Hello": "World!"}


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=80)