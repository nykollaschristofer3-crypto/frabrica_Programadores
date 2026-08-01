#autor= Nykollas Christofer
#Projeto: calculadora   tratamento de exceção
#chamada dea função

try:
    valor1 = float(input('digite o primeiro numero: '))
    valor2 = float(input('digite o segundo numero: '))
    soma = valor1 + valor2
    subtracao = valor1 - valor2
    multiplicacao = valor1 * valor2
    divisao = valor1 / valor2
    print(f'A soma é: {soma}')
    print(f'A subtração é: {subtracao}')
    print(f'A multiplicação é: {multiplicacao}')
    print(f'A divisão é: {divisao}')
except ValueError:
    print('digite um número válido!')
except ZeroDivisionError:
    print('não é possível dividir por zero!')