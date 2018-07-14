import SorteiaOrdenaCartas as Sor


__author__ = "Rodrigo Farias"
__copyright__ = "Copyright (C) 2018 Rodrigo Farias"
__credits__ = ["Rodrigo Farias"]
__license__ = "Private"
__version__ = "1.0.1"
__maintainer__ = "Rodrigo Farias"
__email__ = "rodrigofarias08@gmail.com"
__status__ = "Production"


def define_melhor_combinacao(combinacao):
    if combinacao[7][0]:
        return [8, "Sequência de Cor", combinacao[7][1]]
    elif combinacao[4][0]:
        return [7, "Quadra", combinacao[4][1]]
    elif combinacao[3][0]:
        return [6, "Casa Completa", combinacao[3][1]]
    elif combinacao[5][0]:
        return [5, "Cor", combinacao[5][1]]
    elif combinacao[6][0]:
        return [4, "Sequência", combinacao[6][1]]
    elif combinacao[2][0]:
        return [3, "Trinca", combinacao[2][1]]
    elif combinacao[1][0]:
        return [2, "Dois Pares", combinacao[1][1]]
    elif combinacao[0][0]:
        return [1, "Par", combinacao[0][1]]
    else:
        return [0, "Carta Alta", combinacao[8][1]]


def ordena_seq_cor(combinacoes_seq_cor):
    cartas_alta = []
    combinacoes_ordenadas = []
    for comb in combinacoes_seq_cor:
        comb.append([False, []])  # Adiciona a variável de índice 4 que informará se há empate com essa combinação e
        # com quais jogadores está empatado.
        cartas_alta.append(comb[2][0])
    ordem = Sor.ordena_varias_cartas(cartas_alta)
    ordem_sem_emp = []  # Indicador de combinações diferentes
    empatados = []  # Indicador de quais jogadores estão empatados com essa mão
    for i, o in enumerate(ordem, 0):
        if not (o in ordem_sem_emp):
            ordem_sem_emp.append(o)
            empatados.append([False, [combinacoes_seq_cor[i][3]]])
        else:
            empatados[ordem_sem_emp.index(o)][0] = True
            empatados[ordem_sem_emp.index(o)][1].append(combinacoes_seq_cor[i][3])
    for carta in ordem:
        for i, comb in enumerate(combinacoes_seq_cor, 0):
            if carta == comb[2][0]:
                combinacoes_seq_cor[i][4] = empatados[ordem_sem_emp.index(carta)]
                combinacoes_ordenadas.append(combinacoes_seq_cor[i])
                combinacoes_seq_cor.pop(i)
                break
    return combinacoes_ordenadas


def ordena_quadra(combinacoes_quadra):
    combinacoes_ordenadas = []
    indice_quadra = []
    kicker = []
    for comb in combinacoes_quadra:
        indice_quadra.append(comb[2][0])
        kicker.append(comb[2][4])
        comb.append([False, []])  # Adiciona a variável de índice 4 que informará se há empate com essa combinação e
        # com quais jogadores está empatado.
    print(indice_quadra)
    print(kicker)
    indice_quadra = Sor.ordena_varias_cartas(indice_quadra)
    kicker = Sor.ordena_varias_cartas(kicker)
    quadras = []  # Indicador de combinações diferentes
    empatados = []  # Indicador de quais jogadores estão empatados com essa mão sem considerar o kicker ainda
    for i, q in enumerate(indice_quadra, 0):
        if not (q[0] in quadras):
            quadras.append(q[0])
            empatados.append([False, [combinacoes_quadra[i][3]]])
        else:
            empatados[quadras.index(q[0])][0] = True
            empatados[quadras.index(q[0])][1].append(combinacoes_quadra[i][3])
    for i in empatados:
        for e in i:  # percorrer a lista de empatados e fazer a comparação dos kickers
            print(e)
    print(quadras)
    print(empatados)
    for i in indice_quadra:
        for j, comb in enumerate(combinacoes_quadra, 0):
            if i == comb[2][0]:
                combinacoes_quadra[j][4] = empatados[quadras.index(i[0])]
                combinacoes_ordenadas.append(combinacoes_quadra[j])
                combinacoes_quadra.pop(j)
                break
    return combinacoes_ordenadas


def desempate(melhor_combinacao, n_adversarios):
    cont8 = 0  # Contador de mãos com Seq. de Cor
    cont7 = 0  # Contador de mãos com Quadra
    cont6 = 0  # Casa Completa
    cont5 = 0  # Cor
    cont4 = 0  # Sequência
    cont3 = 0  # Trinca
    cont2 = 0  # Dois Pares
    cont1 = 0  # Par
    cont0 = 0  # Carta Alta
    for i in range(n_adversarios + 1):
        if melhor_combinacao[i][0] == 0:
            cont0 += 1
        elif melhor_combinacao[i][0] == 1:
            cont1 += 1
        elif melhor_combinacao[i][0] == 2:
            cont2 += 1
        elif melhor_combinacao[i][0] == 3:
            cont3 += 1
        elif melhor_combinacao[i][0] == 4:
            cont4 += 1
        elif melhor_combinacao[i][0] == 5:
            cont5 += 1
        elif melhor_combinacao[i][0] == 6:
            cont6 += 1
        elif melhor_combinacao[i][0] == 7:
            cont7 += 1
        else:
            cont8 += 1
    empatados = 0  # Número de jogadores empatados
    for i in range(n_adversarios + 1):
        if empatados > 0:  # Se o jogador estiver empatado com o anterior
            empatados -= 1
        elif cont8 > 1:
            melhor_combinacao[i:i + cont8] = ordena_seq_cor(melhor_combinacao[i:i + cont8])
            empatados = cont8 - 1
            cont8 = 0
        elif cont7 > 1 and melhor_combinacao[i][0] == 7:
            melhor_combinacao[i:i + cont7] = ordena_quadra(melhor_combinacao[i:i + cont7])
            empatados = cont7 - 1
            cont7 = 0
        elif cont6 > 1 and melhor_combinacao[i][0] == 6:
            # melhor_combinacao[i:i + cont6] = ordenaCasaCompleta(melhor_combinacao[i:i + cont6])
            empatados = cont6 - 1
            cont6 = 0
        elif cont5 > 1 and melhor_combinacao[i][0] == 5:
            # melhor_combinacao[i:i + cont5] = ordenaCor(melhor_combinacao[i:i + cont5])
            empatados = cont5 - 1
            cont5 = 0
        elif cont4 > 1 and melhor_combinacao[i][0] == 4:
            # melhor_combinacao[i:i + cont4] = ordenaSequencia(melhor_combinacao[i:i + cont4])
            empatados = cont4 - 1
            cont4 = 0
        elif cont3 > 1 and melhor_combinacao[i][0] == 3:
            # melhor_combinacao[i:i + cont3] = ordenaTrinca(melhor_combinacao[i:i + cont3])
            empatados = cont3 - 1
            cont3 = 0
        elif cont2 > 1 and melhor_combinacao[i][0] == 2:
            # melhor_combinacao[i:i + cont2] = ordena2Pares(melhor_combinacao[i:i + cont2])
            empatados = cont2 - 1
            cont2 = 0
        elif cont1 > 1 and melhor_combinacao[i][0] == 1:
            # melhor_combinacao[i:i + cont1] = ordenaPar(melhor_combinacao[i:i + cont1])
            empatados = cont1 - 1
            cont1 = 0
        elif cont0 > 1 and melhor_combinacao[i][0] == 0:
            # melhor_combinacao[i:i + cont0] = ordenaCartaAlta(melhor_combinacao[i:i + cont0])
            empatados = cont0 - 1
            cont0 = 0
        else:
            melhor_combinacao[i].append(
                [False, []])  # Adiciona a variável de índice 4 informando que não há empate para essa combinação.
    return melhor_combinacao