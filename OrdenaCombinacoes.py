from typing import List, Any, Union

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
    ordem = Sor.ordena_varias_cartas(cartas_alta.copy())
    cartas_alta_sem_emp = []  # Indicador de combinações diferentes (kickers)
    empatados = []  # Indicador de quais jogadores estão empatados com essa mão
    for i, o in enumerate(cartas_alta, 0):
        if not (o in cartas_alta_sem_emp):
            cartas_alta_sem_emp.append(o)
            empatados.append([False, [combinacoes_seq_cor[i][3]]])
        else:
            empatados[cartas_alta_sem_emp.index(o)][0] = True
            empatados[cartas_alta_sem_emp.index(o)][1].append(combinacoes_seq_cor[i][3])
    cartas_alta_em_ordem = Sor.ordena_varias_cartas(cartas_alta_sem_emp.copy())
    empatados_em_ordem = []
    for q in cartas_alta_em_ordem:
        empatados_em_ordem.append(empatados[cartas_alta_sem_emp.index(q)])
    for carta in ordem:
        for i, comb in enumerate(combinacoes_seq_cor, 0):
            if carta == comb[2][0]:
                combinacoes_seq_cor[i][4] = empatados_em_ordem[cartas_alta_em_ordem.index(carta)]
                combinacoes_ordenadas.append(combinacoes_seq_cor[i])
                combinacoes_seq_cor.pop(i)
                break
    return combinacoes_ordenadas


def ordena_quadra(combinacoes_quadra):
    combinacoes_ordenadas = []  # Combinações ordenadas usando também o kicker
    indice_quadra = []
    for comb in combinacoes_quadra:
        indice_quadra.append(comb[2][0])
        comb.append([False, []])  # Adiciona a variável de índice 4 que informará se há empate com essa combinação e
        # com quais jogadores está empatado.
    quadras = []  # Indicador de combinações diferentes
    empatados = []  # Indicador de quais jogadores estão empatados com essa mão sem considerar o kicker ainda
    for i, q in enumerate(indice_quadra, 0):
        if not (q[0] in quadras):
            quadras.append(q[0])
            empatados.append([False, [combinacoes_quadra[i][3]]])
        else:
            empatados[quadras.index(q[0])][0] = True
            empatados[quadras.index(q[0])][1].append(combinacoes_quadra[i][3])
    quadras_em_ordem = Sor.ordena_varias_cartas_sem_naipe(quadras.copy())
    empatados_em_ordem = []
    for q in quadras_em_ordem:
        empatados_em_ordem.append(empatados[quadras.index(q)])
    kickers_diferentes = []
    kickers_diferentes_em_ordem = []
    empatados_no_kicker = []
    empatados_no_kicker_em_ordem = []
    for i, e in enumerate(empatados_em_ordem, 0):  # Percorre o vetor de quadras diferentes para fazer uma lista de
        # kickers para cada índice de quadra diferente
        kickers_diferentes.append([])
        kickers_diferentes_em_ordem.append([])
        empatados_no_kicker.append([])
        empatados_no_kicker_em_ordem.append([])
        for emp in e[1]:  # Percorre a lista de empatados com essa mesma quadra para obter os kickers
            for comb in combinacoes_quadra:
                if emp == comb[3]:
                    if not (comb[2][4][0] in kickers_diferentes[i]):
                        kickers_diferentes[i].append(comb[2][4][0])
                        empatados_no_kicker[i].append([False, [comb[3]]])
                    else:
                        empatados_no_kicker[i][kickers_diferentes[i].index(comb[2][4][0])][0] = True
                        empatados_no_kicker[i][kickers_diferentes[i].index(comb[2][4][0])][1].append(comb[3])
        kickers_diferentes_em_ordem[i] = Sor.ordena_varias_cartas_sem_naipe(kickers_diferentes[i].copy())
        for k in kickers_diferentes_em_ordem[i]:
            empatados_no_kicker_em_ordem[i].append(empatados_no_kicker[i][kickers_diferentes[i].index(k)])
    for q in empatados_no_kicker_em_ordem:
        for k in q:
            for e in k[1]:
                for j, comb in enumerate(combinacoes_quadra, 0):
                    if e == comb[3]:
                        comb[4] = k
                        combinacoes_ordenadas.append(comb)
                        combinacoes_quadra.pop(j)
                        break
    return combinacoes_ordenadas


def ordena_casa_completa(combinacoes_full):
    combinacoes_ordenadas = []
    indice_trinca = []
    indice_par = []
    for comb in combinacoes_full:
        indice_trinca.append(comb[2][0])
        indice_par.append(comb[2][3])
        comb.append([False, []])  # Adiciona a variável de índice 4 que informará se há empate com essa combinação e
        # com quais jogadores está empatado.
    trincas = []  # Indicador de combinações diferentes de trincas
    pares = []  # Indicador de combinações diferentes de pares para cada trinca
    empatados_p = []  # Indicador de quais jogadores estão empatados com a mesma trinca e o mesmo par
    for i, t in enumerate(indice_trinca, 0):
        if not (t[0] in trincas):
            trincas.append(t[0])
            pares.append([indice_par[i][0]])
            empatados_p.append([[False, [combinacoes_full[i][3]]]])
        else:  # Se a trinca já existir no vetor trincas
            if not (indice_par[i][0] in pares[trincas.index(t[0])]):  # Se o par desta trinca for diferente dos pares
                # das outras trincas de mesmo índice
                pares[trincas.index(t[0])].append(indice_par[i][0])
                empatados_p[trincas.index(t[0])].append([False, [combinacoes_full[i][3]]])
            else:  # Se a combinação de trinca e par já existirem registra o empate entre essas combinações
                empatados_p[trincas.index(t[0])][pares[trincas.index(t[0])].index(indice_par[i][0])][0] = True
                empatados_p[trincas.index(t[0])][pares[trincas.index(t[0])].index(indice_par[i][0])][1].\
                    append(combinacoes_full[i][3])
    trincas_ordem = Sor.ordena_varias_cartas_sem_naipe(trincas.copy())
    empatados_p_em_ordem = []
    pares_em_ordem = []
    for t in trincas_ordem:
        pares_em_ordem.append(pares[trincas.index(t)])
        pares_em_ordem[-1] = Sor.ordena_varias_cartas_sem_naipe(pares_em_ordem[-1].copy())
        empatados_p_em_ordem.append([])
        for p in pares_em_ordem[-1]:
            empatados_p_em_ordem[-1].append(empatados_p[trincas.index(t)][pares[trincas.index(t)].index(p)])
    for i, e in enumerate(trincas_ordem, 0):  # Percorre o vetor de trincas diferentes
        for ep in empatados_p_em_ordem[i]:  # percorre o vetor de pares para essa trinca
            for jogador in ep[1]:  # percorre os jogadores com esse par
                for k, comb in enumerate(combinacoes_full, 0):
                    if jogador == comb[3]:  # Procura a combinação do jogador na lista original
                        comb[4] = ep  # Define se há empates nessa combinação
                        combinacoes_ordenadas.append(comb)  # e anexa a combinação na lista ordenada
                        combinacoes_full.pop(k)  # Remove a combinação da lista original
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
            melhor_combinacao[i:i + cont6] = ordena_casa_completa(melhor_combinacao[i:i + cont6])
            empatados = cont6 - 1
            cont6 = 0
        elif cont5 > 1 and melhor_combinacao[i][0] == 5:
            # melhor_combinacao[i:i + cont5] = ordena_cor(melhor_combinacao[i:i + cont5])
            for comb in melhor_combinacao[i:i + cont5]:
                comb.append([False, [comb[3]]])
            empatados = cont5 - 1
            cont5 = 0
        elif cont4 > 1 and melhor_combinacao[i][0] == 4:
            # melhor_combinacao[i:i + cont4] = ordena_sequencia(melhor_combinacao[i:i + cont4])
            for comb in melhor_combinacao[i:i + cont4]:
                comb.append([False, [comb[3]]])
            empatados = cont4 - 1
            cont4 = 0
        elif cont3 > 1 and melhor_combinacao[i][0] == 3:
            # melhor_combinacao[i:i + cont3] = ordena_trinca(melhor_combinacao[i:i + cont3])
            for comb in melhor_combinacao[i:i + cont3]:
                comb.append([False, [comb[3]]])
            empatados = cont3 - 1
            cont3 = 0
        elif cont2 > 1 and melhor_combinacao[i][0] == 2:
            # melhor_combinacao[i:i + cont2] = ordena_2_pares(melhor_combinacao[i:i + cont2])
            for comb in melhor_combinacao[i:i + cont2]:
                comb.append([False, [comb[3]]])
            empatados = cont2 - 1
            cont2 = 0
        elif cont1 > 1 and melhor_combinacao[i][0] == 1:
            # melhor_combinacao[i:i + cont1] = ordena_par(melhor_combinacao[i:i + cont1])
            for comb in melhor_combinacao[i:i + cont1]:
                comb.append([False, [comb[3]]])
            empatados = cont1 - 1
            cont1 = 0
        elif cont0 > 1 and melhor_combinacao[i][0] == 0:
            # melhor_combinacao[i:i + cont0] = ordena_carta_alta(melhor_combinacao[i:i + cont0])
            for comb in melhor_combinacao[i:i + cont0]:
                comb.append([False, [comb[3]]])
            empatados = cont0 - 1
            cont0 = 0
        else:
            melhor_combinacao[i].append(
                [False, []])  # Adiciona a variável de índice 4 informando que não há empate para essa combinação.
    return melhor_combinacao
