from flask import Flask
from flask_restful import Api, Resource, reqparse
import stanza
stanfordnlp.download('fr')
app = Flask(__name__)


@app.route("/")
def get(self, text):
      nlp=stanza.Pipeline('fr')
      doc = nlp(text)
      return doc.entities()

if __name__ == '__main__':
    app.run()
