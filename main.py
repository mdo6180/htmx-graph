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



@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    nodes = [
        {"name": "preprocessing", "endpoint": "/app1"},
        {"name": "training", "endpoint": "/app2"},
        {"name": "evaluation", "endpoint": "/evaluation"},
    ]
    return templates.TemplateResponse("base.html", {"request": request, "nodes": nodes, "title": "Anacostia Pipeline"})

@app.get("/evaluation", response_class=HTMLResponse)
async def evaluation():
    return "<h1>evaluation</h1>"

@app.get("/d3", response_class=HTMLResponse)
async def d3(request: Request):
    json_data = {
        "nodes": [
            {
                "id": 1,
                "name": "A"
            },
            {
                "id": 2,
                "name": "B"
            },
            {
                "id": 3,
                "name": "C"
            },
            {
                "id": 4,
                "name": "D"
            },
            {
                "id": 5,
                "name": "E"
            },
            {
                "id": 6,
                "name": "F"
            },
            {
                "id": 7,
                "name": "G"
            },
            {
                "id": 8,
                "name": "H"
            },
            {
                "id": 9,
                "name": "I"
            },
            {
                "id": 10,
                "name": "J"
            }
        ],
        "links": [
            {
                "source": 1,
                "target": 2
            },
            {
                "source": 1,
                "target": 5
            },
            {
                "source": 1,
                "target": 6
            },

            {
                "source": 2,
                "target": 3
            },
            {
                "source": 2,
                "target": 7
            },
            {
                "source": 3,
                "target": 4
            },
            {
                "source": 8,
                "target": 3
            },
            {
                "source": 4,
                "target": 5
            },
            {
                "source": 4,
                "target": 9
            },
            {
                "source": 5,
                "target": 10
            }
        ]
    }
    return templates.TemplateResponse("d3_practice.html", {"request": request, "json_data": json_data, "title": "D3 Practice"})