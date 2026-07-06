from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
   return {"Message" : "Hello world"}

@app.get("/item/{item_id}")
async def read_item(item_id):
   return {"Item Id" : item_id}