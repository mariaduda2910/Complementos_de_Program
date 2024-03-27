# Considere o vetor
# v = list ( range (50) ) # v = [0 , 1 , 2 , 3 , ... 49]
# Sem utilizar ciclos, imprima:
# (a) os primeiros 10 elementos
# (b) os últimos 10 elementos
# (c) os valores entre a posição 10 e 20 (inclusive)
# (d) apague o número na posição 5
# (e) apague o número 20
# (f) imprima os números por ordem inversa
# (g) faça a união com o conjunto [′a′,′ b′,′ c′
v = list(range(50))
print(v)
print(v[0:10])
print(v[-10:])
print(v[10:21])
v.pop(5)
v.remove(20)
v.reverse()
v.extend(["a","b","c"])
print(v)
