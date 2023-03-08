#calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora

faturamentos = dict([('SP', 67836.43),('RJ', 36678.66),('MG', 29229.88),('ES', 27165.48),('Outros',  19849.53)])

def caculaPercentual(faturamentos):
    total_mensal = 0.00
    percentuais = []

    for i in faturamentos.values():
        total_mensal = total_mensal + i

    for i in faturamentos.values():
        percentuais.append(i*100/total_mensal)

    j = 0
    for i in faturamentos.keys():
        print(i, f'{percentuais[j]:.02f}','%')
        j = j+1

caculaPercentual(faturamentos)
    

