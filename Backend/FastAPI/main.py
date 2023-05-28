from fastapi import FastAPI
from routers import players

app= FastAPI()

app.include_router(players.router)

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