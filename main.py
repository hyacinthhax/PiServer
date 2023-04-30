from flask import Flask
from views import views_blueprint
from auth import auth_blueprint


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

    # Register Blueprint
    app.register_blueprint(views_blueprint, url_prefix='/')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
