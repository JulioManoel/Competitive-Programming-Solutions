num = list(map(float, input().split()))
num.sort()
a, b, c = num[2], num[1], num[0]

if a >= b+c: print('NAO FORMA TRIANGULO')

else:
  if a**2 == b**2+c**2: print('TRIANGULO RETANGULO') 
  if a**2 > b**2+c**2: print('TRIANGULO OBTUSANGULO')
  if a**2 < b**2+c**2: print('TRIANGULO ACUTANGULO')
  if a == b and b == c: print('TRIANGULO EQUILATERO')
  elif  a == b or b == c: print('TRIANGULO ISOSCELES')
