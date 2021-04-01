from flask import Flask
from .extenstions import db
from .routes.link_blueprint import short


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)
    db.init_app(app)
    # app.register_blueprint(short, url_prefix="/shorten")
    app.register_blueprint(short)
    return app


app = create_app()

@app.before_first_request
def create_tables():
    db.create_all()


# app.run(host='0.0.0.0', port=4000)
