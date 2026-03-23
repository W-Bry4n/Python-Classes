# caixa registradora
total = 0.0
valor = -1
print("Bem-vindo ao Mercadinho Maria")
print("Digite o valor do produto ou 0 para finalizar")

while valor != 0:
  valor = float(input("Preço do produto: R$"))
  if valor >0:
    total = total + valor
    print(f"Subtotal: R$ {total:.2f}")
  elif valor <0:
    print("Valor inválido, sistema não aceita valor negativo")
print(f"valor total da compra: R$:{total:.2f} volte sempre!")