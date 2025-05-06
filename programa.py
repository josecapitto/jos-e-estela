
from funcoes import (
    rolar_dados, guardar_dado, remover_dado, calcula_pontos_regra_simples,
    calcula_pontos_soma, calcula_pontos_sequencia_baixa, calcula_pontos_sequencia_alta,
    calcula_pontos_full_house, calcula_pontos_quadra, calcula_pontos_quina,
    calcula_pontos_regra_avancada, faz_jogada, imprime_cartela
)

cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(cartela)

cats_regra_simples = ['1', '2', '3', '4', '5', '6']
cats_regra_avan = ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']

rodada = 0
while rodada < 12:
    dados_guardados = []
    dados_rolados = rolar_dados(5)
    rerro = 0
    rodada_continua = True

    while rodada_continua:
        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados guardados: {dados_guardados}')
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        comando = input()

        while comando not in ['0', '1', '2', '3', '4']:
            print('Opção inválida. Tente novamente.')
            comando = input()

        if comando == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice_g = int(input())
            result_g = guardar_dado(dados_rolados, dados_guardados, indice_g)
            dados_rolados, dados_guardados = result_g

        elif comando == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice_r = int(input())
            result_r = remover_dado(dados_rolados, dados_guardados, indice_r)
            dados_rolados, dados_guardados = result_r

        elif comando == '3':
            if rerro < 2:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerro += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif comando == '4':
            imprime_cartela(cartela)

        elif comando == '0':
            dados_totais = dados_guardados + dados_rolados
            print("Digite a combinação desejada:")
            while True:
                combinacao = input()
                if combinacao in cats_regra_simples:
                    if cartela['regra_simples'][int(combinacao)] == -1:
                        cartela = faz_jogada(dados_totais, combinacao, cartela)
                        break
                    else:
                        print("Essa combinação já foi utilizada.")
                elif combinacao in cats_regra_avan:
                    if cartela['regra_avancada'][combinacao] == -1:
                        cartela = faz_jogada(dados_totais, combinacao, cartela)
                        break
                    else:
                        print("Essa combinação já foi utilizada.")
                else:
                    print("Combinação inválida. Tente novamente.")
            rodada_continua = False

    rodada += 1

imprime_cartela(cartela)

pontuacao_final = 0
pontos_simples = sum(v for v in cartela['regra_simples'].values() if v != -1)
pontos_avancada = sum(v for v in cartela['regra_avancada'].values() if v != -1)

pontuacao_final = pontos_simples + pontos_avancada
if pontos_simples >= 63:
    pontuacao_final += 35

print(f"Pontuação total: {pontuacao_final}")
