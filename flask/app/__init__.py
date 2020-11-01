from flask import Flask
from app.views import nlu_bp, get_ready

def create_app():
    app = Flask(__name__)
    get_ready() # Call the get_ready() function from the views.py to get the NLP engine ready. (warmup)
    app.register_blueprint(nlu_bp)
    return app