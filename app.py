from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def saludar():
    response = {
        "status": "Peticion por get recibida..."
    }
    return response

@app.post("/")
def insertAny() :
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