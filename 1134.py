#Tipo de combustivel
alcool = 0
gasolina = 0
diesel = 0

while True:
  combustivel = int(input())
  while combustivel < 1 or combustivel > 4:
      combustivel = int(input())

  if combustivel == 1:
    alcool += 1
  elif combustivel == 2:
    gasolina += 1
  elif combustivel == 3:
    diesel += 1
  else:
    break

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}")
