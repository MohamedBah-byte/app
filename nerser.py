from flask import Flask
from flask import request
from flask_restful import Api, Resource, reqparse
import stanza
from json2html import *

app = Flask(__name__)

@app.route('/ner', methods=['GET'])
def ner():
      nlp=stanza.Pipeline('fr')
      text=request.args.get('text', default = '', type = str)
      doc = nlp(text)
      result=json2html.convert(json = doc.entities(), table_attributes="id=\"info-table\" class=\"table table-bordered table-hover\"")
      
      return result
   
if __name__ == '__main__':
    app.run(port=5005, debug=True)
