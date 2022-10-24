from fastapi import FastAPI

app = FastAPI(title ="new project")


@app.get("/")
def home():
    resources = {
        "Title": "Hello 123"
    }
    return resources