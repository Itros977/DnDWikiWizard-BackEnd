from fastapi import FastAPI

app= FastAPI()

@app.get("/")
async def root():
    return "Hola FastAPI, estamos desplegados en casita"

#Iniciar el servior 

#Documentacion en swagger localhost/docs
#Documentacion en swagger localhost/redoc

#Get leer datos
#Post crear datos
#Put actaulizar datos
#delete borrar datos