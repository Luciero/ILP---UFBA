N,M = map(int,input().split())
maior = 0

for i in range(N):
  M = input().split()
  soma = 0
  for j in M:
    j = int(j)
    soma = soma + j
    if(soma > maior):
      maior = soma
print(maior)    
    
