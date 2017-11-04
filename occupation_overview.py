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
    return render_template('occ_overview.html', occupation=data['occupation'], summary=data['summary'],
                            region=data['region'], trend_comparison=data['trend_comparison'],
                            employing_industries=data['employing_industries'])

@app.route('/data.tsv')
def data():
    f = open('data.tsv', 'r')
    response = f.read()
    return response

@app.route('/table')
def table_template():
    data = query_data()
    return render_template('table.html',
        trend_comparison=data['trend_comparison'])


def query_data():
    f = open('sample_response.txt', 'r')
    response = f.read()
    response = response.replace('\n', '')
    data = json.loads(response)
    return data

