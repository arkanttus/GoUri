from flask import Flask
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object(test_config)

    from .app.routes import routes

    app.register_blueprint(routes)

    CORS(app)

    return app
