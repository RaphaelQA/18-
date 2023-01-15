from flask_restx import Resource, Namespace

from implemented import director_service, director_schema, directors_schema

directors_ns = Namespace('directors')


@directors_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = director_service.get_all()
        return directors_schema.dump(genres), 200


@directors_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        director = director_service.get_by_id(gid)
        return director_schema.dump(director), 200