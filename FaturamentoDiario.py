import json

def ordenacao(lista):
    if len(lista) <= 1:
        return lista
    
    pivo = lista.pop()
    
    valores_maiores = []
    valores_menores = []
    for valor in lista:
        if valor == 0.0:
            continue
        elif valor > pivo:
            valores_maiores.append(valor)
        else:
            valores_menores.append(valor)
    
    return ordenacao(valores_menores) + [pivo] + ordenacao(valores_maiores)

with open("dados.json") as file:
    dados = json.load(file)

valores = [dado['valor'] for dado in dados]
valores = ordenacao(valores)
total = sum([dado['valor'] for dado in dados])

dias_superioriores = 0 


media = round(total / len(valores),4)

for valor in valores:
    if valor > media:
        dias_superioriores += 1

        
if __name__ == "__main__":
    print ( f"O menor valor de faturamento ocorrido em um dia do mês foi: {valores[0]}")
    print ( f"O maior valor de faturamento ocorrido em um dia do mês foi: {valores[len(valores)-1]}")
    print ( f"Foram {dias_superioriores} dias em que o valor de faturamento diário foi superior à média mensal.")  