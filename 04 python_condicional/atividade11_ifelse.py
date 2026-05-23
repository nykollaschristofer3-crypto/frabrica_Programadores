#autor: Nykollas Christofer
#projeto desvio condicional

#criação de variavel
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
#cálculo da média
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")