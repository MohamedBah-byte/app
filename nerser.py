from flask import Flask
from flask_restful import Api, Resource, reqparse
import stanza
app = Flask(__name__)
nlp=stanza.Pipeline('fr')

@app.route('/ner', methods=['GET', 'POST', 'PUT'])
def ner():
      text=request.args.get('username')
      doc = nlp(text)
      return doc.entities() 
   
if __name__ == '__main__':
    app.run('')
