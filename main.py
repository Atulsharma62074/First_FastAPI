from fastapi import FastAPI

app = FastAPI()

@app.get("/")
# async 
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def read_item():
    return {"item_id": "Foo Bar"}