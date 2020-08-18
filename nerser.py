from flask import Flask
from flask import request
from flask_restful import Api, Resource, reqparse
import stanza
import json
from io import StringIO 
import sys


app = Flask(__name__)


@app.route('/ner', methods=['GET', 'POST'])
def ner():
      stanza.download('fr')
      nlp=stanza.Pipeline('fr')
      text=request.args.get('text')
      doc = nlp(text)
      return str(doc.entities).strip('[]')

if __name__ == '__main__':
    app.run(port=5005, debug=True)
