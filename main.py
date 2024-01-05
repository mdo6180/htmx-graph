import random
from typing import Annotated

from fastapi import FastAPI, APIRouter, Header
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request, Response

from app1.main import app as app1 
from app2.main import app as app2

app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="./templates")

# mount the app1 app at /app1 and the app2 app at /app2
app.mount("/app1", app1)
app.mount("/app2", app2)


json_data = {
    "nodes": [
        { "id": "kspacey", "label": "Kevin Spacey", "width": 144, "height": 100, "endpoint": "/node/kspacey", "progress_endpoint": "/progress/kspacey" },
        { "id": "swilliams", "label": "Saul Williams", "width": 160, "height": 100, "endpoint": "/node/swilliams", "progress_endpoint": "/progress/swilliams" },
        { "id": "bpitt", "label": "Brad Pitt", "width": 108, "height": 100, "endpoint": "/node/bpitt", "progress_endpoint": "/progress/bpitt" },
        { "id": "hford", "label": "Harrison Ford", "width": 168, "height": 100, "endpoint": "/node/hford", "progress_endpoint": "/progress/hford" },
        { "id": "lwilson", "label": "Luke Wilson", "width": 144, "height": 100, "endpoint": "/node/lwilson", "progress_endpoint": "/progress/lwilson" },
        { "id": "kbacon", "label": "Kevin Bacon", "width": 121, "height": 100, "endpoint": "/node/kbacon", "progress_endpoint": "/progress/kbacon" }
    ],
    "edges": [
        {"source": "kspacey", "target": "swilliams", "arrowhead": "vee" },
        {"source": "swilliams", "target": "kbacon", "arrowhead": "vee" },
        {"source": "bpitt", "target": "kbacon", "arrowhead": "vee" },
        {"source": "hford", "target": "lwilson", "arrowhead": "vee" },
        {"source": "lwilson", "target": "kbacon", "arrowhead": "vee" }
    ]
}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("dag.html", {"request": request, "nodes": json_data["nodes"], "json_data": json_data})


@app.get("/node/{node_id}", response_class=HTMLResponse)
async def insert(request: Request, node_id: str):
    for node in json_data["nodes"]:
        if node["id"] == node_id:
            return f"""<p> node clicked: {node["label"]} </p>"""
        
    return "<p> node does not exist </p>"


progress_dict = {
    "kspacey": 0,
    "swilliams": 0,
    "bpitt": 0,
    "hford": 0,
    "lwilson": 0,
    "kbacon": 0
}

@app.get("/progress/{node_id}", response_class=HTMLResponse)
async def progress(request: Request, node_id: str, response: Response):
    global progress_dict

    added_progress = random.randint(1, 5)
    if progress_dict[node_id] + added_progress < 100:
        progress_dict[node_id] += added_progress
        return f"{progress_dict[node_id]}%"
    elif progress_dict[node_id] + added_progress >= 100:
        progress_dict[node_id] = 100
        response.headers["HX-Trigger"] = "done"
        return "100%"
