import json

# Alguns exemplos de dados de faturamento
data = '''
[
    {"dia": 1, "valor": 200.0},
    {"dia": 2, "valor": 470.4},
    {"dia": 3, "valor": 0},
    {"dia": 4, "valor": 350.0},
    {"dia": 5, "valor": 200.0}
]
'''

faturamento = json.loads(data)

# Filtrando dias com faturamento
valores = [item["valor"] for item in faturamento if item["valor"] > 0]
menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_media = len([v for v in valores if v > media_mensal])

print("Menor valor de faturamento:", menor_valor)
print("Maior valor de faturamento:", maior_valor)
print("Dias com faturamento acima da média:", dias_acima_media)
 