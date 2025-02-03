numeros = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))
soma_positivos = 0
soma_negativos = 0
for num in numeros:
    if num > 0:
        soma_positivos += num
    elif num < 0:
        soma_negativos == num
print('a soma dos positivos é', soma_positivos)
print("a soma dos negaotivos é", soma_negativos)