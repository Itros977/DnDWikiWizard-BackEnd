from fastapi import FastAPI
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
@app.get("/playerquery/")
async def player(id: int):
    return search_player(id)
    
def search_player(id: int):
    players = filter(lambda player: player.id == id, jugadores_list)
    try:
        return list(players)[0]
    except:
        return {"Error": "No existe actualmente un elemento con esa id "}

#Post de un usuario
@app.post("/newplayer/")
async def player(player: Jugador):
    if type(search_player(player.id)) == Jugador:
        return {"Error": "El usuario ya existe "}
    else:    
        jugadores_list.append(player)
        
@app.put("/modifyplayer/")
async def player(player: Jugador):
    
    found = False
    
    for index, saved_players in enumerate(jugadores_list):
        if saved_players.id == player.id:
            jugadores_list[index] = player
            found = True
    if not found:
        return {"Error": "No existe el usuario al actualizar "} 