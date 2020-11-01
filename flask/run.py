"""
Input:
{"sentence": "What will be the weather in Mumbai next week?"}
"""
from app import create_app
import sys

app = create_app()
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True,use_reloader=True)
