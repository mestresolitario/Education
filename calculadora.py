main = """
  ____	   ___		___	    ___
 / ___|__ _| | ___ _   _| | __ _  __| | ___  _ __ __ _
| |   / _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` |
| |__| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| |
 \  __\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_|

Powered by Sr Solitario...\n\n"""

print(main)

print('Seja bem vindo!!')
print('Criado pelo Sr Solitário')

while True:
	operacao = input('''
	digite a operação desejada:
	+ soma
	- subtração
	* multiplicação
	/ divisão
	// divisão de números inteiros
>>> ''')


	n1 = float(input('Informe o primeiro valor >>> '))
	n2 = float(input('Informe o segundo valor >>> '))

	if operacao == '+':
		print('{} + {} ='.format(n1, n2))
		print(n1 + n2)
					
	if operacao == '-':
		print('{} - {} ='.format(n1, n2))
		print(n1 - n2)

	if operacao == '*':
		print('{} * {} ='.format(n1, n2))
		print(n1 * n2)

	if operacao == '/':
		print('{} / {} ='.format(n1, n2))
		print(n1 / n2)

	if operacao == '//':
		print('{} // {} ='.format(n1, n2))
		print(n1 // n2)

	else:
		print('Obrigado')
