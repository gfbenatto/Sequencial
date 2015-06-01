#!/usr/bin/python

metros = input("Informe a quantidade de metros que serao pintados.")
litros = metros/6

totallata = litros/18.0
totalgalao = litros/3.6

precolata = totallata*80.0
precogalao = totalgalao*25.0

print("O total de tinta necessario e de ",litros,"litros de tinta.")
print("O total de latas necessario e de ", totallata, "latas.")
print("O total de galoes necessario e de ", totalgalao, "galoes.")
print("O preco total em latas de 18 litros e de ", precolata, "reais.")
print("O preco total em galoes de 3.6 litros e de ", precogalao, "reais.")
