def numMenor(Numero):
  arr = []
 
  for i in range(1, (Numero + 1)):
    arr.append(i)
 
  return arr
 
num = input("Digite un numero: ")
 
arrNumeros = numMenor(num)
 
print arrNumeros
 
sum = 0
 
for u in range(0, (num + 1)):
  sum = sum + u
 
print(sum)
