# g) Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação
# no seu respetivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
idade = []
altura = []
for i in range(5):
    idade.append(int(input("Qual a idade ?")))
    altura.append(float(input("Qual a altura ?")))
idade.reverse()
altura.reverse()
print(idade,"\n", altura)
for i in range(5):
    print("A idade é ", idade[i], "e a respectiva altura é ",altura[i])
