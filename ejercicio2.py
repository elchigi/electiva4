def numMenor(Numero):
  arr = []
 
  for i in range(1, Numero):
    if i <= Numero:
      arr.append(i)
 
  print arr
  return arr
 
num = input("Digite un numero: ")
 
arrNumeros = numMenor(num)
