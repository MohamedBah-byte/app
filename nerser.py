from flask import Flask
from flask_restful import Api, Resource, reqparse
import stanza
stanfordnlp.download('fr')
app = Flask(__name__)
api = Api(app)
nlp=stanza.Pipeline('fr')

class NEREntinty(Resource):
    def get(self, text):
        doc = nlp(text)
        return doc.entities()

api.add_resource(NEREntinty)
if __name__ == '__main__':
    app.run(port='5005')
