from flask import Flask, request
from flask_restx import Api, Resource
from pi_block_capture import pi_picture

app = Flask(__name__)
api = Api(app)

@api.route('/capture')
class Capture(Resource):
    def post(self):
        capture_folder = request.json.get('capture_folder')
        fin = pi_picture(capture_folder)
    
        return fin

if __name__ == "__main__":
    app.run(debug=True, host="localhost")