#!/usr/bin/python



peso = input("Digite o peso e Kg de peixe de hoje: ")

if peso <= 50:
    print("Quantidade de peixes dentro do limite")
    print(peso)
elif peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print("Quantidade de peixe excedeu, o valor da multa e: ", multa)
    print(peso)


