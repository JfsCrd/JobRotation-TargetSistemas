#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fib(n):
    a = 0
    b = 1
    if n==0:
        return a
    elif n==1:
        return b
    else:
        return fib(n-1)+fib(n-2) #calcula o fib recursivamente
    
n = int(input())
l = [(fib(i)) for i in range(0,n+1)] #armazena cada um dos valores da sequencia
print('Sequencia:', l)

if n in l:
    print('O valor existe na sequencia!')
else:
    print('O valor não existe na sequencia!')