from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request, Response

import threading
import random
import time



node_url = "/node1"

app = FastAPI()
#app.mount("/static", StaticFiles(directory="./app1/static"), name="static")
#templates = Jinja2Templates(directory="./app1/templates")

@app.get(node_url, response_class=HTMLResponse)
async def preprocessing(request: Request):
    # return templates.TemplateResponse("preprocessing.html", {"request": request, "message": "Preprocessing"})
    return "<h1>node1</h1>"



class Node1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name="Node1", daemon=True)
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
            print(f"node1: {percentage}")
            percentage += random.randint(1, 10)
            self.set_percentage(percentage)
            time.sleep(1)
        percentage = 100
        print(f"node1: {percentage}")


if __name__ == "__main__":
    node1 = Node1()
    node1.start()

    while node1.get_percentage() < 100:
        time.sleep(1)

    node1.join()
