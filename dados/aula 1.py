# Programa dos Dados
# Carlos Eduardo G. Corrêa 

from random import randint

print(" Jogo de Dados")

dados1 = randint(1, 6)
dados2 = randint(1, 6)
jogador1 = dados1 + dados2

dados3 = randint(1, 6)
dados4 = randint(1, 6)
jogador2 = dados3 + dados4

print("Dado 1:", dados1)
print("Dado 2:", dados2)
print("Dado 3:", dados3)
print("Dado 4:", dados4)

print("Jogador 1:", jogador1)
print("Jogador 2:", jogador2)

if jogador1>jogador2:
    print("jogador 1 é foda")
elif jogador2>jogador1:
    print("jogador 2 deu a volta por cima")
else:
    print("empate de 2 lendas")
