#Escreva um programa que inverta os caracteres de um string

string = input('Digite a string: ')

def inverteCaracteres(string):
    aux_string_invertida = [] 
    tamanho_string = len(string)-1
    fim = tamanho_string

    for i in range(0, tamanho_string+1):
        aux_string_invertida.append(string[fim])
        fim = fim-1

    string_invertida = ''.join(aux_string_invertida)

    print('String original:', string)
    print('String invertida:', string_invertida)

inverteCaracteres(string)