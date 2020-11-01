import json

from app.nlu.nlu import NLU
from flask import Blueprint, request, jsonify

nlu_bp = Blueprint('nlu', __name__)

# Global variables
_nlu = None

# We define a function here which will be called when the the app is started.
def get_ready(json_name):
    """
    This method will be called only once to setup and train the NLU engine.
    :return:
    """
    global _nlu
    _nlu = NLU(json_name)
    _nlu.train_engine()
    

@nlu_bp.route('/', methods=['GET'])
def main():
    return f'<h1>Whelp NLU</h1>'

@nlu_bp.route('/nlu', methods=['POST'])
def parse_query():
    
    """
    Here we have denied a method which will parse the query which is in natural
    language using the trained nlp engine.
    :return:
    """
    required_output = dict()
    if request.method == "POST":
        post_data = request.get_json()
        print(post_data.get("sentence"))
        result = _nlu.parse_sentence(post_data.get("sentence"))
        required_output['intent'] = result.get('intent')
        required_output['slots'] = result.get('slots')
        return jsonify(required_output)
