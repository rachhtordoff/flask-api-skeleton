from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


def register_blueprint(app):
    from src.routes.general import general_blueprint

    app.register_blueprint(general_blueprint)


register_blueprint(app)
