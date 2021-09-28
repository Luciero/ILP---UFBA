X = input()
Y = input()

X = int(X)
Y = int(Y)

if(X > 0):
  if(Y > 0):
    print("Quadrante 1")
  else:
    print("Quadrante 4")

if(X < 0):
  if(Y > 0):
    print("Quadrante 2")
  else:
    print("Quadrante 3")
      
if(X == 0 and Y == 0):
  print("Centro")
