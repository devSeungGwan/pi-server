from flask import Flask
from flask_restx import Api, Resource
from pi_picture import pi_picture

app = Flask(__name__)
api = Api(app)

@api.route('/capture')
class Capture(Resource):
    def get(self):
        pi_picture()

if __name__ == "__main__":
    app.run(debug=True, host="localhost")