from fastapi import APIRouter
from models.alumno import Alumno

router = APIRouter()
alumnos = []

#Servicio para obtener todos los alumnos
@router.get('/getAll')
def getAll():
    return alumnos

#Servicio para insertar un alumno
@router.post('/insert')
def insert(alumno:Alumno):
    alumnos.append(dict(alumno))
    response={
        "status":"Alumno insertado"
    }
    return response

#Servicio para consultar alumnos por matricula
@router.get('/getOne/{matricula}')
def getOne(matricula):
    #Aqui va el codigo para buscar un alumno en la lista
    return "Hola"