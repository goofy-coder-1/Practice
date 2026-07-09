from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "car"}, {"item_name": "barcelona"}, {"item_name": "Dahi"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/calculate")
async def calculator(a: int, b: int, op: str):
    match op:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b
        case '/':
            if b == 0:
                return {"error": "Cannot divide by zero"}
            result = a / b
        case _:
            return {"Error": "Invalid operation"}
            
    return {"result": result}

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing thing that has a long description"}
        )
    return item