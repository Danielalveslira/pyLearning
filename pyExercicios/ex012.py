# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

precoProduto = float(input('Preço do produto R$: '))

desconto = 10 / 2

print(f'Promoção! Este produto está com 5% de desconto, de R$: {precoProduto} por apenas R$: {(precoProduto * 0.95)}')