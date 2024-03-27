# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro
# entre 1 a 10. O utilizador deve informar qual número de que deseja ver a tabuada.
numero = int(input("Digite um valor de 1 a 10: "))
if numero >= 1 and numero <= 10:
    for i in range(1, 11):
        multiplicacao = numero * i
        print(f"{numero} x {i} = {multiplicacao}")
else:
    print("Só é possivel valores entre 1 e 10")
