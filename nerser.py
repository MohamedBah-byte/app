from flask import Flask
from flask_restful import Api, Resource, reqparse
import stanza
app = Flask(__name__)


@app.route('/ner', methods=['GET'])
def ner():
      nlp=stanza.Pipeline('fr')
      text=request.args.get('text', default = '', type = str)
      doc = nlp(text)
      return doc.entities()
   
if __name__ == '__main__':
    app.run(port=5005, debug=True)
