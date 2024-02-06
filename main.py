import random
from typing import Annotated

from fastapi import FastAPI, APIRouter, Header
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request, Response
from fastapi.responses import StreamingResponse
import asyncio

from whitehouse.default import *
from whitehouse.utils import format_html
from component_templates import IndexTemplate

from app1.main import Node1
from app2.main import Node2



app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="./templates")

node1 = Node1()
node2 = Node2()

# mount the app1 app at /app1 and the app2 app at /app2
app.mount("/node1", node1.get_app())
app.mount("/node2", node2.get_app())


json_data = {
    "nodes": [
        { "id": "kspacey", "label": "Kevin Spacey", "width": 144, "height": 100, "endpoint": "/node/kspacey", "progress_endpoint": "/progress/kspacey", },
        { "id": "swilliams", "label": "Saul Williams", "width": 160, "height": 100, "endpoint": "/node/swilliams", "progress_endpoint": "/progress/swilliams" },
        { "id": "bpitt", "label": "Brad Pitt", "width": 108, "height": 100, "endpoint": "/node/bpitt", "progress_endpoint": "/progress/bpitt" },
        { "id": "hford", "label": "Harrison Ford", "width": 168, "height": 100, "endpoint": "/node/hford", "progress_endpoint": "/progress/hford" },
        { "id": "lwilson", "label": "Luke Wilson", "width": 144, "height": 100, "endpoint": "/node/lwilson", "progress_endpoint": "/progress/lwilson" },
        { "id": "kbacon", "label": "Kevin Bacon", "width": 121, "height": 100, "endpoint": "/node/kbacon", "progress_endpoint": "/progress/kbacon" }
    ],
    "edges": [
        {"source": "kspacey", "target": "swilliams", "arrowhead": "vee", "endpoint": "/edge/?source=kspacey&target=swilliams" },
        {"source": "swilliams", "target": "kbacon", "arrowhead": "vee", "endpoint": "/edge/?source=swilliams&target=kbacon" },
        {"source": "bpitt", "target": "kbacon", "arrowhead": "vee", "endpoint": "/edge/?source=bpitt&target=kbacon" },
        {"source": "hford", "target": "lwilson", "arrowhead": "vee", "endpoint": "/edge/?source=hford&target=lwilson" },
        {"source": "lwilson", "target": "kbacon", "arrowhead": "vee", "endpoint": "/edge/?source=lwilson&target=kbacon" }
    ]
}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    #return templates.TemplateResponse("dag.html", {"request": request, "nodes": json_data["nodes"], "json_data": json_data})
    return format_html(
        IndexTemplate(
            [
                div([
                        svg("<g/>", {"width": "960", "height": "600"}),
                        section(
                            p("Potomac AI Inc.")
                        )
                    ], {"id": "graph"}),
                script("", {"src": "/static/js/dag.js", "graph-data": json_data}),
            ],
            json_data
        )
    )


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

    elif progress_dict[node_id] + added_progress >= 100:
        progress_dict[node_id] = 100
    
    if node_id == "bpitt":
        return "done!" if progress_dict["bpitt"] == 100 else "waiting..."

    return f"{progress_dict[node_id]}%"
        

@app.get("/edge/", response_class=HTMLResponse)
async def edge(request: Request, source: str, target: str):
    async def event_stream():
        while True:
            try:
                if progress_dict[source] == 100:
                    yield "event: done\n"
                    yield f"data: red\n\n"
                await asyncio.sleep(0.2)
            except asyncio.CancelledError:
                yield "event: close\n"
                yield f"data: edge sse closed: {source} -> {target}\n\n"
                print(f"closing edge sse: {source} -> {target}")
                break
    return StreamingResponse(event_stream(), media_type="text/event-stream")