programa {
  funcao inicio() {
    real valor_produto,percentual_desconto,valor_desconto
    //VALOR DO PRODUTO = 200,00
    //PERCENTUAL DE DESCONTO 10%
    //VALOR DO DESCONTO = 20,00

    escreva("DIGITE O VALOR DOPRODUTO: ")
    leia(valor_produto)
    escreva("quanto de desconto tem a vista?:")
    leia(percentual_desconto)

    valor_desconto = valor_produto * (percentual_desconto/100)

  }
}
