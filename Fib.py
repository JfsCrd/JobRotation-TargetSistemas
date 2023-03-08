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