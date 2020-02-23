def create_app():
    from flask import Flask

    from .views import users

    app = Flask(__name__)

    app.add_url_rule('/users',view_func= users.list)

    return app
