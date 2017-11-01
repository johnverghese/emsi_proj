from flask import Flask
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, World!"

def query_data():
    f = open('sample_response.txt', 'r')
    response = f.read()
    response = response.replace('\n', '')
    data = json.loads(response)
    print(data)

query_data()
