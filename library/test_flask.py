from flask import Flask
""" set up virtual enviorment"""
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'