h = float(input("Digite a altura da parede: "))
c = float(input("Digite o comprimento da parede: "))
area = h * c
cobertura = area / 3
baldes = cobertura / 3.6
valor = baldes * 107
print ("Precisará de" ,baldes, "baldes de tinta. O valor será R$",valor)