N1,N2,N3,N4,N5,N6 = map(int,input().split())

R = N1 + N2 + N3 + N4 + N5 + N6
if(R >= 250):
  print("S+")
elif(R >= 200):
  print("S")
elif(R >= 180):
  print("S-")
elif(R >= 150):
  print("A+")
elif(R >= 100):
  print("A")
elif(R >= 80):
  print("A-")
elif(R >= 60):
  print("B+")
elif(R >= 40):
  print("B")
elif(R <= 39):
  print("B-")
