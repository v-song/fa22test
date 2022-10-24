from fastapi import FastAPI
from src.test import Adder

app = FastAPI(title ="new project")


@app.get("/")
def home():
    adder = Adder()
    resources = {
        "Title": "Hello 123",
        "Count": adder.count
    }
    return resources