import json
import os

ALUMNES_FILE = 'alumnes.json'
alumnes = []
id_actual = 1

# Carrega alumnes del fitxer si existeix
def carregar_alumnes():
    global alumnes, id_actual
    if os.path.exists(ALUMNES_FILE):
        with open(ALUMNES_FILE, 'r') as f:
            alumnes = json.load(f)
            if alumnes:
                id_actual = max(a['id'] for a in alumnes) + 1  # Assegura ID únic

# Desa alumnes al fitxer JSON
def desar_alumnes():
    with open(ALUMNES_FILE, 'w') as f:
        json.dump(alumnes, f, indent=4)

# Mostra ID, nom i cognom de tots els alumnes
def mostrar_alumnes():
    for a in alumnes:
        print(f"{a['id']}: {a['nom']} {a['cognom']}")

# Afegeix un alumne nou amb dades introduïdes per l’usuari
def afegir_alumne():
    global id_actual
    nom = input("Nom: ")
    cognom = input("Cognom: ")
    dia = int(input("Dia naixement: "))
    mes = int(input("Mes naixement: "))
    any = int(input("Any naixement: "))
    email = input("Email: ")
    feina = input("Té feina? (s/n): ").lower() == 's'
    curs = input("Curs: ")

    nou = {
        'id': id_actual,
        'nom': nom,
        'cognom': cognom,
        'data': {'dia': dia, 'mes': mes, 'any': any},
        'email': email,
        'feina': feina,
        'curs': curs
    }

    alumnes.append(nou)
    id_actual += 1
    print("Alumne afegit!")

# Mostra totes les dades d’un alumne per ID
def veure_alumne():
    id_busc = int(input("ID de l'alumne: "))
    alumne = next((a for a in alumnes if a['id'] == id_busc), None)
    if alumne:
        print(json.dumps(alumne, indent=4))
    else:
        print("Alumne no trobat.")

# Esborra un alumne per ID
def esborrar_alumne():
    global alumnes
    id_busc = int(input("ID a esborrar: "))
    alumnes = [a for a in alumnes if a['id'] != id_busc]
    print("Alumne esborrat si existia.")

# Menú principal
carregar_alumnes()
while True:
    print("\n1. Mostrar alumnes\n2. Afegir alumne\n3. Veure alumne\n4. Esborrar alumne\n5. Desar fitxer\n6. Carregar fitxer\n7. Sortir")
    op = input("Opció: ")
    if op == '1':
        mostrar_alumnes()
    elif op == '2':
        afegir_alumne()
    elif op == '3':
        veure_alumne()
    elif op == '4':
        esborrar_alumne()
    elif op == '5':
        desar_alumnes()
    elif op == '6':
        carregar_alumnes()
    elif op == '7':
        break
    else:
        print("Opció no vàlida")

