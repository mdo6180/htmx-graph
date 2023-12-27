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