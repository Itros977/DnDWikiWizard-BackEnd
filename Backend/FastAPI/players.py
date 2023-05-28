from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app= FastAPI()

#levantar server uvicorn main:app --reload

class Jugador(BaseModel):
    id: int
    nombre: str
    raza: str
    rol: str
    rutaFoto: str
    hp: int
    mana: int
    xp:int
    nivel:int
    
jugadores_list = [Jugador(id=1,nombre="Gimli",raza="Enano",rol="Tanque",rutaFoto="",hp=18,mana=15,xp=12,nivel=8),
                  Jugador(id=2,nombre="Aragorn",raza="Humano",rol="Luchador",rutaFoto="",hp=18,mana=15,xp=12,nivel=8),
                  Jugador(id=3,nombre="Legolas",raza="Elfo",rol="Ranger",rutaFoto="",hp=18,mana=15,xp=12,nivel=8),
                  Jugador(id=4,nombre="Gandalf",raza="Istari",rol="Mago",rutaFoto="",hp=18,mana=15,xp=12,nivel=8)]

@app.get("/players")
async def root():
    return "Hola FastAPI, estamos desplegados en casita, en la parte de jugadores"

@app.get("/playerslist")
async def userlist():
    return jugadores_list

#Path
@app.get("/player/{id}")
async def player(id: int):
    return search_player(id)
    
#Query
@app.get("/playerquery/", status_code=201)
async def player(id: int):
    return search_player(id)
    
def search_player(id: int):
    players = filter(lambda player: player.id == id, jugadores_list)
    try:
        return list(players)[0]
    except:
        raise HTTPException(status_code=404)

#Post de un usuario
@app.post("/player/", status_code=201)
async def player(player: Jugador):
    if type(search_player(player.id)) == Jugador:
        raise HTTPException(status_code=204)
        
    jugadores_list.append(player)
    return player
        
@app.put("/modifyplayer/")
async def player(player: Jugador):
    
    found = False
    
    for index, saved_players in enumerate(jugadores_list):
        if saved_players.id == player.id:
            jugadores_list[index] = player
            found = True
    if not found:
        return {"Error": "No existe el usuario al actualizar "}
    else:
        return player

#Delete de un usuario
@app.delete("/player/{id}")
async def player(id: int):
    
    found = False
    
    for index, saved_players in enumerate(jugadores_list):
        if saved_players.id == id:
            del jugadores_list[index]
            found = True
    if not found:
        return {"Error": "No existe el usuario a eliminar "}