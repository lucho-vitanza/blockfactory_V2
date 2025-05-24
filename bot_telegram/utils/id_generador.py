import json
import os

COUNTER_PATH = os.path.join("data", "counters.json")

def generar_id(tipo):
    with open(COUNTER_PATH, "r+") as file:
        counters = json.load(file)
        if tipo not in counters:
            raise ValueError("Tipo inválido")
        counters[tipo] += 1
        file.seek(0)
        json.dump(counters, file, indent=2)
        file.truncate()
        return counters[tipo]
