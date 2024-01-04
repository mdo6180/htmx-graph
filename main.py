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
        {"id": 1, "name": "A"}, {"id": 2, "name": "B"},
        {"id": 3, "name": "C"}, {"id": 4, "name": "D"},
        {"id": 5, "name": "E"}, {"id": 6, "name": "F"},
        {"id": 7, "name": "G"}, {"id": 8, "name": "H"},
        {"id": 9, "name": "I"}, {"id": 10, "name": "J"}
    ],
    "links": [
        {"source": 1, "target": 2}, {"source": 3, "target": 2}, 
        {"source": 4, "target": 5}, {"source": 6, "target": 5},
        {"source": 7, "target": 8}, {"source": 9, "target": 8}, 
        {"source": 10, "target": 8}, {"source": 4, "target": 8},
        {"source": 5, "target": 9}, {"source": 2, "target": 6}
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

@app.get("/node/{node_name}", response_class=HTMLResponse)
async def insert(request: Request, node_name: str):
    return f"""
    <div>
        <p> node clicked: {node_name.replace("_", " ")} </p>
    </div>
    """