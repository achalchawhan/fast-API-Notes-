from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pymongo import MongoClient
app = FastAPI()

# Mount static files
app.mount("../static", StaticFiles(directory="static"), name="static")

# Initialize Jinja2Templates with the correct directory
templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://aachalchawhan14:aachalchawhan14@cluster1.tfe4z.mongodb.net/")



# Render the index.html page
# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     docs = conn.nodes.nodes.find_one({})
    # docs = conn["nodes_db"]["nodes_collection"].find_one({})

    # print(docs)
    # return templates.TemplateResponse("index.html", {"request": request})

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # docs = conn.node.notes.find_one({})
    # print(docs)
    # or
    # docs = conn.node.notes.find({})
    # for doc in docs:
    #     print(doc)
    #     or

    # docs = conn.node.notes.find({})
    # for doc in docs:
    #     print(doc["_id"])
    # return templates.TemplateResponse("index.html", {"request": request, "docs": docs})

    docs = conn.node.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "note": doc["note"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}




