from fastapi import FastAPI, APIRouter
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
        { "id": "kspacey", "label": "Kevin Spacey",  "width": 144, "height": 100, "endpoint": "/node/kspacey" },
        { "id": "swilliams", "label": "Saul Williams", "width": 160, "height": 100, "endpoint": "/node/swilliams" },
        { "id": "bpitt", "label": "Brad Pitt",     "width": 108, "height": 100, "endpoint": "/node/bpitt" },
        { "id": "hford", "label": "Harrison Ford", "width": 168, "height": 100, "endpoint": "/node/hford" },
        { "id": "lwilson", "label": "Luke Wilson",   "width": 144, "height": 100, "endpoint": "/node/lwilson" },
        { "id": "kbacon", "label": "Kevin Bacon",   "width": 121, "height": 100, "endpoint": "/node/kbacon" }
    ],
    "edges": [
        {"source": "kspacey", "target": "swilliams", "arrowhead": "vee" },
        {"source": "swilliams", "target": "kbacon", "arrowhead": "vee" },
        {"source": "bpitt", "target": "kbacon", "arrowhead": "vee" },
        {"source": "hford", "target": "lwilson", "arrowhead": "vee" },
        {"source": "lwilson", "target": "kbacon", "arrowhead": "vee" }
    ]
}


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    nodes = [
        {"name": "preprocessing", "endpoint": "/app1"},
        {"name": "training", "endpoint": "/app2"},
        {"name": "evaluation", "endpoint": "/evaluation"},
    ]
    return templates.TemplateResponse("base.html", {"request": request, "nodes": nodes, "title": "Anacostia Pipeline"})


@app.get("/directed_graph", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "json_data": json_data, "title": "Anacostia Pipeline"})


@app.get("/node/{node_id}", response_class=HTMLResponse)
async def insert(request: Request, node_id: str):
    for node in json_data["nodes"]:
        if node["id"] == node_id:
            return f"""<p> node clicked: {node["label"]} </p>"""
        
    return "<p> node does not exist </p>"