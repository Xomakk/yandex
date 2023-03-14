from .user_parce import parse
from flask import jsonify
from flask_restful import Resource, abort
from . import db_session
from .user import User


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        abort(404, message=f'User id={user_id} not found.')


# класс для получение одного объекта с указанным id
class UserResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).filter(User.id == user_id).first()
        return jsonify({'user': user.to_dict(
            only=('id', 'name', 'about', 'email', 'created_date')
        )})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).filter(User.id == user_id).first()
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


# класс для получения списка объектов из таблицы User
class UserListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [
            user.to_dict(only=('id', 'name', 'about', 'email', 'created_date'))
            for user in users
        ]})

    def post(self):
        args = parse.parse_args()
        session = db_session.create_session()
        user = User(
            name=args['name'],
            about=args['about'],
            email=args['email']
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})
