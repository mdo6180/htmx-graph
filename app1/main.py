from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request, Response


app = FastAPI()
app.mount("/static", StaticFiles(directory="./app1/static"), name="static")
templates = Jinja2Templates(directory="./app1/templates")


@app.get("/", response_class=HTMLResponse)
async def preprocessing(request: Request):
    return templates.TemplateResponse("preprocessing.html", {"request": request, "message": "Preprocessing"})
