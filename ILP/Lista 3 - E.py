E,P = map(int,input().split())
F = 0

i = -1
while(i != P):

  E = E-P

  if(E <= 0):
    print(F+1)
    break
  elif(P == 0):
    print("F")
  P-=1
  if(P > 0):
    F+=1
