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