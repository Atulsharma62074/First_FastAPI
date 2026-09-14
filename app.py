from fastapi import FastAPI

app = FastAPI()

@app.get("/atul")
# async 
def read_root():
    return {"Hello": "Atul"}
