from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

ALUMNES_FILE = 'alumnes.json'
alumnes = []
id_actual = 1

# Carrega les dades del fitxer JSON si existeix
if os.path.exists(ALUMNES_FILE):
    with open(ALUMNES_FILE, 'r') as f:
        alumnes = json.load(f)
        if alumnes:
            id_actual = max(a['id'] for a in alumnes) + 1  # ID únic per al següent alumne

# Models per validar les dades d’entrada amb Pydantic
class Data(BaseModel):
    dia: int
    mes: int
    any: int

class Alumne(BaseModel):
    nom: str
    cognom: str
    data: Data
    email: str
    feina: bool
    curs: str

# Ruta principal
@app.get("/")
def read_root():
    return "Institut TIC de Barcelona"

# Retorna el nombre total d’alumnes
@app.get("/alumnes/")
def get_total():
    return {"total": len(alumnes)}

# Retorna un alumne pel seu ID
@app.get("/id/{numero}")
def get_alumne(numero: int):
    alumne = next((a for a in alumnes if a['id'] == numero), None)
    if not alumne:
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    return alumne

# Elimina un alumne pel seu ID
@app.delete("/del/{numero}")
def delete_alumne(numero: int):
    global alumnes
    alumnes = [a for a in alumnes if a['id'] != numero]
    with open(ALUMNES_FILE, 'w') as f:
        json.dump(alumnes, f, indent=4)
    return {"status": "Alumne esborrat"}

# Afegeix un alumne nou
@app.post("/alumne/")
def add_alumne(alumne: Alumne):
    global id_actual
    nou = alumne.dict()
    nou['id'] = id_actual
    alumnes.append(nou)
    id_actual += 1
    with open(ALUMNES_FILE, 'w') as f:
        json.dump(alumnes, f, indent=4)
    return {"status": "Alumne afegit", "id": nou['id']}

