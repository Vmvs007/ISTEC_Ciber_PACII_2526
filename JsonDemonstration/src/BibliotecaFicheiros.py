import json

def readFile(path):
    with open(path) as ficheiro:
        data = json.load(ficheiro)

    return data


def saveFile(path, data):
    with open(path, 'w', encoding='utf-8') as ficheiroGuardado:
        json.dump(data, ficheiroGuardado, indent=4)
