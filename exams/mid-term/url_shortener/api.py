from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

urls = {}

class Url(Resource):
    def get(self, url_hash):
        print('TODO-GET:url_hash=', url_hash)
        return {'id': 'FIX_ME', 'short': 'FIX_ME', 'url': 'FIX_ME'}

    def delete(self, url_hash):
        print('TODO-DELETE')
        return None, 204

class ShortenUrl(Resource):
    def post(self):
        print('TODO-POST:Shorten URL')
        return {}


api.add_resource(ShortenUrl, '/url')
api.add_resource(Url, '/url/<string:url_hash>')

if __name__ == '__main__':
    app.run(debug=True)
