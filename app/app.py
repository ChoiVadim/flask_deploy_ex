from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from app.config import Config


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    CORS(app)
    migrate = Migrate(app, db)
    
    with app.app_context():
        from app.test.routes import test_routes
        app.register_blueprint(test_routes)

        db.create_all()

    return app

