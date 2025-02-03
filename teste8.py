#Escreva um programa que receba um número inteiro positivo do usuário e calcule a soma de todos os números de 1 até esse número.#

numero = int(input("digite um numero inteiro positivo"))
soma = sum(range(1,numero + 1))
print(soma)

