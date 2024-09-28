# Ex 9. Implemente as classes apresentadas no diagrama da Fig. 1. Use decoradores para im-
# plementar o encapsulamento. Note que além de getter e setter, existem outros métodos em
# algumas das classes. Crie um programa que permita de modo interativo listar, inserir, remo-
# ver, e editar carros de uma lista. Crie ainda uma opção para gravar essa lista num ficheiro
# (veja o pacote pickle). Pode encontrar um template para as classes em https://bitbucket.
# org/pcardoso/complementos-de-programa-o-sti-ise-ualg/src/master/Python/templates_
# exercicios/car.
# Exemplo de menu:
# 11 - lista carros 21 - lista pessoas ...
# 12 - novo carro 22 - nova pessoa ...
# 13 - apaga carro 23 - apaga pessoa ...
# 14 - edita carro 24 - edita pessoa ...

from color import Color
from engine import Engine
from person import Person
from car import Car
import pickle
from time import sleep

list_of_persons = []
list_of_engines = []
list_of_colors = []
list_of_cars = []


def showMenu():
    print(47 * " ", "MENU")
    print(53 * "-=")
    print("| (1) Criar Pessoa         (5) Criar Motor          (9) Criar Cor            (13) Criar Carro           |")
    print("| (2) Lista de Pessoa(s)   (6) Lista de Motor(es)   (10) lista de Cor(es)    (14) Lista de Carro(s)     |")
    print("| (3) Salvar Pessoa(s)     (7) Salvar Motor(es)     (11) Salvar Cor(es)      (15) Salvar Carro(s)       |")
    print("| (4) Carregar Pessoa(s)   (8) Carregar Motor(es)   (12) Carregar Cor(es)    (16) Carregar Carro(s)     |")
    print("|                                                                                                       |")
    print("|                                             (0) Sair                                                  |")
    print(53 * "-=")


def main():
    global list_of_colors, list_of_cars, list_of_engines, list_of_persons
    while True:
        showMenu()
        try:
            op = int(input("Insira a ação que deseja executar: "))

            if op == 0:  # Sair do Programa
                break
            # _____________________________________________________________________________________________Classe Pessoa

            elif op == 1:  # Criar uma Pessoa
                forename = input("Nome: ").title()
                surname = input("Sobrenome: ").title()
                address = input("Endereço: ").title()
                CC = input("Identidade: ")
                phone = input("Número: ")
                pessoa = Person(forename=forename, surname=surname, address=address, CC=CC, phone=phone)
                list_of_persons.append(pessoa)
            elif op == 2:  # Mostrar lista de pessoa
                print(list_of_persons)
            elif op == 3:  # Salvar Pessoas
                with open("list_of_persons.pkl", "wb") as f:
                    pickle.dump(list_of_persons, f)
            elif op == 4:  # Carregar Pessoas
                with open("list_of_persons.pkl", "rb") as f:
                    list_of_persons = pickle.load(f)

            # ______________________________________________________________________________________________Classe Motor

            elif op == 5:  # Criar motor
                fuel = input("Capacidade do Combustível: ")
                horsepower = input("Potência do motor: ")
                torque = input("Torque: ")
                displacement = input("Deslocamento: ")
                numberCylinders = input("Cilindradas: ")
                startingSystem = input("Arranque do sistema: ")
                dryWeight = input("dry Weight")
                manufacturer = input("Fabricante: ")
                motor = Engine(fuel=fuel, horsepower=horsepower, torque=torque, displacement=displacement,
                               numberCylinders=numberCylinders, startingSystem=startingSystem, dryWeight=dryWeight,
                               manufacturer=manufacturer)
                list_of_engines.append(motor)
            elif op == 6:  # Lista de motor
                print(list_of_engines)
            elif op == 7:  # Salvar Motores
                with open("list_of_engines.pkl", "wb") as f:
                    pickle.dump(list_of_engines, f)
            elif op == 8:  # Carregar Motores
                with open("list_of_engines.pkl", "rb") as f:
                    list_of_engines = pickle.load(f)

            # ______________________________________________________________________________________________Classe Cores

            elif op == 9:  # Criar Cor
                colorName = input("Nome da cor: ")
                r = input("R: ")
                g = input("G: ")
                b = input("B: ")
                cor = Color(colorName=colorName, r=r, g=g, b=b)
                list_of_colors.append(cor)
            elif op == 10:  # Lista de Cores
                print(list_of_colors)
            elif op == 11:  # Salvar Cores
                with open("list_of_colors.pkl", "wb") as f:
                    pickle.dump(list_of_colors, f)
            elif op == 12:  # Carregar Cores
                with open("list_of_colors.pkl", "rb") as f:
                    list_of_colors = pickle.load(f)

            # ______________________________________________________________________________________________Classe Carro

            elif op == 13:  # Criar Carro
                if list_of_persons == []:
                    print("Não é possível criar um carro, pois não foi criado um dono antes.")
                    sleep(2)
                elif list_of_colors == []:
                    print("Não é possível criar um carro, pois não foi criado uma cor antes.")
                    sleep(2)
                elif list_of_engines == []:
                    print("Não é possível criar um carro, pois não foi criado um motor antes.")
                    sleep(2)
                else:
                    person_id = int(input(f"""{list_of_persons} \nIndice do dono do carro: """))
                    color_id = int(input(f"""{list_of_colors} \nIndice da cor do carro: """))
                    engine_id = int(input(f"""{list_of_engines}\nIndice do motor:  """))
                    brand = input("Marca: ").title()
                    model = input("Modelo: ").title()
                    consumption = input("Consumo: ")
                    kms = input("Número: ")
                    carro = Car(owner=list_of_persons[person_id],
                                color=list_of_colors[color_id],
                                engine=list_of_engines[engine_id],
                                brand=brand,
                                model=model,
                                consumption=consumption,
                                kms=kms)
                    list_of_cars.append(carro)
            elif op == 14:  # Lista de Carro
                print(list_of_cars)
                if list_of_cars == []:
                    print()
                else:
                    try:
                        ask = int(input("Deseja remover algum carro digite (1)? "))
                        if ask == 1:
                            remover = int(input("Qual o indice do carro que deseja remover: "))
                            del (list_of_cars[remover])
                        else:
                            pass
                    except ValueError:
                        print("Verifique se digitou corretamente os valores!")

            elif op == 15:  # salvar lista de carros
                with open("list_of_cars.pkl", "wb") as f:
                    pickle.dump(list_of_cars, f)  # dump (envia os dados para o pickle em forma de binário)
            elif op == 16:
                with open("list_of_cars.pkl", "rb") as f:
                    list_of_cars = pickle.load(f)  # load (carrega de volta pra mémoria o qu esta salvo em forma de binário)
                print(list_of_cars)


        except ValueError:
            print("!Verifique se inseriu corretamente os dados!")


main()
# TODO editar carros de uma lista(para editar pelo indice )
