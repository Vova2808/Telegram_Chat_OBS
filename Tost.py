from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn
import json

app = FastAPI()
messages = []


@app.get("/", response_class=HTMLResponse)
async def root():
    return HTMLResponse(open("index.html", encoding="utf-8").read())


@app.post("/get-messages")
async def get_messages(request: Request):
    data = await request.json()
    if data:
        d = json.loads(data)
        messages.append({"message": d["message"], "name": d["name"]})
        return True
    return False


@app.get("/get-message")
async def get_message(request: Request):
    if messages:
        return {**messages.pop(0)}
    return None


if __name__ == "__main__":
    uvicorn.run(app)