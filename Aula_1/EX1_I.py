altura = float(input("Qual é a sua altura para calcularmos seu peso ideal? "))
genero = int(input("Mas antes disso precisamos saber qual seu genero: 0 - Feminino e 1-Masculino "))
if genero == 0:
    print("Seu peso ideal é", (62.1 * altura) - 44.7, "Kg")
elif genero == 1:
    print("Seu peso ideal é", (72.7 * altura) - 58, "Kg")
else:
    print("Opção de genero invalida")
