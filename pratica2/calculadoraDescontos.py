nomeP = "camiseta"
preco_original = 50.00
porcent_descont = 0.2

valorD = preco_original * porcent_descont
print(f" Valor do Desconto: R${valorD:.2f}")

precoF = preco_original - valorD
print(f"Preço final do produto: R${precoF:.2f}")