from flask import Flask
from flask_restful import Api, Resource, reqparse
import stanza

app = Flask(__name__)
api = Api(app)
nlp=stanza.Pipeline('fr')

class NEREntinty(Resource):
    def get(self, text):
        doc = nlp(Resource)
        return doc.entities()

api.add_resource(NEREntinty)
if __name__ == '__main__':
    app.run(port='5005')
    
