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
      old_stdout = sys.stdout
      result = StringIO()
      sys.stdout = result
      nlp=stanza.Pipeline('fr')
      
      return request.query_string

if __name__ == '__main__':
    app.run(port=5005, debug=True)
