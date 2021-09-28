T = int(input())
maior = 0
  
P = int(input())

while(P != 0):
  P = int(input())
  if(P > maior):
    maior = P
if(maior > T):
  print("ALARME")
else:
  print("O Havai pode dormir tranquilo")  



