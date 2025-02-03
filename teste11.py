#Escreva um programa que receba um número inteiro positivo e calcule o fatorial desse número.#

numero = int(input('digite um numero'))
fatorial = 1
for i in range (1, numero +1):
    fatorial *= i
print("o fatorial do numero é", fatorial)
