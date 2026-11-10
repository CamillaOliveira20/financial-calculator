preco_refeicao_crianca = float(input("Qual é o preço de uma refeição para criança? "))
preco_refeicao_adulto = float(input("Qual é o preço de uma refeição para adulto? "))
quantidade_de_adultos = int(input("Qual a quantidade de adultos? ")) 
quantidade_de_crianca = int(input("Qual a quantidade de crianças? "))       
preco_refeicao_crianca * quantidade_de_crianca
preco_refeicao_adulto * quantidade_de_adultos
subtotal = (preco_refeicao_crianca*quantidade_de_crianca) + (preco_refeicao_adulto*quantidade_de_adultos)
print(subtotal)

Qual_a_taxa_de_imposto_sobre_vendas = float(input("Qual é a taxa de imposto sobre vendas? "))
imposto = subtotal * (Qual_a_taxa_de_imposto_sobre_vendas/100)
print(f"Imposto: R$ {imposto:.2f}")
total = subtotal + imposto 
print(f"total: R$ {total: .2F}")
pagamento = float(input("Quanto dinheiro o cliente entregou? "))
troco = pagamento - total
print(f"troco: R$ {troco:.2f}")
