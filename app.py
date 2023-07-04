from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class Alumno(BaseModel):
    matricula:str
    nombre:str
    apellidos:str
    promedio:float
    cuatrimestre:int




@app.get("/")
def saludar():
    response = {
        "status": "Peticion por get recibida..."
    }
    return response

@app.post("/")
def insertAny(alumno:Alumno):
    print(dict(alumno))
    response={
        "status":"Peticion por post recibida..."
    }
    return response

@app.delete("/")
def delete() :
    response={
        "status":"Peticion por delete recibida..."
    }
    return response

@app.put("/")
def put() :
    response={
        "status":"Peticion por put recibida..."
    }
    return response