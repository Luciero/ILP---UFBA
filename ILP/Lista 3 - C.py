N,X,XPmin = map(int,input().split())

for i in range(N):
  XP,Q = map(int,input().split())
  if(XP >= XPmin):
    print(X + XP,Q + 1)
  else:
    print(XP,Q)
