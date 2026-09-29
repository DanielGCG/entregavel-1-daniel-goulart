# Entregável 1 - Bateria do Robô

# === Entrada ===
bateria_inicial = int(input('Bateria atual: '))

if (bateria_inicial > 100 or bateria_inicial < 0):
    print('Valor inválido: ')
    exit()

duracao_missao = int(input('Duração prevista da missão: '))

if (duracao_missao <= 0):
    print('Valor inválido: ')
    exit()

consumo_minuto = int(input('Consumo por minuto: '))

if (consumo_minuto <= 0):
    print('Valor inválido: ')
    exit()


# === Calculo ===
bateria_final = bateria_inicial - ((duracao_missao) * consumo_minuto)

if (bateria_final < 0):
    print('Bateria insuficiente para a missão, faltaria ' + str(abs(bateria_final)) + '% de carga.')
else:
    print('Bateria suficiente para a missão, sobrando: ' + str(bateria_final) + '% de carga.')