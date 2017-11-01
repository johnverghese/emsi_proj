from flask import Flask, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
import json
app = Flask(__name__)

# TODO:
#link to environment to use
from add_spaces import add_spaces

@app.route('/')
def occ_overview():
    data = query_data()
    return render_template('occ_overview.html', occupation=data['occupation'])

def query_data():
    f = open('sample_response.txt', 'r')
    response = f.read()
    response = response.replace('\n', '')
    data = json.loads(response)
    return data

print(query_data())
