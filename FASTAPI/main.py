from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello! My first API is running."}

@app.get("/predict")
def predict(value: float):
    # In the future,
    result = value * 2
    return {"input": value, "prediction": result}
