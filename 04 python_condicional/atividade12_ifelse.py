#autor: Nykollas Christofer
#projeto desvio condicional

#criação de variavel
nome = input("Digite seu nome: ")
telefone = input("Digite seu telefone: ")
cidade = input("Digite sua cidade: ")
salario = float(input("Digite seu salário: "))
if salario >= 1000:
    print("Você tem uma boa renda!")
elif salario >= 700:
    print("Você tem uma renda razoável!")
elif salario >= 500:
    print("Você tem uma renda baixa!")
else:
    print("Você tem uma renda muito baixa!")