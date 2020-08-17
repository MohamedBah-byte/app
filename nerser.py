from flask import Flask
from flask_restful import Api, Resource, reqparse
import stanza
app = Flask(__name__)
nlp=stanza.Pipeline('fr')

@app.route('/ner', methods=['GET'])
def ner():
      text=request.args.get('text')
      doc = nlp(text)
      return doc.entities() 
   
if __name__ == '__main__':
    app.run(port=5005, debug=True)
