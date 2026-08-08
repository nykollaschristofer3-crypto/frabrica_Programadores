#autor= nykolloas christofer
## Programa que calcula o IMC de uma pessoa
#mostrar a classificação do IMC de acordo com a tabela da OMS

altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso:"))

IMC = peso / (altura ** 2)
print("Seu IMC é: {:.2f}".format(IMC))
if IMC < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= IMC < 24.9:
    print("Você está com o peso normal.")
elif 25 <= IMC < 29.9:
    print("Você está com sobrepeso.")
elif 30 <= IMC < 34.9:
    print("Você está com obesidade grau 1.")
elif 35 <= IMC < 39.9:
    print("Você está com obesidade grau 2.")
elif IMC >= 40:
    print("Você está com obesidade grau 3 mórbida.")
else:
    if IMC >= 30.00:
        print("cuidado com a saúde")
    else:
        print("tudo ok")