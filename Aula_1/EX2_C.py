# (c) Faça um programa que verifique se uma letra digitada é "F"ou "M". Conforme a letra
# escrever: F - Feminino, M - Masculino, Sexo Inválido.
genero = input("Digite F- Feminino e M - Masculino  ").upper()
if genero == "F":
    print("Feminino")
elif genero == "M":
    print("Masculino")
else:
    print("Sexo Inválido")