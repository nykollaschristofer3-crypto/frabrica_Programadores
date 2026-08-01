#autor= Nykollas Christofer
#Projeto: conversão de moeda

try:
    reais = float(input("Digite o valor em reais: "))
    dolar = reais / 5.08
    print(f"O valor em dólares é: {dolar:.2f}")
except ValueError:
    print("Por favor, digite um valor numérico válido.")