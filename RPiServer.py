from flask import Flask, request
from flask_restx import Api, Resource
from pi_block_capture import pi_picture

app = Flask(__name__)
api = Api(app)

if __name__ == "__main__":
    app.run(debug=True, host="localhost")