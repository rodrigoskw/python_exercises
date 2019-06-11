from datetime import date

nascimento = int(input('INFORME O ANO DE NASCIMENTO: '))
alistar = nascimento + 18
idade = date.today().year - nascimento

if idade > 18:
    print('Você deveria ter se alistado em {}'.format(alistar))
elif idade < 18:
    print('Você deve se alistar em {}'.format(alistar))
else:
    print('Você deve se alistar IMEDIATAMENTE')
