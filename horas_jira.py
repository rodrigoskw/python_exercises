import math

horas_somadas = 0.00
sair = 'n'
while sair == 'n':
    horas = float(input('Informe as horas que aparecem no Jira com ponto:'))
    horas_somadas = horas_somadas + horas
    # Transformar as horas decimais para horas normais
    sair = input('Deseja sair (s-sim / n-não) ?')


if int(horas_somadas) < 8:
    horas_faltantes = (horas_somadas - 8) * -1
    dec, inteiro = math.modf(horas_faltantes)
    decimais_em_minutos = dec * 60
    print('Faltam lançar {} horas e {} minutos'.format(int(inteiro), int(decimais_em_minutos)))
