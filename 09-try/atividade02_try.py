# autor: Nykollas Christofer
# Projeto: Entendendo tratamento de exeção

try:
    num1 = float(input('digite o primeiro numero: '))
    num2 = float(input('digite o segundo numero: '))
    soma = num1 + num2
    print(f'A  soma é: {soma}')
except ValueError:
    print('digite um número válido!')