import json

# Definim la classe Alumne per gestionar la informació dels alumnes
class Alumne:
    def __init__(self, id, nom, cognom, dia, mes, any, email, feina, curs):
        self.id = id
        self.nom = nom
        self.cognom = cognom
        self.data = {
            "dia": dia,
            "mes": mes,
            "any": any
        }
        self.email = email
        self.feina = feina
        self.curs = curs

    # Mètode per convertir l'objecte Alumne en un diccionari per ser desat en JSON
    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "cognom": self.cognom,
            "data": self.data,
            "email": self.email,
            "feina": self.feina,
            "curs": self.curs
        }

    @classmethod
    def from_dict(cls, data):
        # Mètode per crear un alumne a partir d'un diccionari (de JSON)
        return cls(
            data['id'],
            data['nom'],
            data['cognom'],
            data['data']['dia'],
            data['data']['mes'],
            data['data']['any'],
            data['email'],
            data['feina'],
            data['curs']
        )

# Funció per llegir el fitxer JSON i carregar la llista d'alumnes
def llegir_fitxer():
    try:
        with open('alumnes.json', 'r') as f:
            alumnes_data = json.load(f)
            return [Alumne.from_dict(alumne) for alumne in alumnes_data]
    except FileNotFoundError:
        return []

# Funció per desar la llista d'alumnes al fitxer JSON
def desar_fitxer(alumnes):
    with open('alumnes.json', 'w') as f:
        json.dump([alumne.to_dict() for alumne in alumnes], f, indent=4)

# Funció per afegir un alumne
def afegir_alumne(alumnes, nom, cognom, dia, mes, any, email, feina, curs):
    # Determinem l'ID de l'alumne (l'ID serà l'últim ID + 1)
    if alumnes:
        nou_id = max([alumne.id for alumne in alumnes]) + 1
    else:
        nou_id = 1

    alumne = Alumne(nou_id, nom, cognom, dia, mes, any, email, feina, curs)
    alumnes.append(alumne)
    return alumnes

# Funció per veure els detalls d'un alumne a partir del seu ID
def veure_alumne(alumnes, id):
    for alumne in alumnes:
        if alumne.id == id:
            return alumne
    return None

# Funció per esborrar un alumne a partir del seu ID
def esborrar_alumne(alumnes, id):
    alumnes = [alumne for alumne in alumnes if alumne.id != id]
    return alumnes

# Funció per mostrar el llistat d'alumnes
def mostrar_llistat(alumnes):
    for alumne in alumnes:
        print(f"ID: {alumne.id} - Nom: {alumne.nom} - Cognom: {alumne.cognom}")

# Interfície d'usuari interactiva
def main():
    alumnes = llegir_fitxer()

    while True:
        print("\nGestió d'alumnes")
        print("1. Mostrar tots els alumnes")
        print("2. Afegir un alumne")
        print("3. Veure un alumne")
        print("4. Esborrar un alumne")
        print("5. Desar a fitxer")
        print("6. Llegir fitxer")
        print("7. Sortir")
        opcio = input("Selecciona una opció: ")

        if opcio == '1':
            mostrar_llistat(alumnes)
        elif opcio == '2':
            nom = input("Nom: ")
            cognom = input("Cognom: ")
            dia = int(input("Dia de naixement: "))
            mes = int(input("Mes de naixement: "))
            any = int(input("Any de naixement: "))
            email = input("Email: ")
            feina = input("Treballa? (True/False): ") == 'True'
            curs = input("Curs: ")
            alumnes = afegir_alumne(alumnes, nom, cognom, dia, mes, any, email, feina, curs)
            desar_fitxer(alumnes)
        elif opcio == '3':
            id = int(input("Introdueix l'ID de l'alumne: "))
            alumne = veure_alumne(alumnes, id)
            if alumne:
                print(f"\nID: {alumne.id}\nNom: {alumne.nom}\nCognom: {alumne.cognom}")
                print(f"Data de naixement: {alumne.data['dia']}/{alumne.data['mes']}/{alumne.data['any']}")
                print(f"Email: {alumne.email}\nFeina: {alumne.feina}\nCurs: {alumne.curs}")
            else:
                print("Alumne no trobat.")
        elif opcio == '4':
            id = int(input("Introdueix l'ID de l'alumne a esborrar: "))
            alumnes = esborrar_alumne(alumnes, id)
            desar_fitxer(alumnes)
        elif opcio == '5':
            desar_fitxer(alumnes)
            print("Dades desades correctament.")
        elif opcio == '6':
            alumnes = llegir_fitxer()
            print("Dades llegides correctament.")
        elif opcio == '7':
            break
        else:
            print("Opció no vàlida.")

if __name__ == "__main__":
    main()
