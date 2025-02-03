#Escreva um programa que receba uma lista de palavras e imprima a palavra mais longa da lista.

palavras = (input("digite uma sequencia de palavras separadas por espaço")) .split()
maior_palavra = max(palavras, key=len)
print("a maior palavra da frase é:", maior_palavra)