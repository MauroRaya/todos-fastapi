from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/')
async def get(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "message": "testando"
    })


if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=80)