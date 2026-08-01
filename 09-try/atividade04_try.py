#autor= Nykollas Christofer
#Projeto: calculo de imc

try:
    peso = float(input('digite o peso (kg): '))
    altura = float(input('digite a altura (m): '))
    imc = peso / (altura ** 2)
    print(f'O IMC é: {imc:.2f}')
except ValueError:
    print('digite valores válidos!')
