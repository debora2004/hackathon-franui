import json

if __name__ == '__main__':
    pregunta: dict[str: dict[str, bool]] = json.load(open('preguntas.json', encoding='utf-8'))['preguntas'][0]
    print(pregunta)
