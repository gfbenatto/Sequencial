#!/usr/bin/python

salario = input("Quanto voce ganha por hora trabalhada? ")
tempo = input("Quantas horas voce trabalhou este mes? ")

bruto = salario * tempo
print("Seu salario bruto e: ",bruto)

inss = (bruto*8)/100

print("Voce pagou", inss, "de INSS este mes.")

sindicato = (bruto*5)/100

print("Voce pagou", sindicato, " de Sindicato este mes.")

ir = (bruto*11)/100

print("Voce pagou", ir , " de IR este mes.")

liq = bruto-ir-inss-sindicato

print("Seu salario liquido e de ", liq , "este mes.")
