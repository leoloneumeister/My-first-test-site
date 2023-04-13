from app.extensions.database import db

from flask import Flask, render_template
from app.simple_pages.routes import blueprint as simple_pages_blueprint

def create_app():
  app = Flask(__name__)
  register_blueprints(app)

  return app

def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config')

  register_extensions(app)
  register_blueprints(app)

  return app


def register_blueprints(app):
  app.register_blueprint(simple_pages_blueprint)


def register_extensions(app: Flask):
  db.init_app(app)
