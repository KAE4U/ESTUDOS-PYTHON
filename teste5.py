peso = float(input('digite o peso'))
altura = float(input('digite a altura'))
imc = peso / altura ** 2 
print(f"o imc é:", imc)
if imc < 18.5:
  print("está abaixo do peso saudavel!")
if imc > 24.9:
  print('está acima do peso saudavel!')

