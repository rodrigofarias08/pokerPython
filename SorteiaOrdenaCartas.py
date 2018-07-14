import random


__author__ = "Rodrigo Farias"
__copyright__ = "Copyright (C) 2018 Rodrigo Farias"
__credits__ = ["Rodrigo Farias"]
__license__ = "Private"
__version__ = "1.0.1"
__maintainer__ = "Rodrigo Farias"
__email__ = "rodrigofarias08@gmail.com"
__status__ = "Production"


naipe = ['e', 'c', 'o', 'p']
# naipe_escrito = ["Espadas", "Copas", "Ouros", "Paus"]
carta_indice = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
baralho = []
for i in naipe:
    for j in carta_indice:
        baralho.append(j + i)
cartas_em_jogo = baralho.copy()


def ordena_duas_cartas(carta1, carta2):
    if carta_indice.index(carta1[0]) < carta_indice.index(carta2[0]):
        return [carta1, carta2]
    elif carta_indice.index(carta1[0]) > carta_indice.index(carta2[0]):
        return [carta2, carta1]
    else:
        if naipe.index(carta1[1]) < naipe.index(carta2[1]):
            return [carta1, carta2]
        else:
            return [carta2, carta1]


def ordena_varias_cartas(cartas):
    cartas_em_ordem = []
    for c in range(0, len(cartas)):
        carta_alta = cartas[0]
        for c2 in range(1, len(cartas)):
            carta_alta = ordena_duas_cartas(carta_alta, cartas[c2])[0]
        cartas_em_ordem.append(carta_alta)
        cartas.pop(cartas.index(carta_alta))
    return cartas_em_ordem


def sorteia_carta():
    random.shuffle(cartas_em_jogo)
    return cartas_em_jogo.pop(0)


def distribui_cartas(n_adversarios):
    maos_jogadores = []
    index = 1
    while index <= n_adversarios:
        mao = ordena_duas_cartas(sorteia_carta(), sorteia_carta())
        print("A mão do computador {} é: {} {}".format(index, mao[0], mao[1]))
        maos_jogadores.append(mao)
        index += 1
    mao = ['Ke', 'Qe']  # ordenaDuasCartas(sorteiaCarta(), sorteiaCarta())
    print("\nSua mão é: {} {}\n".format(mao[0], mao[1]))
    maos_jogadores.append(mao)
    return maos_jogadores
