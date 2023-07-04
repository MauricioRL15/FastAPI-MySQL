from pydantic import BaseModel

class Alumno(BaseModel):
    matricula:str
    nombre:str
    apellidos:str
    promedio:float
    cuatrimestre:int

