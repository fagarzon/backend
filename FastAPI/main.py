
#https://fastapi.tiangolo.com/es/
#pip install "fastapi[all]"

from fastapi import FastAPI

app = FastAPI()

@app.get("/")    
async def root():
    return "hola FastAPI!"
    
# http://127.0.0.1:8000

@app.get("/url")    
async def url():
    return {"url_curso":"http://mouredev.com"}

# uvicorn main:app --reload
# ctrl c
# doc swagger: http://127.0.0.1:8000/docs
# doc redocly: http://127.0.0.1:8000/redoc

# pruebas: postman cliente ejecutar peticiones a un api
#

