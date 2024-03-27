# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
# números pares e a quantidade de números impares.
pares = 0
impares = 0
for i in range(10):
    numero = int(input("Digite um valor: "))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
print(f"Dos numeros {pares} são pares e {impares} são impares")
