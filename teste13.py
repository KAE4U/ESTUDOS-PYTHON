entrada = input('digite uma frase')
contador = 0
for letra in entrada:
 if letra == "a" or letra == "A":
  contador += 1
print(f"a letra A aparece:", contador, 'vezes')