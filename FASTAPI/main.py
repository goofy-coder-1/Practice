from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/")
async def root():
   return {"Message" : "Hello world"}

@app.get("/item/{item_id}")
async def read_item(item_id: int):
   return {"Item Id" : item_id}

class ModalName(str, Enum):
   hello = "hello"
   lenet = "lenet"
   anything = "anything"

@app.get("/users/{model_name}")
async def get_model(model_name: ModalName):
   if model_name is ModalName.anything:
      return {"Modal name": model_name, "Message": "Wassuppp"}
   
   if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

   return {"model_name": model_name, "message": "Have some residuals"}