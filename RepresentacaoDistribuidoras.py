
faturamento = [{
"estado": "SP","valor" :  67836.43},
{"estado":"RJ", "valor": 36678.66},
{"estado": "MG", "valor" : 29229.88},
{"estado": "ES", "valor" : 27165.48},
{"estado":"OUTROS", "valor": 19849.53}
]
total = 0
total = sum([dado['valor'] for dado in faturamento])


for dado in faturamento:
    percentual = round(((dado["valor"]/ total)*100),2)
    dado['percentual'] = percentual

for dado in faturamento:
    print(f"{dado['estado']}: {dado['percentual']} %")