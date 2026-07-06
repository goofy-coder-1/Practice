from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
   return {"Message" : "Hello world"}

@app.get("/items/item_id")
async def read_item():
   return {"Message" : "Aahile lai chahi khali chha hai"}