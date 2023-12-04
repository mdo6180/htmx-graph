from flask import Flask, render_template
import requests
import time


app = Flask(__name__)

@app.route("/visjs")
def vis_js():
    json_data = [
        { "id": 1, "label": "Node 1", "title": "I have a popup!", "widthConstraint": { "minimum": 80 } },
        { "id": 2, "label": "Node 2", "title": "I have a popup!", "heightConstraint": {"minimum": 60, "valign": "top"}, "shape": "circle"},
        { "id": 3, "label": "Node 3", "title": "I have a popup!" },
        { "id": 4, "label": "Node 4", "title": "I have a popup!" },
        { "id": 5, "label": "Node 5", "title": "I have a popup!" },
    ]
    return render_template("visjs.html", json_data=json_data)


@app.route("/d3")
def d3():
    json_data = {
        "nodes": [
            {"id": 1, "name": "A", "label": "<h3>Node A</h3><p>HTML content for Node A</p>"},
            {"id": 2, "name": "B", "label": "<h3>Node B</h3><p>HTML content for Node B</p>"},
            {"id": 3, "name": "C"},
            {"id": 4, "name": "D"},
            {"id": 5, "name": "E"},
            {"id": 6, "name": "F"},
            {"id": 7, "name": "G"},
            {"id": 8, "name": "H"},
            {"id": 9, "name": "I"},
            {"id": 10, "name": "J"}
        ],
        "links": [
            {"source": 1, "target": 2},
            {"source": 1, "target": 5},
            {"source": 1, "target": 6},
            {"source": 2, "target": 3},
            {"source": 2, "target": 7},
            {"source": 3, "target": 4},
            {"source": 8, "target": 3},
            {"source": 4, "target": 5},
            {"source": 4, "target": 9},
            {"source": 5, "target": 10},
        ]
    }
    return render_template("d3.html", json_data=json_data)


@app.route("/d3_practice")
def d3_practice():
    json_data = {
        "nodes": [
            {"id": 1, "name": "A", "label": "<h3>Node A</h3><p>HTML content for Node A</p>"},
            {"id": 2, "name": "B", "label": "<h3>Node B</h3><p>HTML content for Node B</p>"},
            {"id": 3, "name": "C", "label": "<h3>Node C</h3><p>HTML content for Node C</p>"},
            {"id": 4, "name": "D", "label": "<h3>Node D</h3><p>HTML content for Node D</p>"},
            {"id": 5, "name": "E", "label": "<h3>Node E</h3><p>HTML content for Node E</p>"},
            {"id": 6, "name": "F", "label": "<h3>Node F</h3><p>HTML content for Node F</p>"},
            {"id": 7, "name": "G", "label": "<h3>Node G</h3><p>HTML content for Node G</p>"},
            {"id": 8, "name": "H", "label": "<h3>Node H</h3><p>HTML content for Node H</p>"},
            {"id": 9, "name": "I", "label": "<h3>Node I</h3><p>HTML content for Node I</p>"},
            {"id": 10, "name": "J", "label": "<h3>Node J</h3><p>HTML content for Node J</p>"}
        ],
        "links": [
            {"source": 1, "target": 2},
            {"source": 1, "target": 5},
            {"source": 1, "target": 6},
            {"source": 2, "target": 3},
            {"source": 2, "target": 7},
            {"source": 3, "target": 4},
            {"source": 8, "target": 3},
            {"source": 4, "target": 5},
            {"source": 4, "target": 9},
            {"source": 5, "target": 10},
        ]
    } 
    return render_template("d3_practice.html", json_data=json_data)


@app.route("/home")
def home():
    nodes = [
        {"name": "preprocessing", "endpoint": "/preprocessing"},
        {"name": "training", "endpoint": "/training"},
        {"name": "evaluation", "endpoint": "/evaluation"},
    ]
    return render_template("home.html", nodes=nodes, title="Anacostia")

@app.route("/preprocessing")
def preprocessing():
    return "<h1>preprocessing</h1>"

@app.route("/training")
def training():
    return "<h1>training</h1>"

@app.route("/evaluation")
def evaluation():
    return "<h1>evaluation</h1>"