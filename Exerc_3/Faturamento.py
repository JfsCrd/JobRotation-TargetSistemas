import json

with open("Exerc_3\dados.json") as dados_faturamento:
    dados = json.load(dados_faturamento)


def faturamento(dados):
    maior = 0.00

    for i in dados:
        if maior < i['valor'] and i['valor']!=0.00:
            maior = i['valor']
            dia_maior = i['dia']

    print('Maior faturamento no dia', dia_maior, ':', maior)
    
    menor = maior

    for i in dados:
        if menor > i['valor'] and i['valor']!=0.00:
            menor = i['valor']
            dia_menor = i['dia']
    
    print('Menor faturamento no dia', dia_menor, ':', menor)

def maiorMedia(dados):
    dias_totais = 0.00
    dias_maior = []
    total = 0.00

    for i in dados:
        if i['valor']!=0.00:
            total = total + i['valor']
            dias_totais = dias_totais + 1
    
    for i in dados:
        if i['valor']> total/dias_totais:
            dias_maior.append(i['dia'])

    print("Dias que tiveram faturamento superior a média:", dias_maior)

faturamento(dados)
maiorMedia(dados)