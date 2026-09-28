from fastapi import FastAPI
from enum import Enum

app=FastAPI()


@app.get("/items/{item_id}")
async def get_item(item_id:int):
    if item_id==90:
        return "Hello Sujeeth"
    return {"item_id":item_id}

fake_items=["oranges","apples","banana","pineapple"]

@app.get("/fakeItems/{start}to{end}")
async def get_fakeItems(start:int, end:int):
    return fake_items[start:end]
