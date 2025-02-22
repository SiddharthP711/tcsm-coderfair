from flask import Flask
from .routes import init_routes
from .config import init_config
from .routes.error_handlers import init_error_handlers
from flask_cors import CORS


def create_app():
    app = Flask("website")

    # Enable cross-origin resource sharing
    CORS(app)

    # config
    init_config(app)

    # security key, test mode, debugging window

    # Register the routes by calling init_routes
    init_routes(app)

    # Register the error handlers to handle 400, 404, 500, and all other exceptions in routes
    init_error_handlers(app)

    return app
