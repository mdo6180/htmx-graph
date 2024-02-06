from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request, Response

from whitehouse.default import *
from whitehouse.utils import format_html

import threading
import random
import time



app = FastAPI()
app.mount("/static", StaticFiles(directory="./app2/static"), name="static")
#app.mount("/templates", StaticFiles(directory="./app2/templates"), name="templates")
#app_templates = Jinja2Templates(directory="./app2/templates")

@app.get("/header", response_class=HTMLResponse)
async def training():
    return format_html(
        html([
            head([
                title("Node2"),
                link({"rel": "stylesheet", "type": "text/css", "href": "/node2/static/css/app2.css"})
            ]),
            body([
                h1("node2", {"id": "app2"})
            ])
        ])
    )



class Node2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name="Node2", daemon=True)
        self.percentage = 0
        self.lock = threading.Lock()
    
    def get_percentage(self):
        while True:
            with self.lock:
                return self.percentage
    
    def set_percentage(self, percentage):
        while True:
            with self.lock:
                self.percentage = percentage
                return
    
    def get_app(self):
        return app
    
    def get_header(self):
        return link({"rel": "stylesheet", "type": "text/css", "href": "/node2/static/css/app2.css"})
    
    def run(self):
        percentage = self.get_percentage()
        while percentage < 100:
            print(f"node2: {percentage}")
            percentage += random.randint(1, 10)
            self.set_percentage(percentage)
            time.sleep(1)
        percentage = 100
        print(f"node2: {percentage}")
