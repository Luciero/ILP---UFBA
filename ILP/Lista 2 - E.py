C,O,L,X = map(int,input().split())

C = C // 4
O = O // 8
L = L // 2
X = X // 1

Segundo = 1259
menor = C

if(O < menor):
  menor = O

if(L < menor):
  menor = L

if(X < menor):
  menor = X

Valor = Segundo * menor
H = Valor // 3600
M = (Valor % 3600)//60 
S = (Valor % 3600) % 60
print(H,'h',M,'m',S,'s')
