# (f) Dada uma string, conte:
# (a) quantos espaços em branco existem na frase.
# (b) quantas vezes aparecem as vogais a, e, i, o, u.
string_1 = "A rua é azul"
string = string_1.lower()

print("Possui", string.count(" ")," espaço.")
print("Possui", string.count("a")," letra a.")
print("Possui", string.count("e")," letra e.")
print("Possui", string.count("i")," letra i.")
print("Possui", string.count("o")," letra o.")
print("Possui", string.count("u")," letra u.")

for c in "aeiou": 
    print("Possui", string.count(c),f" letra {c}.")

