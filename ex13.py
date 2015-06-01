#!/usr/bin/python

#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal

def calcula():
    altura = input("Informe sua altura: ")
    sexo = raw_input("Informe seu sexo: ")

    if sexo == 'masculino':
        idealmasc = (72.7 * altura) - 58
        print("Seu peso ideal e: ", idealmasc)
    else:
        idealmulher = (62.1 * altura) - 44.7
        print("Seu peso ideal e: ", idealulher)
#pesoideal = input("Informe o resultado do seu pesoo ideal: ")

#resultado = pesoideal/(altura**2)

    pesoatual = input("Qual seu peso atual? ")
    if pesoatual < 17:
        print("Seu peso esta muito baixo")
        print(pesoatual)
    elif pesoatual >= 60 and pesoatual <= 80:
        print("Seu peso esta legal!")
        print(pesoatual)
    elif pesoatual > 80:
        print("Voce ta pesado pra caralho!!!!")
        print(pesoatual)

calcula()
