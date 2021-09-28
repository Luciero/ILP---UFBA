TR,I,TN = map(int,input().split());

if(TN == 2):
  print("VITORIA");

elif(TR <= 9 and I <= 3 and TN < 2):
  TR = 9 - TR;
  I = 3 - I;
  TN = 2 - TN;
  print(TR,I,TN);
