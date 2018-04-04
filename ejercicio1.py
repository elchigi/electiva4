num = input("Ingrese el numero a calcular")
 
divisor = 0
contador = 0
 
Arreglo= []
 
print("divisores:")
 
if num % 2 == 0:
  iterar = num / 2
else:
  iterar = (num - 1) / 2
 
for i in range(1, int(iterar) + 1):
  if num % i == 0:
    Arreglo.append(i)
    contador = contador + 1
 
  if contador == 10:
    break
 
print Arreglo
