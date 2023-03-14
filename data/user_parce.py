from flask_restful import reqparse

parse = reqparse.RequestParser()
parse.add_argument('name', required=True)
parse.add_argument('about', required=True)
parse.add_argument('email', required=True)