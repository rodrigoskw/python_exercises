casa = float(input('Valor da casa: '))
salario = float(input('Informe o salário: '))
anos = int(input('Quantos anos deseja pagar a casa: '))

prestacao = casa / (anos * 12)

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, prestacao))

minimo = salario * 30 / 100

if prestacao > minimo:
    print('EMPRÉSTIMO NEGADO!!!')
else:
    print('EMPRÉSTIMO CONCEDIDO!!!')

