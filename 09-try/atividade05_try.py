#autor= Nykollas Christofer
#Projeto: Entendendo tratamento de exeção
print("---------conversão de temperatura---------")
print("Nykollas Christofer")

try:
    celcius = float(input('digite a temperatura em Celsius: '))
    fahrenheit = (celsius*(9/5))+32
    print(f'A temperatura em Fahrenheit é: {fahrenheit:.2f}')
except:
    print('digite um numero!')
