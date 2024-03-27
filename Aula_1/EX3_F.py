# Faça um programa que leia n números e informe a soma e a média destes.
soma = 0
count = 0
while True:
    numero = int(input("Digite um valor, caso deseje parar pressione 0: "))
    if numero == 0:
        break
    else:
        soma = soma + numero
        count = count + 1
try:
    print(f"A soma foi de {soma} e a média foi {soma/count}")
except ZeroDivisionError:
    print(f"A soma foi de 0 e a média tambem foi 0")