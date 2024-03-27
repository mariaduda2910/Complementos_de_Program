# A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Faça um
# programa capaz de gerar a série até ao n-ésimo termo.
numero = int(input("Quantos termos deseja ver na sequencia de Fibonacci? "))
ultimo=1
penultimo=1
fibonacci = [1,1]

if numero==1:
    print(fibonacci[0])
elif numero==2:
    print(fibonacci[:])
else:
    count=3
    while count <= numero:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        fibonacci.append(termo)
        count += 1
    print(fibonacci)
