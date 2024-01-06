# Programa que calcula aprovação de financiamento.

casa = float(input('Qual o valor da casa desejada? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
prestacao  = casa / (anos * 12)
parcelas = anos * 12
minimo = salario * 30 / 100

print('Para pagar uma casa no valor de R${:.2f} em {} anos'.format(casa, anos), end=' ')
print('a prestação será de R${:.2f} em {} vezes.'.format(prestacao, parcelas))

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Valor solicitado excede o limite de 30% do salário. \nEmpréstimo NEGADO!')
