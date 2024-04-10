def calcular_pontuacao(ordem, sistema_pontos):
    # Inicializa uma lista de pontos para cada piloto
    pontos = [0] * len(ordem)
    # Itera sobre a ordem de chegada
    for idx, posicao in enumerate(ordem):
        # Verifica se a posição do piloto está dentro das posições válidas para pontuação
        if posicao <= sistema_pontos['ult_pos']:
            # Atribui os pontos correspondentes à posição do piloto
            pontos[idx] = sistema_pontos['pts'][posicao - 1]
    return pontos

def determinar_vencedor(num_corridas, num_pilotos, resultados, sistemas):
    # Itera sobre os diferentes sistemas de pontuação
    for sistema in sistemas:
        # Inicializa uma lista de pontos para cada piloto
        pontos_pilotos = [0] * num_pilotos
        # Itera sobre os resultados de cada corrida
        for resultado in resultados:
            # Calcula os pontos para cada piloto na corrida atual usando o sistema de pontuação atual
            pontos_corrida = calcular_pontuacao(resultado, sistema)
            # Acumula os pontos de cada piloto
            for idx in range(num_pilotos):
                pontos_pilotos[idx] += pontos_corrida[idx]
        
        # Determina o máximo de pontos obtidos entre todos os pilotos
        max_pontos = max(pontos_pilotos)
        # Identifica os pilotos que obtiveram o máximo de pontos (vencedores)
        vencedores = [str(idx + 1) for idx, pontos in enumerate(pontos_pilotos) if pontos == max_pontos]
        # Imprime os números dos pilotos vencedores
        print(' '.join(vencedores))

def iniciar_simulacao():
    # Loop principal para continuar a simulação até que o número de corridas e pilotos seja zero
    while True:
        # Entrada: número de corridas e número de pilotos
        num_corridas, num_pilotos = map(int, input().split())
        if num_corridas == 0 and num_pilotos == 0:
            # Verifica se é o momento de encerrar a simulação
            break
        
        # Entrada: resultados das corridas
        resultados_corrida = []
        for _ in range(num_corridas):
            resultados_corrida.append(list(map(int, input().split())))
        
        # Entrada: número de sistemas de pontuação e definição de cada sistema
        num_sistemas = int(input())
        sistemas_pontuacao = []
        for _ in range(num_sistemas):
            sistema = {}
            ult_pos, *pontos = map(int, input().split())
            sistema['ult_pos'] = ult_pos
            sistema['pts'] = pontos
            sistemas_pontuacao.append(sistema)
        
        # Determina os vencedores usando os resultados das corridas e os sistemas de pontuação
        determinar_vencedor(num_corridas, num_pilotos, resultados_corrida, sistemas_pontuacao)

if __name__ == "__main__":
    # Roda a simulação
    iniciar_simulacao()
