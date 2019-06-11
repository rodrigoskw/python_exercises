import datetime

ano = int(input('INFORME O ANO DE NASCIMENTO: '))
alistar = ano + 18
idade = datetime.datetime.now().year - ano

if idade > 18:
    print('Você deveria ter se alistado em {}'.format(alistar))
elif idade < 18:
    print('Você deve se alistar em {}'.format(alistar))
else:
    print('Você deve se alistar nesse ano')
