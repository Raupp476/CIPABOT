# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount


start = input()

# pega as informações

while(True):
        CEP = int(input("Olá, primeiro informe seu ID: "))
        if (11111111 <= CEP <= 99999999):
            break
        else:
            print("Informe um ID existente.")
            
emergencia = input("Qual a sua emergência?\n a - Manutenção \n b - Operador ")
emergencia = emergencia.lower()
manutencao = "a"
operador = "b"

# se caso for incêndio
if emergencia == manutencao:
    emergencia = "Manutenção"
    gravidade = input("Qual a gravidade da manutençao?\n a - Leve\n b - Moderado\n c - Grave ")
    gravidade = gravidade.lower()
    if gravidade == "a":
        gravidade = "Leve"
        print("\nEstamos enviando o relatório à CIPA\n")
    if gravidade == "b":
        gravidade = "Moderado"
        print("\nEstamos enviando o relatório à CIPA\n")
    if gravidade == "c":
        gravidade = "Grave"
        print("\nEstamos enviando o relatório à CIPA\n")
          
# se caso for com Operador            
if emergencia == operador:
    emergencia = "Operador"
    maquina = input("Acidente com Homem e Máquina?\n s - sim\n n - não ")
    maquina = maquina.lower()
    if maquina == "s":
        maquina = "Sim"
        corpo = input("O operador lesonou alguma parte do corpo?\n s - sim\n n - não ")
        corpo = corpo.lower()
        if corpo == "s":
            corpo = "Sim"
        if corpo == "n":
            corpo = "Não"
        print("\nEstamos enviando o relatório à CIPA\n")
    if maquina == "n":
        maquina = "Não"
        corpo = input("O operador lesionou alguma parte do corpo?\n s - sim\n n - não ")
        corpo = corpo.lower()
        if corpo == "s":
            corpo = "Sim"
        if corpo == "n":
            corpo = "Não"
        print("\nEstamos enviando o relatório à CIPA\n")
        
# printa as informações aos bombeiros

print("##################")
print("\nDados recolhidos:\n")
print("Emergência: " + emergencia)
if (emergencia == "manutencao"):
    print("Gravidade: " + gravidade)
    
if (emergencia == "operador"):
    print("Acidente com homem e máquina: " + maquina)
    print("Corpo Lesionado " + corpo)
        
print("ID: " + str(ID))
