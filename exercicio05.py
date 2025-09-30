preco = float(input("Informe o preço do produto: R$"))
desconto = preco * 0.10
preco_final = preco - desconto
print(f"O preço do produto com 10% de desconto é: R${preco_final:.2f}")
