#!/usr/bin/python

#Faca um Programa que peca 2 numeros inteiros e um numero real.
#Calcule e mostre:
#O produto do dobro do primeiro com metade do segundo . 
#A soma do triplo do primeiro com o terceiro. 
#O terceiro elevado ao cubo.

int1 = input("Digite o primeiro valor inteiro. ")
int2 = input("Digite o segundo valor inteiro. ")
real = input("Digite um numero real, ")

calc1 = (int1*2) + (int2/2)
calc2 = (int1*3) + real
calc3 = real**3

print("O produto do dobro do primeiro com metade do segundo e: ",
       float(calc1))
print("A soma do triplo do primeiro com o terceiro e: ", float(calc2))
print("O terceiro elevado ao cubo e: ", float(calc3))
