# (e) Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve
# calcular a média alcançada por aluno e apresentar:
# • A mensagem "Aprovado", se a média alcançada for maior ou igual a 9.5 e menor
# que 19;
# • A mensagem "Reprovado", se a média for menor do que 9.5;
# • A mensagem "Aprovado com Distinção", se a média for pelo menos 19.
nota_1 = float(input("Digite o valor da primeira nota: "))
nota_2 = float(input("Digite o valor da segunda nota: "))
media = (nota_2 + nota_1) / 2
if 9.5 >= media < 19:
    print("Aprovado")
elif media < 9.5:
    print("Reprovado")
elif 19 >= media <= 20:
    print("Aprovado com Distinção")
else:
    print("Este valor não pertence à escala de notas")


