from flask import Flask
from data import db_session
from data.user import User

from flask_restful import reqparse, abort, Api, Resource

from data.user_resource import UserResource, UserListResource

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/blogs.db')

    api.add_resource(UserResource, '/api/v2/users/<int:user_id>')
    api.add_resource(UserListResource, '/api/v2/users')

    app.run()


@app.route('/')
def index():
    return 'hello world!'


if __name__ == '__main__':
    main()
