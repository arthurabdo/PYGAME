import json

with open('score.json', 'r') as arquivo_json:
    texto = arquivo_json.read()

# Criando um dicionário a partir das informações no texto
dicionario = json.loads(texto)
print(dicionario)
print(texto)