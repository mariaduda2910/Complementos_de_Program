from math import ceil
tamanho_da_area = float(input("Digite o valor a ser pintado em metros quadrados: "))
latas = (tamanho_da_area / 3) / 18
quantidade_de_latas = ceil(latas)
preco = quantidade_de_latas * 80
print(f"È necessário {quantidade_de_latas} lata(s) para pintar todo o local. E o valor a ser pago é {preco} euros")


