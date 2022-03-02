from math import pi
 
r = float(input("Valor do raio?"))
message = "A área do círculo é {:.3f}"

area = pi * r ** 2

print(message.format(area))