# Ex 6. (a) Faça uma função que recebe 2 strings e informe se possuem o mesmo compri-
# mento e são iguais ou diferentes no conteúdo.
# Compara duas strings
# String 1: Portugal é campeão da Europa
# String 2: Portugal! é campeão da Europa!
# Tamanho de "Portugal é campeão da Europa": 28 caracteres
# Tamanho de "Portugal! é campeão da Europa!": 30 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.
string = input("Qual é a string?")
string_1 = input("Qual é a string?")


def comparador_de_sring(string, string_1):
    if len(string) == len(string_1):
        if string == string_1:
            print("As duas strings possuem tamanhos iguais e conteúdos iguais.")
        else:
            print("As duas strings possuem conteúdos diferentes, porem tamanho igual.")
    else:
        print("As duas strings tem conteúdos e tamanhos diferentes.")


comparador_de_sring(string, string_1)
