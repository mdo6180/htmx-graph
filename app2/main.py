from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request, Response


app = FastAPI()
app.mount("/static", StaticFiles(directory="./app2/static"), name="static")
app_templates = Jinja2Templates(directory="./app2/templates")

@app.get("/", response_class=HTMLResponse)
async def training():
    return "<h1>training</h1>"
