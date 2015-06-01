#!/usr/bin/python

tamanho = input("Favor informar o tamanho do arquivo em MB. ")
link = input("Favor inforar a velocidade do link em Mbps. ")

tempo = tamanho/link
minutos = tempo/60.0

print("O tempo aproximado para o download deste arquivo utilizando este link e de: ",minutos, "minutos.")
