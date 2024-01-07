from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request, Response

import threading
import random
import time



node_url = "/node2"


app = FastAPI()
app.mount("/static", StaticFiles(directory="./app2/static"), name="static")
#app.mount("/templates", StaticFiles(directory="./app2/templates"), name="templates")
#app_templates = Jinja2Templates(directory="./app2/templates")

@app.get(node_url, response_class=HTMLResponse)
async def training():
    return "<h1>node2</h1>"



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
    
    def get_node_url(self):
        return node_url

    def run(self):
        percentage = self.get_percentage()
        while percentage < 100:
            print(f"node2: {percentage}")
            percentage += random.randint(1, 10)
            self.set_percentage(percentage)
            time.sleep(1)
        percentage = 100
        print(f"node2: {percentage}")
