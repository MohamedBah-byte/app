from flask import Flask
from flask import request
from flask_restful import Api, Resource, reqparse
import stanza
import json



app = Flask(__name__)


@app.route('/ner', methods=['GET', 'POST'])
def ner():
      
      nlp=stanza.Pipeline('fr')
      text=request.args.get('text')
      doc = nlp(text)
      return str(doc.entities).strip('[]')

if __name__ == '__main__':
    stanza.download('fr')
    app.run(port=5005, debug=True)
