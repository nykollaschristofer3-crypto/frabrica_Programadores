#autor: Nykollas Christofer
# Projeto:  desvio Condicional

#criação das variáveis
nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário: '))
calculo = salario * 0.10
if calculo >= 100:
    print(f'{nome}, você tem dinheiro!')
else:
    print(f'{nome}, você não tem muito dinheiro!')