from flask import Flask
from flask import request
from flask_restful import Api, Resource, reqparse
import stanza
import json

app = Flask(__name__)

@app.route('/ner', methods=['GET'])
def ner():
      nlp=stanza.Pipeline('fr')
      text=request.args.get('text', default = '', type = str)
      doc = nlp(text)
      return print(*[f'entity: {ent.text}\ttype: {ent.type}' for sent in doc.sentences for ent in sent.ents], sep='\n')

if __name__ == '__main__':
    app.run(port=5005, debug=True)
