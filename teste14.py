entrada = int(input('digite uma sequencia de numeros separados por espaço:'))
numeros = list(map(int, entrada.split()))
print (numeros)
if numeros == sorted(numeros):
    print('a lista está em ordem crescente')
else:
    print('a lista não está em ordem crescente')