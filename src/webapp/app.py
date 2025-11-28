"""Flask-sovelluksen luonti ja konfigurointi."""

from flask import Flask
from .models import db
from .routes import main_bp


def create_app(config=None):
    """Luo ja konfiguroi Flask-sovelluksen."""
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///varasto.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev-secret-key'

    if config:
        app.config.update(config)

    db.init_app(app)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    application = create_app()
    application.run(debug=True)
