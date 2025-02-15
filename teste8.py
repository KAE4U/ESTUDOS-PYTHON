num1 = int(input("digite um numero inteiro"))
num2 = int(input("digite um numero inteiro"))
num3 = int(input("digite um numero inteiro"))
if num1 > num2 and num1 > num3:
    print(f"o maior numero é", num1)
elif num2 > num1 and num2 > num3:
    print(f"o maior numero é", num2)
else:
    print(f"o maior numero é", num3) 