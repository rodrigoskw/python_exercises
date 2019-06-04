nome = str(input('Digite seu nome: ')).strip().lower()
print('O nome digitado com as letras maiusculas é {}'.format(nome.upper()))
print('O nome digitado com as letras minusculas é {}'.format(nome.lower()))
nome_separado = nome.split()
print('O primeiro nome possui {} letras'.format(len(nome_separado[0])))
print('Seu nome possui silva: {}'.format('silva' in nome))

cidade = str(input('Digite o nome de uma cidade: ')).strip().lower()
print('A cidade possui o nome Santo: {}'.format('santo' in cidade))

frase = str(input('Digite uma frase: ')).strip().lower()
print('Processando frase ...')
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A posição da primeira letra A é {}.'.format(frase.find('a')+1))
print('A posição da ultima letra A é {}.'.format(frase.rfind('a')+1))
print('A primeira palavra da frase é {}.'.format(frase.split()[0]))
print('A última palavra da frase é {}.'.format(frase.split()[len(frase.split())-1]))



