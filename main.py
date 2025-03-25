from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# Definim el model d'alumne
class Alumne(BaseModel):
    id: int
    nom: str
    cognom: str
    data: dict
    email: str
    feina: bool
    curs: str

# Llegir dades d'alumnes des del fitxer JSON
def llegir_dades():
    with open("alumnes.json", "r") as f:
        return json.load(f)

# Endpoint per mostrar la informació bàsica de l'institut
@app.get("/")
def root():
    return {"message": "Institut TIC de Barcelona"}

# Endpoint per obtenir el número total d'alumnes
@app.get("/alumnes/")
def obtenir_total_alumnes():
    alumnes = llegir_dades()
    return {"total_alumnes": len(alumnes)}

# Endpoint per obtenir la informació d'un alumne per ID
@app.get("/id/{id}")
def obtenir_alumne(id: int):
    alumnes = llegir_dades()
    for alumne in alumnes:
        if alumne['id'] == id:
            return alumne
    return {"error": "Alumne no trobat"}

# Endpoint per eliminar un alumne per ID
@app.delete("/del/{id}")
def eliminar_alumne(id: int):
    alumnes = llegir_dades()
    alumnes = [alumne for alumne in alumnes if alumne['id'] != id]
    with open('alumnes.json', 'w') as f:
        json.dump(alumnes, f, indent=4)
    return {"message": "Alumne esborrat"}

# Endpoint per afegir un alumne
@app.post("/alumne/")
def afegir_alumne(alumne: Alumne):
    alumnes = llegir_dades()
    alumnes.append(alumne.dict())
    with open('alumnes.json', 'w') as f:
        json.dump(alumnes, f, indent=4)
    return alumne
