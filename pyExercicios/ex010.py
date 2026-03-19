# Crie um programa que leia quanto dinheiro a pessoa tem na wallet e mostre quantos dollars ela pode comprar
# Considere o dolar a: US$ 1,00 = 3,27

import requests

r = requests.get("https://br.dolarapi.com/v1/cotacoes/usd")

rJson= r.json() # Pega a estrutura da request: {'moeda': 'USD', 'nome': 'Dólar', 'compra': 5.2293, 'venda': 5.2302, 'fechoAnterior': 5.3232, 'dataAtualizacao': '2026-03-12T20:59:58.000Z'}

valorDisp = float(input('Quanto R$ tem disponivel: '))
#                                                 rJson["venda"] acessa o campo "venda" do JSON retornado pela API, ou seja, a cotação usada no cálculo.
print(f'R$: {valorDisp}, compra US$ {(valorDisp / rJson['venda']):.2f} em doláres')
#                                                                :.2f Duas Casas Decimais

