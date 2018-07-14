import SorteiaOrdenaCartas as Sor


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


def procura_carta_alta(mao, mesa):
    high = Sor.ordena_varias_cartas([mao[0], mao[1], mesa[0], mesa[1], mesa[2], mesa[3], mesa[4]])
    return [True, high[0:5]]


def procura_cor(mao, mesa):
    flush = [0, 0, 0, 0]
    cartas_flush = [[], [], [], []]
    for carta in [mao[0], mao[1], mesa[0], mesa[1], mesa[2], mesa[3], mesa[4]]:
        if carta[1] == 'e':
            flush[0] += 1
            cartas_flush[0].append(carta)
        elif carta[1] == 'c':
            flush[1] += 1
            cartas_flush[1].append(carta)
        elif carta[1] == 'o':
            flush[2] += 1
            cartas_flush[2].append(carta)
        else:
            flush[3] += 1
            cartas_flush[3].append(carta)
    for i in range(0, 4):
        if flush[i] >= 5:
            return [True, Sor.ordena_varias_cartas(cartas_flush[i])[0:5]]
    return [False, []]


def procura_seq(mao, mesa):
    seq = Sor.ordena_varias_cartas([mao[0], mao[1], mesa[0], mesa[1], mesa[2], mesa[3], mesa[4]])
    for c in range(6):  # Move cartas repetidas para o final da lista
        if seq[c][0] == seq[c + 1][0]:
            repetida = seq.pop(c + 1)
            seq.append(repetida)
            if seq[c][0] == seq[c + 1][0]:
                repetida = seq.pop(c + 1)
                seq.append(repetida)
    for i in range(0, 3):
        if carta_indice.index(seq[i][0]) == carta_indice.index(seq[i + 1][0]) - 1:
            if carta_indice.index(seq[i + 1][0]) == carta_indice.index(seq[i + 2][0]) - 1:
                if carta_indice.index(seq[i + 2][0]) == carta_indice.index(seq[i + 3][0]) - 1:
                    if carta_indice.index(seq[i + 3][0]) == carta_indice.index(seq[i + 4][0]) - 1:
                        return [True, seq[i:i + 5]]
    return [False, []]


def procura_seq_cor(mao, mesa):
    flush = Sor.ordena_varias_cartas([mao[0], mao[1], mesa[0], mesa[1], mesa[2], mesa[3], mesa[4]])
    for c in range(6):  # Move cartas repetidas para o final da lista
        if flush[c][0] == flush[c + 1][0]:
            repetida = flush.pop(c + 1)
            flush.append(repetida)
            if flush[c][0] == flush[c + 1][0]:
                repetida = flush.pop(c + 1)
                flush.append(repetida)
    for n in range(0, 3):
        if carta_indice.index(flush[n][0]) == carta_indice.index(flush[n + 1][0]) - 1 and \
                flush[n][1] == flush[n + 1][1]:
            if carta_indice.index(flush[n + 1][0]) == carta_indice.index(flush[n + 2][0]) - 1 and \
                    flush[n + 1][1] == flush[n + 2][1]:
                if carta_indice.index(flush[n + 2][0]) == carta_indice.index(flush[n + 3][0]) - 1 and \
                        flush[n + 2][1] == flush[n + 3][1]:
                    if carta_indice.index(flush[n + 3][0]) == carta_indice.index(flush[n + 4][0]) - 1 and \
                            flush[n + 3][1] == flush[n + 4][1]:
                        return [True, flush[n:n + 5]]
    return [False, []]


def procura_par(mao, mesa):
    par = Sor.ordena_varias_cartas([mao[0], mao[1], mesa[0], mesa[1], mesa[2], mesa[3], mesa[4]])
    for c, carta in enumerate(par[0:6], 0):
        if carta[0] == par[c + 1][0]:
            carta1 = par.pop(c)
            carta2 = par.pop(c)
            par.insert(0, carta1)
            par.insert(1, carta2)
            return [True, par[0:5]]
    return [False, []]


def procura_2_pares(mao, mesa):
    pares = Sor.ordena_varias_cartas([mao[0], mao[1], mesa[0], mesa[1], mesa[2], mesa[3], mesa[4]])
    for c, carta in enumerate(pares[0:6], 0):
        if carta[0] == pares[c + 1][0]:
            carta1 = pares.pop(c)
            carta2 = pares.pop(c)
            pares.insert(0, carta1)
            pares.insert(1, carta2)
            break
    for c, carta in enumerate(pares[2:6], 0):
        if carta[0] == pares[c + 3][0]:
            carta1 = pares.pop(c + 2)
            carta2 = pares.pop(c + 2)
            pares.insert(2, carta1)
            pares.insert(3, carta2)
            return [True, pares[0:5]]
    return [False, []]


def procura_trinca(mao, mesa):
    trinca = Sor.ordena_varias_cartas([mao[0], mao[1], mesa[0], mesa[1], mesa[2], mesa[3], mesa[4]])
    for c, carta in enumerate(trinca[0:5], 0):
        if carta[0] == trinca[c + 1][0] and carta[0] == trinca[c + 2][0]:
            carta1 = trinca.pop(c)
            carta2 = trinca.pop(c)
            carta3 = trinca.pop(c)
            trinca.insert(0, carta1)
            trinca.insert(1, carta2)
            trinca.insert(2, carta3)
            return [True, trinca[0:5]]
    return [False, []]


def procura_quadra(mao, mesa):
    quadra = Sor.ordena_varias_cartas([mao[0], mao[1], mesa[0], mesa[1], mesa[2], mesa[3], mesa[4]])
    for c, carta in enumerate(quadra[0:4], 0):
        if carta[0] == quadra[c + 1][0] and carta[0] == quadra[c + 2][0] and carta[0] == quadra[c + 3][0]:
            carta1 = quadra.pop(c)
            carta2 = quadra.pop(c)
            carta3 = quadra.pop(c)
            carta4 = quadra.pop(c)
            quadra.insert(0, carta1)
            quadra.insert(1, carta2)
            quadra.insert(2, carta3)
            quadra.insert(3, carta4)
            return [True, quadra[0:5]]
    return [False, []]


def procura_full(mao, mesa):
    full = Sor.ordena_varias_cartas([mao[0], mao[1], mesa[0], mesa[1], mesa[2], mesa[3], mesa[4]])
    for c, carta in enumerate(full[0:5], 0):
        if carta[0] == full[c + 1][0] and carta[0] == full[c + 2][0]:
            carta1 = full.pop(c)
            carta2 = full.pop(c)
            carta3 = full.pop(c)
            full.insert(0, carta1)
            full.insert(1, carta2)
            full.insert(2, carta3)
            break
    for c, carta in enumerate(full[3:6], 0):
        if carta[0] == full[c + 4][0]:
            carta1 = full.pop(c + 3)
            carta2 = full.pop(c + 3)
            full.insert(3, carta1)
            full.insert(4, carta2)
            return [True, full[0:5]]
    return [False, []]
