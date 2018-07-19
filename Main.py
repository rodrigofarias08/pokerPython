import SorteiaOrdenaCartas as Sor
import ProcuraCombinacoes as Pro
import OrdenaCombinacoes as Ord


__author__ = "Rodrigo Farias"
__copyright__ = "Copyright (C) 2018 Rodrigo Farias"
__credits__ = ["Rodrigo Farias"]
__license__ = "Private"
__version__ = "1.0.1"
__maintainer__ = "Rodrigo Farias"
__email__ = "rodrigofarias08@gmail.com"
__status__ = "Production"


maos_jogadores = []
n_adversarios = 0


def define_vencedor(mesa):
    combinacoes = []
    for m, mao in enumerate(maos_jogadores, 0):
        combinacoes.append([])
        # lista de combinações para cada mão m:
        # combinacoes[m][0] --> Par
        # combinacoes[m][1] --> 2 Pares
        # combinacoes[m][2] --> Trinca
        # combinacoes[m][3] --> Full House
        # combinacoes[m][4] --> Quadra
        # combinacoes[m][5] --> Flush
        # combinacoes[m][6] --> Straight
        # combinacoes[m][7] --> Straight Flush
        # combinacoes[m][8] --> Carta Alta
        combinacoes[m].append(Pro.procura_par(mao, mesa))  # Procura par
        if combinacoes[m][0][0]:  # Se tiver par
            combinacoes[m].append(Pro.procura_2_pares(mao, mesa))  # Procura 2 pares
            combinacoes[m].append(Pro.procura_trinca(mao, mesa))  # Procura trinca
            if combinacoes[m][2][0]:  # Se tiver trinca
                combinacoes[m].append(Pro.procura_full(mao, mesa))  # Procura full house
                combinacoes[m].append(Pro.procura_quadra(mao, mesa))  # Procura quadra
            else:  # Se não tiver trinca, não precisa procurar full house e quadra
                combinacoes[m].append([False, []])
                combinacoes[m].append([False, []])
        else:  # Se não tiver par, não precisa procurar 2 pares, trinca, full house e quadra
            combinacoes[m].append([False, []])
            combinacoes[m].append([False, []])
            combinacoes[m].append([False, []])
            combinacoes[m].append([False, []])
        if combinacoes[m][3][0] or combinacoes[m][4][0]:  # Se tiver full ou quadra
            combinacoes[m].append([False, []])  # não terá flush
            combinacoes[m].append([False, []])  # não terá straight
            combinacoes[m].append([False, []])  # não terá sequência de cor
        else:  # Se não tiver full ou quadra pode ser que tenha flush, straight e straight flush
            combinacoes[m].append(Pro.procura_cor(mao, mesa))  # Procura flush
            combinacoes[m].append(Pro.procura_seq(mao, mesa))  # Procura straight
            if combinacoes[m][5][0] and combinacoes[m][6][0]:  # Se tiver flush e straight procura sequência de cor
                combinacoes[m].append(Pro.procura_seq_cor(mao, mesa))
            else:  # Se não, não precisa procurar sequência de cor
                combinacoes[m].append([False, []])
        combinacoes[m].append(Pro.procura_carta_alta(mao, mesa))  # Procura carta alta
    melhor_combinacao = []
    for c, combinacao in enumerate(combinacoes, 0):
        melhor_combinacao.append(
            Ord.define_melhor_combinacao(combinacao))  # Obtém melhor combinação para cada mão participante
        melhor_combinacao[c].append(c)
    melhor_combinacao.sort(key=lambda x: x[0], reverse=True)
    melhor_combinacao = Ord.desempate(melhor_combinacao, n_adversarios)
    empatados = 0  # Número de jogadores empatados
    for combinacao in melhor_combinacao:  # Publica as melhores combinações de forma ordenada pela melhor mão
        if empatados > 0:  # Se o jogador estiver empatado com o anterior
            print("O jogador {} tem: {} {}".format(combinacao[3] + 1, maos_jogadores[combinacao[3]][0],
                                                   maos_jogadores[combinacao[3]][1]))
            empatados -= 1
        elif combinacao[4][0]:
            empatados = len(combinacao[4][1])
            print("\n{} jogadores empataram em {}º lugar nessa mão.".format(empatados,
                                                                            melhor_combinacao.index(combinacao) + 1))
            print("Para eles a melhor combinação é um(a) {} com: {} {} {} {} {}".format(combinacao[1], combinacao[2][0],
                                                                                        combinacao[2][1],
                                                                                        combinacao[2][2],
                                                                                        combinacao[2][3],
                                                                                        combinacao[2][4]))
            print("O jogador {} tem: {} {}".format(combinacao[3] + 1, maos_jogadores[combinacao[3]][0],
                                                   maos_jogadores[combinacao[3]][1]))
            empatados -= 1  # Remove o jogador atual da lista de empatados
        else:
            print("\nO jogador {} tem {} {} e terminou em {}º lugar nessa mão.".format(combinacao[3] + 1,
                                                                                       maos_jogadores[combinacao[3]][0],
                                                                                       maos_jogadores[combinacao[3]][1],
                                                                                       melhor_combinacao.index(
                                                                                           combinacao) + 1))
            print("Sua melhor combinação é um(a) {} com: {} {} {} {} {}".format(combinacao[1], combinacao[2][0],
                                                                                combinacao[2][1], combinacao[2][2],
                                                                                combinacao[2][3], combinacao[2][4]))


# main():
while True:
    aux_n_adversarios = input("Digite o número de adversários (1-8): ")
    if aux_n_adversarios.isnumeric():
        n_adversarios = int(aux_n_adversarios)
        if 0 < n_adversarios < 9:
            break

maos_jogadores = Sor.distribui_cartas(n_adversarios)
flop = [Sor.sorteia_carta(), Sor.sorteia_carta(), Sor.sorteia_carta()]
turn = Sor.sorteia_carta()
river = Sor.sorteia_carta()
# board = [flop[0], flop[1], flop[2], turn, river]
board = ['3e', '3e', '3e', '4e', '4e']

print("|" + " Cartas Comunitárias ".center(90, '-') + "|")
print("|" + ' ' * 90 + "|")
print("|" + "{}  {}  {}  {}  {} ".format(board[0], board[1], board[2], board[3], board[4]).center(90, ' ') + "|")
print("|" + ' ' * 90 + "|")
print("|" + '-' * 90 + "|")

# print(maos_jogadores)
define_vencedor(board)

# print(len(cartasEmJogo))
# print(maos_jogadores)
