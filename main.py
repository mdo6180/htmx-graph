from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request, Response


app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="./templates")

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    nodes = [
        {"name": "preprocessing", "endpoint": "/preprocessing"},
        {"name": "training", "endpoint": "/training"},
        {"name": "evaluation", "endpoint": "/evaluation"},
    ]
    return templates.TemplateResponse("base.html", {"request": request, "nodes": nodes, "title": "Anacostia Pipeline"})

@app.get("/preprocessing", response_class=HTMLResponse)
async def preprocessing():
    return "<h1>preprocessing</h1>"

@app.get("/training", response_class=HTMLResponse)
async def training():
    return "<h1>training</h1>"

@app.get("/evaluation", response_class=HTMLResponse)
async def evaluation():
    return "<h1>evaluation</h1>"