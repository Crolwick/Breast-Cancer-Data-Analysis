from flask import Flask
from flask_cors import CORS

from .routes import body

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(body)
    
    return app